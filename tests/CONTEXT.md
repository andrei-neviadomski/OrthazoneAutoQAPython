# Context Document — Orthazone Header Tests
**Purpose:** Single source of truth for writing and maintaining header tests.
**Aligns with:** branch `feat/new-header-tests`, project `OrthazoneAutoQAPython`

---

## 1. Project Architecture

```
OrthazoneAutoQAPython/
├── admin/
│   └── admin_login_page.py          ← AdminLoginPage (teardown helper)
├── components/
│   ├── header.py                    ← Header component (ALL header logic lives here)
│   └── checkout_popup.py            ← Cart modal logic
├── pages/
│   ├── base_page.py                 ← BasePage: open/click/fill/get_text/take_screenshot
│   ├── home_page.py                 ← has self.header = Header(page)
│   ├── login_page.py                ← add_creds_and_login()
│   ├── logout_page.py               ← check_title()
│   ├── category_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_success_page.py
│   └── registration_page.py
├── tests/
│   ├── conftest.py                  ← fixtures: setup_base_test, setup_order_test
│   ├── test_header.py               ← header test suite (extend here)
│   ├── test_cart_popup_flow.py
│   ├── test_checkout_flow.py
│   └── test_registration_on_reg_page.py
├── docs/
│   ├── SPEC.md                      ← what to test
│   └── CONTEXT.md                   ← this file
├── .env.example
└── requirements.txt
```

### Key Architectural Rules

1. **Single `Header` class** — all header logic lives in `components/header.py`.
   Do NOT split into sub-components. Other files import `Header(page)` directly.

2. **`BasePage` pattern** — all classes inherit `BasePage`.
   Use `self.page` (not `self._page`). Helper methods: `self.click()`, `self.fill()`,
   `self.get_text()`. For complex locators, use `self.page.locator(...)` directly.

3. **No session-level auth caching** — tests that need a logged-in user
   perform login inline using `login_page.add_creds_and_login()`, OR
   use the `setup_logged_in_test` fixture (see Section 4).

4. **Assertions** — use `expect()` inside component methods for auto-retry behavior.
   Use plain `assert` for simple href/attribute checks in test body.

---

## 2. Header DOM Structure (Desktop)

```
<header>
  └── div.int-header-wrap                    ← desktop header root
        ├── div.int-header-top               ← ZONE-1: Top bar
        │     ├── div.int-header-top-customers
        │     │     └── div.int-header-top-counter
        │     │           └── span × 5       ← one span per digit
        │     └── div.int-header-top-right
        │           ├── a.int-header-top-right-link.is_current    ← Shopping+
        │           ├── a[href*=drstorelist]                       ← Inventory (VIP)
        │           ├── a[href*=drslider]                          ← Payment (VIP)
        │           ├── a[href*=account/lab]                       ← Lab Tracker (VIP)
        │           │     └── span.int-header-top-badge (×3)       ← "VIP" labels
        │           └── div.int-header-top-right-account
        │                 ├── button.int-account-button            ← click trigger
        │                 │     └── div.int-account-button-text
        │                 │           └── span:first-child          ← "Hi Name!" or "Hi"
        │                 └── div.y-modal.is_user                  ← dropdown (desktop)
        │                       ├── a[href*=account/account]       ← My Account (AUTH only)
        │                       └── a[href*=account/logout]        ← Logout (AUTH only)
        ├── div.int-header-left              ← ZONE-2: Logo
        │     ├── p.int-header-left-serving  ← slogan
        │     ├── a[href="/"] > img[alt="logo"]
        │     └── div.secondary > img[alt="aao"]
        ├── div.int-header-center            ← ZONE-3+4: Nav + Search
        │     ├── div.int-header-center-top
        │     │     ├── a[href="tel:800-833-7132"]
        │     │     ├── a[href="/clearance"]
        │     │     ├── a[href*=brands]
        │     │     ├── a[href*=sampledashboard]
        │     │     ├── a[href*=allorders]
        │     │     └── a[href*=quickreorder]
        │     └── div#search.int-header-search
        │           ├── input.y-search__inp.int-header-search-input
        │           ├── button.int-header-search-button
        │           └── div.search_results_container  ← AJAX (injected on 3+ chars)
        │                 ├── div.search_results_left
        │                 │     └── div.search_results_searches
        │                 └── div.search_results_right  ← product results
        ├── div.int-header-right             ← ZONE-5: Wishlist + Cart
        │     ├── a.int-wishlist-button[href*=wishlist]
        │     │     └── span.int-wishlist-button-indicator
        │     ├── button.int-cart-button.is_cart
        │     │     └── span.int-cart-text-indicator[data-quantity]
        │     └── div.y-modal.is_cart        ← cart modal (desktop)
        │           ├── div.y-modal__title
        │           ├── div.y-basket-card (×N)
        │           ├── div.y-modal__cart-total
        │           │     └── div.y-modal__cart-total--row (×3)
        │           ├── a[href*=checkout/cart]   ← View Cart
        │           └── a[href*=check-out]        ← Checkout
        └── div.int-header-categories        ← ZONE-6: Category pills
              ├── a[href*=general-dentistry]  ← Dental
              ├── a[href*=surgical-and-implant] ← Surgery
              └── a[href=""]                  ← Orthodontic (⚠ empty href!)
```

**⚠ DUPLICATE ELEMENTS IN MOBILE DOM AND FOOTER**
`div.y-header-mobile` (hidden at 1280px+) contains duplicate:
- `button.int-cart-button.is_cart` — 2 in DOM
- `div.y-modal.is_cart` — 2 in DOM
- `button.int-account-button` — 2 in DOM
- `input.y-search__inp` — 2 in DOM
- VIP links (`drstorelist`, `drslider`, `account/lab`) — 2 in DOM each (desktop `int-header-top-right-link` + mobile `y-header-mobile__tabs-link`)

Additionally, these appear outside the header entirely:
- `a[href="tel:800-833-7132"]` — **3 in DOM**: desktop header + mobile header + **footer**
- `a[href*="/brands"]` — **2 in DOM**: desktop header + **footer** (`ftr-menu__link`)

**Two patterns used to handle duplicates (depending on element):**
```python
# Pattern A: .filter(visible=True).first — for elements only visible at current viewport
self.page.locator(".int-cart-text-indicator").filter(visible=True).first

# Pattern B: CSS scope to parent container — for elements also in footer (not hideable by viewport)
self.page.locator(".int-header-center-top a[href='tel:800-833-7132']")
self.page.locator("a.int-header-top-right-link[href*='drstorelist']")
```
**DO NOT** use `locator.nth(0)` — order is not guaranteed.
**DO NOT** use `.filter(visible=True)` for elements that also appear in footer — footer may be visible at desktop viewport.

---

## 3. Selector Reference Table

All selectors for `Header` component methods. Use `self.page.locator(SELECTOR)`.

| Element | Selector | Notes |
|---------|----------|-------|
| Customer counter block | `.int-header-top-counter` | Unique — no duplicate in mobile |
| Counter digit spans | `.int-header-top-counter span` | Expect count == 5 |
| Shopping+ link | `a.int-header-top-right-link.is_current` | Unique |
| Inventory link | `a.int-header-top-right-link[href*="drstorelist"]` | Desktop class prevents mobile tab duplicate |
| Payment link | `a.int-header-top-right-link[href*="drslider"]` | Desktop class prevents mobile tab duplicate |
| Lab Tracker link | `a.int-header-top-right-link[href*="account/lab"]` | Desktop class prevents mobile tab duplicate |
| VIP badges | `a.int-header-top-right-link:not(.is_current) .int-header-top-badge` | Excludes Shopping+ (is_current) which also has a badge → 3 not 4 |
| Account button | `button.int-account-button` | ⚠ Duplicate → `.filter(visible=True).first` |
| Account greeting | `.int-account-button-text span:first-child` | ⚠ Duplicate → `.filter(visible=True).first` |
| Account modal (desktop) | `.int-header-top-right-account .y-modal.is_user` | Scoped — unique |
| My Account link | `.int-header-top-right-account a[href*="account/account"]` | AUTH only |
| Logout link | `.int-header-top-right-account a[href*="account/logout"]` | AUTH only |
| Slogan | `p.int-header-left-serving` | Unique |
| Main logo link | `.int-header-left a[href="/"]` | Use `.first` (logo + home links) |
| Main logo img | `.int-header-left img[alt="logo"]` | Unique |
| AAO logo img | `.int-header-left img[alt="aao"]` | Unique |
| Phone link | `.int-header-center-top a[href="tel:800-833-7132"]` | ⚠ 3 in DOM (header + mobile + footer) → scope to center-top |
| Clearance link | `.int-header-center-top a[href*="clearance"]` | Scoped defensively |
| Brands link | `.int-header-center-top a[href*="/brands"]` | ⚠ Duplicate in footer → scope to center-top |
| Dashboard link | `.int-header-center-top a[href*="sampledashboard"]` | Scoped defensively |
| Your Orders link | `.int-header-center-top a[href*="allorders"]` | Scoped defensively |
| Buy again link | `.int-header-center-top a[href*="quickreorder"]` | Scoped defensively |
| Search input | `input.y-search__inp.int-header-search-input` | `.y-search__inp` alone is duplicate; combined class is desktop-only — unique |
| Search button | `button.int-header-search-button` | Unique (has `int-header-search-button` class) |
| Search dropdown | `div.search_results_container` | ⚠ Duplicate → `.filter(visible=True).first` |
| Search results right | `div.search_results_right` | ⚠ Duplicate → `.filter(visible=True).first` |
| Wishlist button | `a.int-wishlist-button` | Unique (desktop only element) |
| Wishlist count | `.int-wishlist-button-indicator` | Unique |
| Cart button | `button.int-cart-button.is_cart` | ⚠ Duplicate → `.filter(visible=True).first` |
| Cart count | `.int-cart-text-indicator` | ⚠ Duplicate → `.filter(visible=True).first` |
| Cart modal | `.int-header-right .y-modal.is_cart` | Scoped to `.int-header-right` — unique |
| Cart modal title | `div.y-modal__title` | ⚠ Duplicate → `.filter(visible=True).first` |
| Cart close button | `.int-header-right button.y-modal__btn-close` | Scoped |
| Cart product cards | `.int-header-right .y-basket-card` | Scoped |
| Cart total rows | `.int-header-right .y-modal__cart-total--row` | Scoped |
| View Cart button | `.int-header-right a.y-modal__cart-btn:has-text('View Cart')` | Scoped — unique |
| Checkout button | `.int-header-right a.y-modal__cart-btn:has-text('Checkout')` | Scoped — unique |
| Category pills | `.int-header-categories .int-header-categories-pill` | Unique |
| Dental pill | `.int-header-categories a[href*="general-dentistry"]` | Unique |
| Surgery pill | `.int-header-categories a[href*="surgical-and-implant"]` | Unique |
| Orthodontic pill | `.int-header-categories .int-header-categories-pill:last-child` | href="" — test visibility only! |

---

## 4. Fixtures (conftest.py)

### Existing fixtures

```python
# Unauthenticated. Opens homepage, clears cookies/storage on teardown.
# Use for: ANON tests
@pytest.fixture(scope="function")
def setup_base_test(page, context) -> HomePage
```

```python
# Unauthenticated. Opens homepage + cleans up orders/customers in admin on teardown.
# Use for: tests that create orders (checkout, registration)
@pytest.fixture(scope="function")
def setup_order_test(page, context) -> HomePage
```

### New fixture (added in this branch)

```python
# Authenticated. Opens homepage, logs in, yields HomePage.
# Clears cookies on teardown.
# Use for: TOP-015..019 (account dropdown auth state)
@pytest.fixture(scope="function")
def setup_logged_in_test(page, context) -> HomePage
```

---

## 5. Known Quirks & Edge Cases

### 5.1 Search Autocomplete
- **Debounce:** 1000ms. Use `.type(text, delay=100)` (simulates human typing)
  OR `page.fill()` + `page.wait_for_timeout(1500)`. Existing code uses `.type(delay=100)`.
- **Minimum chars:** 3. Below 3 → no AJAX call → no dropdown.
- **Dropdown detection:** `div.search_results_container` (injected into `#search`).
- **Existing code uses:** `search_popup.wait_for(state="visible", timeout=15000)`.

### 5.2 Cart & Account Modals
- The cart modal (`.int-header-right .y-modal.is_cart`) stays `display:block`, `visibility:visible`
  at all times. Two approaches were tried and confirmed NOT to work on this site:
  - `is_visible()` / `wait_for(state="hidden")` — always returns True/never fires
  - `getBoundingClientRect()` viewport check — modal rect does not change between open/closed
- **Root cause (confirmed across 2 test runs):** Journal2 controls the cart panel using
  `pointer-events: none` (closed) / `pointer-events: auto` (open), keeping the DOM element
  visually rendered but non-interactive when hidden.
- Open/closed detection uses **`window.getComputedStyle(el).pointerEvents`** via `page.evaluate()`:
  - Open: `pointerEvents !== 'none'`
  - Closed: `pointerEvents === 'none'`
- `open_cart_modal()` → clicks cart button + `page.wait_for_function(_CART_MODAL_OPEN_JS)`.
- `close_cart_modal()` → clicks close button + `page.wait_for_function(_CART_MODAL_CLOSED_JS)`.
- `cart_modal_is_visible()` → returns bool from `page.evaluate(_CART_MODAL_OPEN_JS)`.
- The account dropdown modal uses a different mechanism — `is_visible()` works for it.
- Existing `click_cart_popup_button()` uses `get_text()` with `assert ==` (not `expect()`).
  New methods should use `expect()` for consistency with other components.

### 5.3 Account dropdown — scoping
- Desktop account modal: `.int-header-top-right-account .y-modal.is_user`
  This selector is unique (scoped to the desktop zone). No `.filter(visible=True)` needed.
- The existing `ACCOUNT_BUTTON = 'span:has-text("Account")'` is text-based and
  may be fragile if text changes. New methods use `button.int-account-button` with
  `.filter(visible=True).first`.

### 5.4 Orthodontic category pill
- `href=""` — links to current page, NOT a broken link. Test visibility only.

### 5.5 Customer counter
- Shows 5 `<span>` elements (animated odometer). Test the count of spans (5), 
  NOT the exact numeric value (changes between page loads).

### 5.6 Logo link
- `a[href="/"]` matches BOTH the logo link AND possibly others.
  Use `.int-header-left a[href="/"]` to scope.

### 5.7 Auth: account dropdown state
- **Guest:** clicking account button shows Login + Register buttons (via `ACCOUNT_BUTTON` = `span:has-text("Account")`).
- **Logged in:** clicking account button shows My Account + Logout links.
  Greeting text `Hi Name!` is in `span:first-child` inside `.int-account-button-text`.
- Note: existing `ACCOUNT_BUTTON = 'span:has-text("Account")'` works for both states
  because "Account" text is always in the button. Do NOT change this selector.

---

## 6. Environment Variables

```bash
# .env (copy from .env.example)
BASE_URL=https://orthazone.com/       # target environment URL

ADMIN_USERNAME=                        # OpenCart admin username
ADMIN_PASSWORD=                        # OpenCart admin password
ADMIN_TEST_EMAIL=                      # test customer email (login in tests)
ADMIN_TEST_PASSWORD=                   # test customer password
ADMIN_NEW_EMAIL=                       # new email for registration tests
```

> ⚠️ Never put `TEST_EMAIL` / `TEST_PASSWORD` — those are NOT the var names used in this project.
> Correct names: `ADMIN_TEST_EMAIL`, `ADMIN_TEST_PASSWORD`.

---

## 7. How to Run

```bash
# Install deps
pip install pytest-playwright python-dotenv

# Install browsers
playwright install chromium

# Run all tests
pytest tests/ -s

# Run only header tests
pytest tests/test_header.py -s -v

# Screenshots + tracing only on failure (matches CI config)
pytest tests/ -s --screenshot only-on-failure --tracing retain-on-failure --output=test-results

# Headed mode for debugging
pytest tests/test_header.py -s --headed --slowmo 500
```

---

## 8. Code Style Conventions

```python
# ✅ Correct: test function names are fully lowercase snake_case
def test_top001_customer_counter_visible(page, setup_base_test): ...
def test_cart010_cart_modal_shows_subtotal(page, setup_cart_with_product): ...

# ❌ Wrong: no uppercase letters in test names
def test_TOP001_customer_counter_visible(page, setup_base_test): ...  # NO
def test_Cart010_cart_modal_shows_subtotal(page, setup_base_test): ...  # NO

# ✅ Correct: class constant for selectors
class Header(BasePage):
    CART_BUTTON = 'button.int-cart-button.is_cart'

    def some_method(self):
        self.page.locator(self.CART_BUTTON).filter(visible=True).first.click()

# ✅ Correct: use expect() for assertions with auto-retry
def verify_something(self):
    expect(self.page.locator(".some-element")).to_be_visible(timeout=15000)

# ✅ Correct: assert for simple attribute checks
def test_something(page, setup_base_test):
    header = Header(page)
    href = header.get_phone_href()
    assert href == "tel:800-833-7132"

# ❌ Wrong: don't create sub-components
class TopBarComponent:  # NO — keep everything in Header

# ❌ Wrong: don't use index-based nth() for deduplication
self.page.locator(".int-cart-text-indicator").nth(0)  # NO

# ✅ Correct: use .filter(visible=True).first for deduplication
self.page.locator(".int-cart-text-indicator").filter(visible=True).first
```
