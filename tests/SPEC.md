# Test Specification — Orthazone
**Project:** OrthazoneAutoQAPython
**URL:** configured via `BASE_URL` env var (default: `https://orthazone.com/`)
**Framework:** Python + Playwright (sync) + pytest

---

## 1. Test Naming Convention

### Format

```
test_{area}{NNN}_{description}
```

| Part | Rule | Example |
|------|------|---------|
| `area` | 2–4 lowercase letters, identifies the test area | `top`, `chk`, `reg` |
| `NNN` | 3-digit sequential number within the area, starting at 001 | `001`, `012` |
| `description` | snake_case, states what is verified | `cart_button_visible` |

### Area Prefixes

| Prefix | Area | File |
|--------|------|------|
| `top` | Header — Top Bar | `test_header.py` |
| `logo` | Header — Logo & Slogan | `test_header.py` |
| `nav` | Header — Navigation & Phone | `test_header.py` |
| `srch` | Header — Search | `test_header.py` |
| `cart` | Header — Cart & Wishlist widget | `test_header.py` |
| `cat` | Header — Category Pills | `test_header.py` |
| `cpop` | Cart Popup Flow (add/remove product) | `test_cart_popup_flow.py` |
| `chk` | Checkout Flow | `test_checkout_flow.py` |
| `reg` | Registration | `test_registration_on_reg_page.py` |

### Rules

- All letters in the function name are **lowercase** — no `CamelCase`, no `UPPERCASE`.
- The spec ID in the **docstring** keeps uppercase for readability: `"""TOP-001: ..."""`.
- Numbers are gapless within an area. When a test is deleted, its number is retired (not reused).
- Tests covering multiple spec rows in one function use a range: `test_nav002_to_nav006_nav_links_visible`.

### Legacy tests

Three tests in `test_header.py` were written before this naming convention was introduced.
They are left unchanged to preserve git history, but their proposed canonical names are noted below.

---

## 2. Fixtures Reference

| Fixture | Auth state | What it does | Teardown |
|---------|-----------|--------------|----------|
| `setup_base_test` | ANON | Opens homepage, verifies title | `clear_cookies` + `localStorage.clear()` |
| `setup_logged_in_test` | AUTH | Opens homepage, logs in via account dropdown | `clear_cookies` + `localStorage.clear()` |
| `setup_cart_with_product` | ANON | Opens homepage, adds Metal Brackets Mini (MBT .018 / Hooks On 3 / UR3) to cart | `clear_cookies` + `localStorage.clear()` |
| `setup_order_test` | ANON\* | Opens homepage, verifies title | `clear_cookies` + admin cleanup of orders and new customer |

\* `setup_order_test` starts anonymous. Tests using it (`test_checkout_flow`, `test_reg_on_reg_page`) perform login or registration **inside the test body** as part of the scenario.

---

## 3. Test Suites

### 3.1 `test_header.py` — Header

#### Legacy tests (pre-convention)

| Test function | Proposed canonical name | Scenario | Auth | Fixture |
|---------------|------------------------|----------|------|---------|
| `test_cart_counter` | `test_cart009_counter_increments_after_add` | Add product → cart counter changes from 0 | ANON | `setup_base_test` |
| `test_search_popup` | `test_srch003_popup_shows_product_results` | Type 5-digit query → product appears in dropdown | ANON | `setup_base_test` |
| `test_check_login_logout` | `test_top013_login_and_logout_via_account_dropdown` | Click Account → Login → verify home → Logout → verify logout page | ANON | `setup_base_test` |

---

#### ZONE-1: Top Bar

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| TOP-001 | `test_top001_customer_counter_visible` | Customer counter block is visible | ANON | `setup_base_test` |
| TOP-002 | `test_top002_customer_counter_has_five_digits` | Counter renders exactly 5 digit spans | ANON | `setup_base_test` |
| TOP-003 | `test_top003_shopping_plus_visible` | Shopping+ link is visible | ANON | `setup_base_test` |
| TOP-004 | `test_top004_inventory_link_visible` | Inventory Management link is visible | ANON | `setup_base_test` |
| TOP-005 | `test_top005_payment_link_visible` | Payment Slider link is visible | ANON | `setup_base_test` |
| TOP-006 | `test_top006_lab_tracker_link_visible` | Lab Case Tracker link is visible | ANON | `setup_base_test` |
| TOP-007 | `test_top007_three_vip_badges_visible` | Exactly 3 VIP badges are present | ANON | `setup_base_test` |
| TOP-008 | `test_top008_shopping_plus_href_is_home` | Shopping+ href is `/` | ANON | `setup_base_test` |
| TOP-009 | `test_top009_inventory_href_contains_drstorelist` | Inventory href contains `drstorelist` | ANON | `setup_base_test` |
| TOP-010 | `test_top010_payment_href_contains_drslider` | Payment href contains `drslider` | ANON | `setup_base_test` |
| TOP-011 | `test_top011_lab_tracker_href_contains_account_lab` | Lab Tracker href contains `account/lab` | ANON | `setup_base_test` |
| TOP-012 | `test_top012_account_button_visible` | Account button is visible | ANON | `setup_base_test` |
| TOP-013 | *(legacy: `test_check_login_logout`)* | Login → verify home → Logout → verify logout page | ANON | `setup_base_test` |
| TOP-015 | `test_top015_greeting_text_non_empty_when_logged_in` | Greeting text is non-empty when logged in | AUTH | `setup_logged_in_test` |
| TOP-016 | `test_top016_my_account_link_visible_when_logged_in` | My Account link visible in dropdown | AUTH | `setup_logged_in_test` |
| TOP-018 | `test_top018_my_account_href_contains_account_account` | My Account href contains `account/account` | AUTH | `setup_logged_in_test` |
| TOP-019 | `test_top019_logout_href_contains_account_logout` | Logout href contains `account/logout` | AUTH | `setup_logged_in_test` |

> Numbers TOP-014 and TOP-017 are retired (scenarios covered by legacy `test_check_login_logout`).

---

#### ZONE-2: Logo & Slogan

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| LOGO-001 | `test_logo001_slogan_visible` | Slogan "Serving the Dental Professionals Since 2015" is visible | ANON | `setup_base_test` |
| LOGO-002 | `test_logo002_main_logo_visible` | Main logo image is visible | ANON | `setup_base_test` |
| LOGO-003 | `test_logo003_aao_logo_visible` | AAO logo image is visible | ANON | `setup_base_test` |
| LOGO-004 | `test_logo004_main_logo_links_to_home` | Main logo link href is `/` | ANON | `setup_base_test` |

---

#### ZONE-3: Navigation & Phone

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| NAV-001 | `test_nav001_phone_link_visible` | Phone link visible, contains `(800) 833-7132` | ANON | `setup_base_test` |
| NAV-002..006 | `test_nav002_to_nav006_nav_links_visible` | Clearance, Brands, Dashboard, Your Orders, Buy Again are visible | ANON | `setup_base_test` |
| NAV-007 | `test_nav007_phone_href_is_tel_link` | Phone href equals `tel:800-833-7132` | ANON | `setup_base_test` |

---

#### ZONE-4: Search

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| SRCH-001 | `test_srch001_search_input_visible` | Search input field is visible | ANON | `setup_base_test` |
| SRCH-002 | `test_srch002_search_button_visible` | Search button is visible | ANON | `setup_base_test` |
| SRCH-003 | *(legacy: `test_search_popup`)* | Type ≥ 3 chars → product dropdown appears | ANON | `setup_base_test` |
| SRCH-005 | `test_srch005_short_query_no_dropdown` | Type < 3 chars → dropdown does NOT appear | ANON | `setup_base_test` |

> SRCH-004 is retired (covered by legacy `test_search_popup`).

---

#### ZONE-5: Cart & Wishlist

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| CART-001 | `test_cart001_wishlist_button_visible` | Wishlist button is visible | ANON | `setup_base_test` |
| CART-002 | `test_cart002_wishlist_href_contains_wishlist` | Wishlist href contains `account/wishlist` | ANON | `setup_base_test` |
| CART-003 | `test_cart003_cart_button_visible` | Cart button is visible | ANON | `setup_base_test` |
| CART-004 | `test_cart004_cart_count_badge_visible` | Cart count badge is visible | ANON | `setup_base_test` |
| CART-005 | `test_cart005_cart_modal_hidden_before_click` | Cart modal is closed on page load | ANON | `setup_base_test` |
| CART-006 | *(legacy: `test_cart_counter`)* | Cart counter > 0 after adding product | ANON | `setup_base_test` |
| CART-010 | `test_cart010_cart_modal_shows_subtotal` | Cart modal shows Sub-Total row | ANON | `setup_cart_with_product` |
| CART-011 | `test_cart011_cart_modal_shows_total` | Cart modal shows Total row (exact match) | ANON | `setup_cart_with_product` |
| CART-012 | `test_cart012_view_cart_href` | View Cart href contains `checkout/cart` | ANON | `setup_cart_with_product` |
| CART-013 | `test_cart013_checkout_button_href` | Checkout href contains `check-out` | ANON | `setup_cart_with_product` |
| CART-014 | `test_cart014_close_button_hides_modal` | Close button hides cart modal | ANON | `setup_cart_with_product` |

> CART-007..009 are retired (covered by legacy tests and `test_cart_popup_flow.py`).

---

#### ZONE-6: Category Pills

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| CAT-001..003 | `test_cat001_to_cat003_all_pills_visible` | Dental, Surgery, Orthodontic pills are visible | ANON | `setup_base_test` |
| CAT-004 | `test_cat004_dental_pill_href` | Dental pill href contains `general-dentistry` | ANON | `setup_base_test` |
| CAT-005 | `test_cat005_surgery_pill_href` | Surgery pill href contains `surgical-and-implant` | ANON | `setup_base_test` |

---

### 3.2 `test_cart_popup_flow.py` — Cart Popup Flow

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| CPOP-001 | `test_cpop001_product_appears_in_cart_modal` | Add product → open cart modal → product name visible | ANON | `setup_base_test` |
| CPOP-002 | `test_cpop002_product_removed_from_cart_modal` | Add product → open cart modal → remove → empty cart message | ANON | `setup_base_test` |

> Current function names: `test_add_product_to_cart_popup`, `test_remove_product_from_cart_popup`.

---

### 3.3 `test_checkout_flow.py` — Checkout

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| CHK-001 | `test_chk001_full_checkout_flow` | Login → add product → cart modal → checkout → fill payment → sign → success page | AUTH\* | `setup_order_test` |

> Current function name: `test_checkout_flow`.
> \* Login happens inside the test body, not in the fixture.

---

### 3.4 `test_registration_on_reg_page.py` — Registration

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| REG-001 | `test_reg001_business_account_registration` | Open registration → fill all steps → verify account created | ANON | `setup_order_test` |

> Current function name: `test_reg_on_reg_page`.

---

## 4. Test Count Summary

| Area | Tests |
|------|-------|
| Header (all zones) | 39 |
| Cart Popup Flow | 2 |
| Checkout | 1 |
| Registration | 1 |
| **Total** | **43** |
