# Context Document — Orthazone
**Purpose:** Single source of truth for writing and maintaining automated tests.

---

## 1. Project Structure

```
OrthazoneAutoQAPython/
├── admin/
│   └── admin_login_page.py        ← Admin panel POM (used only in teardown)
├── components/
│   ├── header.py                  ← Header component — all 6 header zones
│   └── checkout_popup.py          ← Cart modal (add/remove product, checkout button)
├── pages/
│   ├── base_page.py               ← BasePage: open / click / fill / get_text / take_screenshot
│   ├── home_page.py               ← HomePage: check_title, click_category_by_name, set_stripe_cookie
│   │                                 Has self.header = Header(page)
│   ├── login_page.py              ← add_creds_and_login()
│   ├── logout_page.py             ← check_title()
│   ├── category_page.py           ← click_category_by_name(), click_product_by_name()
│   ├── product_page.py            ← select_option_value_by_name(), click_add_to_cart_button()
│   ├── cart_page.py               ← (stub — select_option_value_by_name only)
│   ├── checkout_page.py           ← Full checkout steps: delivery → address → coupon → payment → sign → submit
│   ├── checkout_success_page.py   ← verify_checkout_success_page()
│   └── registration_page.py       ← Multi-step registration: email → phone → password → business → name → submit
├── tests/
│   ├── conftest.py                ← All pytest fixtures + failure screenshot hook
│   ├── test_header.py             ← 42 header tests (all zones)
│   ├── test_cart_popup_flow.py    ← 2 cart popup tests
│   ├── test_checkout_flow.py      ← 1 checkout e2e test
│   └── test_registration_on_reg_page.py  ← 1 registration e2e test
├── .env.example                   ← Environment variable template
├── requirements.txt               ← pytest-playwright, python-dotenv
└── .github/workflows/run_tests.yml
```

### Key Architectural Rules

1. **Single `Header` class** — all header logic lives in `components/header.py`. Other files import `Header(page)` directly. Do not split into sub-components.
2. **`BasePage` pattern** — all classes inherit `BasePage`. Use `self.page` (not `self._page`). Wrappers: `self.click()`, `self.fill()`, `self.get_text()`. For complex locators, call `self.page.locator(...)` directly.
3. **No session-level auth caching** — tests that need a logged-in user perform login inline, or use `setup_logged_in_test`.
4. **Assertions** — use `expect()` inside component methods for auto-retry. Use plain `assert` for simple attribute/href checks in test bodies.
5. **Deduplication pattern** — use `.filter(visible=True).first` for elements that appear in both desktop and mobile DOM. Use CSS class scoping for elements that also appear in the footer.

---

## 2. Environment Variables

```bash
# .env (copy from .env.example, never commit)
BASE_URL=https://orthazone.com/        # target environment

ADMIN_USERNAME=                         # OpenCart admin panel username
ADMIN_PASSWORD=                         # OpenCart admin panel password
ADMIN_TEST_EMAIL=                       # test customer email (used for login in tests)
ADMIN_TEST_PASSWORD=                    # test customer password
ADMIN_NEW_EMAIL=                        # new email for registration tests (cleaned up after)
```

---

## 3. Fixtures

All fixtures are defined in `tests/conftest.py`.

### `setup_base_test`

```
Scope:     function
Auth:      ANON
Setup:     Opens BASE_URL, verifies homepage title
Teardown:  clear_cookies + localStorage.clear() + sessionStorage.clear()
Yields:    HomePage
Used by:   Most header tests, cart popup tests
```

### `setup_logged_in_test`

```
Scope:     function
Auth:      AUTH (ADMIN_TEST_EMAIL / ADMIN_TEST_PASSWORD)
Setup:     Opens BASE_URL → clicks Account → Login → fills creds → verifies homepage title
Teardown:  clear_cookies + localStorage.clear() + sessionStorage.clear()
Yields:    HomePage
Used by:   TOP-015, TOP-016, TOP-018, TOP-019
```

### `setup_cart_with_product`

```
Scope:     function
Auth:      ANON
Setup:     Opens BASE_URL → navigates to Metal Brackets Mini product page
           → selects MBT .018 / Hooks On 3 / Maxillary Right Canine (UR3) → clicks Add to Cart
Teardown:  clear_cookies + localStorage.clear() + sessionStorage.clear()
Yields:    HomePage
Used by:   CART-010, CART-011, CART-012, CART-013, CART-014
```

Product navigation path:
```
Homepage → Bracket Systems → Metal Brackets (Standard, Mini, Self-Ligating, Vertical Slot)
         → Metal Brackets - Mini Size → Metal Brackets - Mini
```

### `setup_order_test`

```
Scope:     function
Auth:      ANON (login/registration happens inside the test body)
Setup:     Opens BASE_URL, verifies homepage title
Teardown:  clear_cookies + localStorage.clear()
           → Admin login → delete orders for ADMIN_TEST_EMAIL
           → Admin panel → delete customer with ADMIN_NEW_EMAIL
Yields:    HomePage
Used by:   CHK-001 (test_checkout_flow), REG-001 (test_reg_on_reg_page)
```

> Note: `setup_order_test` performs admin cleanup **after** `clear_cookies` in teardown. This works because the admin login is a separate navigation step that establishes a fresh session.

---

## 4. Page Objects Reference

### `BasePage`

| Method | Signature | Notes |
|--------|-----------|-------|
| `open` | `open(url: str)` | `goto(url, wait_until="domcontentloaded", timeout=60000)` |
| `click` | `click(selector: str)` | `page.click(selector)` |
| `fill` | `fill(selector: str, text: str)` | `page.fill(selector, text)` |
| `get_text` | `get_text(selector: str) -> str` | `page.inner_text(selector)` |
| `take_screenshot` | `take_screenshot(name: str)` | Saves to `screenshots/` with timestamp |

---

### `HomePage`

Has `self.header = Header(page)`.

| Method | Notes |
|--------|-------|
| `check_title()` | Asserts page title == `"Orthodontic Supplies Store..."` |
| `click_category_by_name(name)` | Waits for `span.catagory-wrap__item--name` and clicks |
| `set_stripe_cookie()` | Sets `stripe_dev_test=1` cookie via JS (required for checkout test) |

---

### `LoginPage`

Reads `ADMIN_TEST_EMAIL` / `ADMIN_TEST_PASSWORD` from env.

| Method | Notes |
|--------|-------|
| `add_creds_and_login()` | Fills email + password + clicks Login button |

---

### `CategoryPage`

| Method | Notes |
|--------|-------|
| `click_category_by_name(name)` | Clicks `span.catagory-wrap__item--name:has-text(name)` |
| `click_product_by_name(name)` | Clicks `a.prodcard__link:has-text(name)` (first match) |

---

### `ProductPage`

| Method | Notes |
|--------|-------|
| `select_option_value_by_name(name)` | Clicks `label:has-text(name)` (radio/checkbox option) |
| `click_add_to_cart_button()` | Clicks `a:has-text('Add to Cart')` |

---

### `CheckoutPage`

Full multi-step checkout. Steps called in order:

| Method | Step |
|--------|------|
| `check_url()` | Asserts URL matches `check-out` |
| `click_continue_button_delivery_method_step()` | Clicks `#button-shipping-method` |
| `click_continue_button_shipping_adress_step()` | Clicks `#button-shipping-address` |
| `click_continue_button_coupon_voucher_step()` | Clicks `#button-coupon-voucher` |
| `fill_cc_data()` | Fills Stripe iframe fields: card `4242424242424242`, exp `0133`, cvc `111` |
| `click_continue_button_payment_info_step()` | Clicks `#button-confirm` |
| `sign_cc_payment()` | Draws signature on `canvas.jSignature` via mouse events |
| `click_submit_button_signature_step()` | Clicks `#button-submit-order` |

> Requires `set_stripe_cookie()` to be called before starting checkout (use `home_page.set_stripe_cookie()`).

---

### `CheckoutSuccessPage`

| Method | Notes |
|--------|-------|
| `verify_checkout_success_page()` | Asserts `.asteps__head` text == `"Your Order Has Been Processed!"` |

---

### `RegistrationPage`

Multi-step registration flow. Steps called in order:

| Method | Step |
|--------|------|
| `verify_reg_page_title()` | Asserts page title == `"Create Account"` |
| `fill_email()` | Fills `ADMIN_NEW_EMAIL` into `input[name="email"]` via `press_sequentially` |
| `fill_phone()` | Fills hardcoded `"5656565656"` |
| `fill_password()` | Fills `ADMIN_TEST_PASSWORD` |
| `fill_confirm_password()` | Fills `ADMIN_TEST_PASSWORD` again |
| `check_business_account()` | Selects business account type via JS (jQuery trigger) |
| `click_next_batton()` | Clicks `button[data-step-btn="next"]` + waits 2s |
| `verify_business_acount()` | Asserts `input[name="company_name"]` is visible |
| `fill_first_name()` | Fills `"Auto test new"` |
| `fill_last_name()` | Fills `"Auto test new"` |
| `verify_register_acount_step()` | Asserts `.aform__head` text == `"Register Account"` |
| `check_agree_checkbox()` | Clicks `label[for="agree"]` |
| `click_register_batton()` | Clicks `button[data-step-btn="send"]` + waits 2s |
| `verify_registation()` | Asserts `.asteps__head` text == `"Your Account Has Been Created!"` |

---

### `CheckoutPopUp` (component)

| Method | Notes |
|--------|-------|
| `verify_adding_product_by_name(name)` | Asserts `.line-clamp-2` first element has text == name |
| `remove_product_from_popup()` | Clicks `button.y-basket-card__remove` (first) |
| `verify_product_removed_from_popup()` | Asserts `.y-modal__header` contains `"YOUR SHOPPING CART IS EMPTY!"` |
| `click_checkout_button()` | Clicks `a.y-modal__cart-btn:has-text('Checkout')` (first) |

---

### `Header` (component)

All selectors are class constants. Methods grouped by zone.

#### Selector constants

| Constant | Value | Zone |
|----------|-------|------|
| `CART_BUTTON` | `'button.int-cart-button.is_cart'` | ZONE-5 (legacy) |
| `ACCOUNT_BUTTON` | `'span:has-text("Account")'` | ZONE-1 (legacy) |
| `LOGIN_BUTTON` | `'span:has-text("Login")'` | ZONE-1 (legacy) |
| `LOGOUT_BUTTON` | `'span:has-text("Logout")'` | ZONE-1 (legacy) |
| `REGISTER_BUTTON` | `'span:has-text("Register")'` | ZONE-1 (legacy) |
| `CUSTOMER_COUNTER` | `'.int-header-top-counter'` | ZONE-1 |
| `COUNTER_DIGIT_SPANS` | `'.int-header-top-counter span'` | ZONE-1 |
| `SHOPPING_PLUS_LINK` | `'a.int-header-top-right-link.is_current'` | ZONE-1 |
| `INVENTORY_LINK` | `'a.int-header-top-right-link[href*="drstorelist"]'` | ZONE-1 |
| `PAYMENT_LINK` | `'a.int-header-top-right-link[href*="drslider"]'` | ZONE-1 |
| `LAB_TRACKER_LINK` | `'a.int-header-top-right-link[href*="account/lab"]'` | ZONE-1 |
| `VIP_BADGES` | `'a.int-header-top-right-link:not(.is_current) .int-header-top-badge'` | ZONE-1 |
| `ACCOUNT_MODAL_DESKTOP` | `'.int-header-top-right-account .y-modal.is_user'` | ZONE-1 |
| `ACCOUNT_BUTTON_DESKTOP` | `'button.int-account-button'` | ZONE-1 |
| `MY_ACCOUNT_LINK` | `'.int-header-top-right-account a[href*="account/account"]'` | ZONE-1 |
| `LOGOUT_LINK_DESKTOP` | `'.int-header-top-right-account a[href*="account/logout"]'` | ZONE-1 |
| `ACCOUNT_GREETING` | `'.int-account-button-text span:first-child'` | ZONE-1 |
| `SLOGAN` | `'p.int-header-left-serving'` | ZONE-2 |
| `MAIN_LOGO_LINK` | `'.int-header-left a[href="/"]'` | ZONE-2 |
| `MAIN_LOGO_IMG` | `'.int-header-left img[alt="logo"]'` | ZONE-2 |
| `AAO_LOGO_IMG` | `'.int-header-left img[alt="aao"]'` | ZONE-2 |
| `PHONE_LINK` | `'.int-header-center-top a[href="tel:800-833-7132"]'` | ZONE-3 |
| `CLEARANCE_LINK` | `'.int-header-center-top a[href*="clearance"]'` | ZONE-3 |
| `BRANDS_LINK` | `'.int-header-center-top a[href*="/brands"]'` | ZONE-3 |
| `DASHBOARD_LINK` | `'.int-header-center-top a[href*="sampledashboard"]'` | ZONE-3 |
| `ORDERS_LINK` | `'.int-header-center-top a[href*="allorders"]'` | ZONE-3 |
| `BUY_AGAIN_LINK` | `'.int-header-center-top a[href*="quickreorder"]'` | ZONE-3 |
| `SEARCH_INPUT` | `'input.y-search__inp.int-header-search-input'` | ZONE-4 |
| `SEARCH_BUTTON` | `'button.int-header-search-button'` | ZONE-4 |
| `WISHLIST_BUTTON` | `'a.int-wishlist-button'` | ZONE-5 |
| `WISHLIST_COUNT` | `'.int-wishlist-button-indicator'` | ZONE-5 |
| `CART_MODAL` | `'.int-header-right .y-modal.is_cart'` | ZONE-5 |
| `CART_CLOSE_BUTTON` | `'.int-header-right button.y-modal__btn-close'` | ZONE-5 |
| `CART_TOTAL_ROWS` | `'.int-header-right .y-modal__cart-total--row'` | ZONE-5 |
| `VIEW_CART_BUTTON` | `".int-header-right a.y-modal__cart-btn:has-text('View Cart')"` | ZONE-5 |
| `CHECKOUT_BUTTON_MODAL` | `".int-header-right a.y-modal__cart-btn:has-text('Checkout')"` | ZONE-5 |
| `CATEGORY_PILLS` | `'.int-header-categories .int-header-categories-pill'` | ZONE-6 |
| `DENTAL_PILL` | `'.int-header-categories a[href*="general-dentistry"]'` | ZONE-6 |
| `SURGERY_PILL` | `'.int-header-categories a[href*="surgical-and-implant"]'` | ZONE-6 |
| `ORTHODONTIC_PILL` | `'.int-header-categories .int-header-categories-pill:last-child'` | ZONE-6 |

---

## 5. Known Quirks

### 5.1 Duplicate Elements (mobile DOM + footer)

`div.y-header-mobile` is always in DOM (hidden via CSS at viewport ≥ 1280px). It duplicates several header elements. Additionally, some elements exist in the footer.

| Selector fragment | DOM count | Resolution |
|-------------------|-----------|------------|
| `button.int-cart-button.is_cart` | 2 | `.filter(visible=True).first` |
| `div.y-modal.is_cart` | 2 | scope to `.int-header-right` |
| `button.int-account-button` | 2 | `.filter(visible=True).first` |
| `input.y-search__inp` | 2 | `.int-header-search-input` class makes it unique |
| VIP links (`drstorelist`, `drslider`, `account/lab`) | 2 each | `a.int-header-top-right-link` class (desktop only) |
| `a[href="tel:800-833-7132"]` | 3 (header + mobile + **footer**) | scope to `.int-header-center-top` |
| `a[href*="/brands"]` | 2 (header + **footer**) | scope to `.int-header-center-top` |

Two patterns used depending on element location:

```python
# Pattern A — element hidden in mobile, visible on desktop:
self.page.locator(".int-cart-text-indicator").filter(visible=True).first

# Pattern B — element also in footer (filter won't help — footer is visible):
self.page.locator(".int-header-center-top a[href='tel:800-833-7132']")
```

Do NOT use `.nth(0)` — element order in DOM is not guaranteed.

### 5.2 Cart Modal (Journal2 animation)

The cart modal stays `display:block` at all times. Playwright's `is_visible()` and `wait_for(state="hidden")` do not work.

**Confirmed non-working approaches (from 2 test runs):**
- `is_visible()` — always `True`
- `wait_for(state="hidden")` — never fires
- `getBoundingClientRect()` — modal rect does not change between open and closed

**Root cause:** Journal2 uses `pointer-events: none` (closed) / `pointer-events: auto` (open).

**Working approach:**
```python
# Open check:
window.getComputedStyle(el).pointerEvents !== 'none'

# Closed check:
window.getComputedStyle(el).pointerEvents === 'none'
```

Used via `page.evaluate()` for instant check and `page.wait_for_function()` for waiting.

### 5.3 Search Autocomplete

- Debounce: 1000ms after typing stops.
- Minimum 3 characters to trigger AJAX request.
- Existing code uses `.type(text, delay=100)` — simulates human typing to trigger debounce.
- New code uses `.fill()` (instant) for negative tests (SRCH-005).
- Dropdown selector: `div.search_results_container`.

### 5.4 VIP Badge Count

`Shopping+` link (`.is_current`) also has a badge element. The `VIP_BADGES` selector explicitly excludes it with `:not(.is_current)` to keep the count at 3.

### 5.5 Orthodontic Category Pill

Has `href=""` — links back to the current page. Test visibility only; do not test navigation.

### 5.6 Checkout Test Requirements

- Must call `set_stripe_cookie()` before navigating to checkout (enables test mode).
- Stripe iframe fields use `frame_locator` — they cannot be filled with standard `fill()`.
- Signature step requires mouse events (`mouse.move` + `mouse.down` + `mouse.up`).
- `setup_order_test` cleans up created orders and the new registered customer in teardown.

### 5.7 Registration Page — JS-driven steps

The business account type selection uses jQuery triggers (not a simple click):
```python
page.evaluate("jQuery('#registration_type_id_2').trigger('change'); ...")
```
This is required because the standard radio button is not directly clickable in the current UI.

---

## 6. How to Run

```bash
# Install
pip install pytest-playwright python-dotenv
playwright install chromium

# All tests
pytest tests/ -s

# One suite
pytest tests/test_header.py -s -v

# One test
pytest tests/test_header.py::test_top001_customer_counter_visible -s

# Headed + slow motion (for debugging)
pytest tests/test_header.py -s --headed --slowmo 500

# On failure only: screenshots + traces (matches CI config)
pytest tests/ -s --screenshot only-on-failure --tracing retain-on-failure --output=test-results

# Run against a specific environment
BASE_URL=https://stage2.dentazone.com/ pytest tests/ -s
```

---

## 7. Code Style

```python
# Test function names: fully lowercase snake_case
def test_top001_customer_counter_visible(page, setup_base_test): ...

# Class constants for all selectors (UPPER_CASE)
class Header(BasePage):
    CART_BUTTON = 'button.int-cart-button.is_cart'

# expect() for assertions with auto-retry (inside component methods)
def verify_something(self):
    expect(self.page.locator(".element")).to_be_visible(timeout=10000)

# assert for simple attribute checks (inside test bodies)
def test_top008_shopping_plus_href_is_home(page, setup_base_test):
    _ = setup_base_test
    header = Header(page)
    assert header.get_shopping_plus_href() == "/"

# Deduplication: .filter(visible=True).first — never .nth(0)
self.page.locator(".int-cart-text-indicator").filter(visible=True).first
```
