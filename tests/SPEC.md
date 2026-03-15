# Header Test Specification — Orthazone
**Version:** 2.0 | **Date:** 2026-03-13
**Branch:** feat/new-header-tests
**URL:** configurable via `BASE_URL` env var (default: `https://orthazone.com/`)
**Scope:** Desktop header only (viewport 1280px+)

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Already covered in existing tests |
| 🆕 | New — to be implemented in this branch |
| AUTH | Requires logged-in user (`ADMIN_TEST_EMAIL` / `ADMIN_TEST_PASSWORD`) |
| ANON | Works without login |

---

## ZONE-1: Top Bar (`.int-header-top`)

### Customer Counter

| ID | Scenario | Auth | Type | Status |
|----|----------|------|------|--------|
| TOP-001 | Customer counter block is visible | ANON | Smoke | 🆕 |
| TOP-002 | Counter renders exactly 5 digit `<span>` elements | ANON | Smoke | 🆕 |

### VIP Navigation Links

| ID | Scenario | Auth | Type | Status |
|----|----------|------|------|--------|
| TOP-003 | `Shopping+` link is visible | ANON | Smoke | 🆕 |
| TOP-004 | `Inventory Management` link is visible | ANON | Smoke | 🆕 |
| TOP-005 | `Payment Slider` link is visible | ANON | Smoke | 🆕 |
| TOP-006 | `Lab Case Tracker` link is visible | ANON | Smoke | 🆕 |
| TOP-007 | All three VIP badges are visible (count = 3) | ANON | Smoke | 🆕 |
| TOP-008 | `Shopping+` link `href` is `/` | ANON | Functional | 🆕 |
| TOP-009 | `Inventory` link `href` contains `drstorelist` | ANON | Functional | 🆕 |
| TOP-010 | `Payment` link `href` contains `drslider` | ANON | Functional | 🆕 |
| TOP-011 | `Lab Tracker` link `href` contains `account/lab` | ANON | Functional | 🆕 |

### Account Button & Dropdown

| ID | Scenario | Auth | Type | Status |
|----|----------|------|------|--------|
| TOP-012 | Account button is visible | ANON | Smoke | 🆕 |
| TOP-013 | Click account button (guest) → Login button appears | ANON | Functional | ✅ `test_check_login_logout` |
| TOP-014 | Click account button (guest) → Register button appears | ANON | Functional | ✅ `test_reg_on_reg_page` |
| TOP-015 | Logged-in: greeting text is non-empty (e.g. `Hi Name!`) | AUTH | Smoke | 🆕 |
| TOP-016 | Logged-in: click account button → `My Account` link visible | AUTH | Functional | 🆕 |
| TOP-017 | Logged-in: click account button → `Logout` link visible | AUTH | Functional | ✅ `test_check_login_logout` |
| TOP-018 | `My Account` `href` contains `account/account` | AUTH | Functional | 🆕 |
| TOP-019 | `Logout` `href` contains `account/logout` | AUTH | Functional | 🆕 |

---

## ZONE-2: Logo & Slogan (`.int-header-left`)

| ID | Scenario | Auth | Type | Status |
|----|----------|------|------|--------|
| LOGO-001 | Slogan "Serving the Dental Professionals Since 2015" is visible | ANON | Smoke | 🆕 |
| LOGO-002 | Main logo image (`alt="logo"`) is visible | ANON | Smoke | 🆕 |
| LOGO-003 | AAO logo image (`alt="aao"`) is visible | ANON | Smoke | 🆕 |
| LOGO-004 | Main logo `<a>` links to home (`href="/"`) | ANON | Functional | 🆕 |

---

## ZONE-3: Navigation Links & Phone (`.int-header-center-top`)

| ID | Scenario | Auth | Type | Status |
|----|----------|------|------|--------|
| NAV-001 | Phone link is visible, contains `(800) 833-7132` | ANON | Smoke | 🆕 |
| NAV-002 | `Clearance` link is visible | ANON | Smoke | 🆕 |
| NAV-003 | `Brands` link is visible | ANON | Smoke | 🆕 |
| NAV-004 | `Dashboard` link is visible | ANON | Smoke | 🆕 |
| NAV-005 | `Your Orders` link is visible | ANON | Smoke | 🆕 |
| NAV-006 | `Buy again` link is visible | ANON | Smoke | 🆕 |
| NAV-007 | Phone `href` equals `tel:800-833-7132` | ANON | Functional | 🆕 |

---

## ZONE-4: Search (`.int-header-center #search`)

| ID | Scenario | Auth | Type | Status |
|----|----------|------|------|--------|
| SRCH-001 | Search input is visible | ANON | Smoke | 🆕 |
| SRCH-002 | Search button is visible | ANON | Smoke | 🆕 |
| SRCH-003 | Typing ≥ 3 chars → dropdown `.search_results_container` appears | ANON | Functional | ✅ `test_search_popup` |
| SRCH-004 | Product results section visible in dropdown | ANON | Functional | ✅ `test_search_popup` (`verify_search_popup`) |
| SRCH-005 | Typing < 3 chars → dropdown does NOT appear | ANON | Functional | 🆕 |

> `test_search_popup` uses query `"12355"` and expects a specific product.
> SRCH-003/004 are already green. SRCH-005 is missing.

---

## ZONE-5: Wishlist & Cart (`.int-header-right`)

| ID | Scenario | Auth | Type | Status |
|----|----------|------|------|--------|
| CART-001 | Wishlist button is visible | ANON | Smoke | 🆕 |
| CART-002 | Wishlist `href` contains `account/wishlist` | ANON | Functional | 🆕 |
| CART-003 | Cart button is visible | ANON | Smoke | 🆕 |
| CART-004 | Cart count badge is visible | ANON | Smoke | 🆕 |
| CART-005 | Cart modal hidden before click | ANON | Functional | 🆕 |
| CART-006 | Click cart button → modal title `SHOPPING CART` visible | ANON | Functional | ✅ `click_cart_popup_button()` (used in multiple tests) |
| CART-007 | Cart modal contains ≥ 1 product card (after adding product) | ANON | Functional | ✅ `test_add_product_to_cart_popup` |
| CART-008 | Remove product → empty cart message appears | ANON | Functional | ✅ `test_remove_product_from_cart_popup` |
| CART-009 | Cart counter increments after adding product | ANON | Functional | ✅ `test_cart_counter` |
| CART-010 | Modal shows `Sub-Total` row | ANON | Functional | 🆕 |
| CART-011 | Modal shows `Total` row | ANON | Functional | 🆕 |
| CART-012 | `View Cart` href contains `checkout/cart` | ANON | Functional | 🆕 |
| CART-013 | `Checkout` href contains `check-out` | ANON | Functional | 🆕 |
| CART-014 | Close button hides the modal | ANON | Functional | 🆕 |

---

## ZONE-6: Category Pills (`.int-header-categories`)

| ID | Scenario | Auth | Type | Status |
|----|----------|------|------|--------|
| CAT-001 | `Dental` pill is visible | ANON | Smoke | 🆕 |
| CAT-002 | `Surgery` pill is visible | ANON | Smoke | 🆕 |
| CAT-003 | `Orthodontic` pill is visible | ANON | Smoke | 🆕 |
| CAT-004 | `Dental` href contains `general-dentistry` | ANON | Functional | 🆕 |
| CAT-005 | `Surgery` href contains `surgical-and-implant` | ANON | Functional | 🆕 |

---

## Summary

| Zone | Total | ✅ Existing | 🆕 New |
|------|-------|------------|--------|
| ZONE-1 Top Bar | 19 | 3 | 16 |
| ZONE-2 Logo | 4 | 0 | 4 |
| ZONE-3 Nav & Phone | 7 | 0 | 7 |
| ZONE-4 Search | 5 | 2 | 3 |
| ZONE-5 Cart | 14 | 4 | 10 |
| ZONE-6 Categories | 5 | 0 | 5 |
| **Total** | **54** | **9** | **45** |

---

## Out of Scope (v2.0)
- Visual regression / screenshot comparison
- Accessibility / ARIA checks
- Mobile header (`div.y-header-mobile`)
- Sticky menu (`.y-menu-sticky`)
- Search results page content
- Admin panel interactions
