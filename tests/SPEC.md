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
| `nav` | Header — Navigation | `test_header.py` |
| `srch` | Header — Search | `test_header.py` |
| `cart` | Header — Wishlist & Cart | `test_header.py` |
| `cpop` | Cart Popup Flow (add/remove product) | `test_cart_popup_flow.py` |
| `chk` | Checkout Flow | `test_checkout_flow.py` |
| `reg` | Registration | `test_registration_on_reg_page.py` |

### Rules

- All letters in the function name are **lowercase** — no `CamelCase`, no `UPPERCASE`.
- The spec ID in the **docstring** keeps uppercase for readability: `"""TOP-001: ..."""`.
- Numbers are gapless within an area. When a test is deleted, its number is retired (not reused).

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
| `test_check_login_logout` | `test_top016_login_and_logout_via_account_dropdown` | Click Account → Login → verify home → Logout → verify logout page | ANON | `setup_base_test` |

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
| TOP-012 | `test_top012_two_free_badges_visible` | Exactly 2 Free badges are present | ANON | `setup_base_test` |
| TOP-013 | `test_top013_dashboard_link_visible` | Dashboard link is visible | ANON | `setup_base_test` |
| TOP-014 | `test_top014_phone_link_visible` | Phone link visible, contains `(800) 833-7132` | ANON | `setup_base_test` |
| TOP-015 | `test_top015_phone_href_is_tel_link` | Phone href equals `tel:800-833-7132` | ANON | `setup_base_test` |


---

#### ZONE-2: Logo & Slogan

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| LOGO-001 | `test_logo001_slogan_visible` | Slogan "Serving the Dental Professionals Since 2015" is visible | ANON | `setup_base_test` |
| LOGO-002 | `test_logo002_main_logo_visible` | Main logo image is visible | ANON | `setup_base_test` |
| LOGO-003 | `test_logo003_aao_logo_visible` | AAO logo image is visible | ANON | `setup_base_test` |
| LOGO-004 | `test_logo004_main_logo_links_to_home` | Main logo link href is `/` | ANON | `setup_base_test` |

---

#### ZONE-3: Navigation & Search

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| NAV-001 | `test_nav001_nav_links_visible` | Clearance, Brands, Dental, Surgery, Orthodontic are visible | ANON | `setup_base_test` |
| SRCH-001 | `test_srch001_search_input_visible` | Search input field is visible | ANON | `setup_base_test` |
| SRCH-002 | `test_srch002_search_button_visible` | Search button is visible | ANON | `setup_base_test` |
| SRCH-003 | *(legacy: `test_search_popup`)* | Type ≥ 3 chars → product dropdown appears | ANON | `setup_base_test` |
| SRCH-005 | `test_srch005_short_query_no_dropdown` | Type < 3 chars → dropdown does NOT appear | ANON | `setup_base_test` |


---

#### ZONE-4: Wishlist & Cart

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| CART-001 | `test_cart001_wishlist_button_visible` | Wishlist button is visible | ANON | `setup_base_test` |
| CART-002 | `test_cart002_wishlist_href_contains_wishlist` | Wishlist href contains `account/wishlist` | ANON | `setup_base_test` |
| CART-003 | `test_cart003_account_button_visible` | Account button is visible | ANON | `setup_base_test` |
| CART-004 | `test_cart004_greeting_text_non_empty_when_logged_in` | Greeting text is non-empty when logged in | AUTH | `setup_logged_in_test` |
| CART-005 | `test_cart005_my_account_link_visible_when_logged_in` | My Account, Your Orders, Buy Again, Logout links visible in dropdown | AUTH | `setup_logged_in_test` |
| CART-006 | `test_cart006_my_account_href_contains_account_account` | My Account, Orders, Buy Again, Logout hrefs contain expected paths | AUTH | `setup_logged_in_test` |
| CART-007 | `test_cart007_cart_button_visible` *(rename pending)* | Cart button is visible | ANON | `setup_base_test` |
| CART-008 | `test_cart008_cart_count_badge_visible` *(rename pending)* | Cart count badge is visible | ANON | `setup_base_test` |
| CART-009 | *(legacy: `test_cart_counter`)* | Cart counter > 0 after adding product | ANON | `setup_base_test` |
| CART-010 | *(legacy: `test_check_login_logout`)* | Login → verify home → Logout → verify logout page | ANON | `setup_base_test` |


---

### 3.2 `test_cart_popup_flow.py` — Cart Popup Flow

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| CPOP-001 | *(legacy: `test_add_product_to_cart_popup`)* | Add product → open cart modal → product name visible | ANON | `setup_base_test` |
| CPOP-002 | *(legacy: `test_remove_product_from_cart_popup`)* | Add product → open cart modal → remove → empty cart message | ANON | `setup_base_test` |

---

### 3.3 `test_checkout_flow.py` — Checkout

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| CHK-001 | `test_checkout_flow` | Login → add product → cart modal → checkout → fill payment → sign → success page | AUTH\* | `setup_order_test` |

---

### 3.4 `test_registration_on_reg_page.py` — Registration

| ID | Test function | Scenario | Auth | Fixture |
|----|---------------|----------|------|---------|
| REG-001 | `test_reg_on_reg_page` | Open registration → fill all steps → verify account created | ANON | `setup_order_test` |

---

## 4. Test Count Summary

| Area | Implemented |
|------|-------------|
| Header TOP (ZONE-1) | 15 |
| Header LOGO (ZONE-2) | 4 |
| Header NAV+SRCH (ZONE-3) | 5 |
| Header CART (ZONE-4) | 10 | 
| Cart Popup Flow | 2 |
| Checkout | 1 |
| Registration | 1 | 
| **Total** | **38** |
