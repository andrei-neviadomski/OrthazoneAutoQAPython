"""Test Suite for Header"""
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from components.header import Header

# ════════════════════════════════════════════════════════════════════════════
# Existing tests (DO NOT change)
# ════════════════════════════════════════════════════════════════════════════

def test_cart_counter(page, setup_base_test):
    """Test cart counter in the header"""

    home_page = setup_base_test
    category_page = CategoryPage(page)
    product_page = ProductPage(page)
    header = Header(page)

    home_page.click_category_by_name("Bracket Systems")
    category_page.click_category_by_name(
        "Metal Brackets (Standard, Mini, Self-Ligating, Vertical Slot)"
        )
    category_page.click_category_by_name("Metal Brackets - Mini Size")
    category_page.click_product_by_name("Metal Brackets - Mini")

    product_page.select_option_value_by_name("MBT .018")
    product_page.select_option_value_by_name("Hooks On 3")
    product_page.select_option_value_by_name("Maxillary Right Canine (UR3)")
    product_page.click_add_to_cart_button()
    header.verify_working_cart_counter()

def test_search_popup(page, setup_base_test):
    """Test the search pop-up in the header"""

    _ = setup_base_test
    header = Header(page)

    header.input_data_search_field("12355")
    header.verify_search_popup("Articulating Paper 200 micron Strips Plastic Box Blue 300/Pk")

def test_check_login_logout(page, setup_base_test):
    """Test login and logout"""
    home_page = setup_base_test
    login_page = LoginPage(page)
    logout_page = LogoutPage(page)

    home_page.header.click_account_button()
    home_page.header.click_login_button()
    login_page.add_creds_and_login()
    home_page.check_title()
    home_page.header.click_account_button()
    home_page.header.click_logout_button()
    logout_page.check_title()


# ════════════════════════════════════════════════════════════════════════════
# ZONE-1: Top Bar — new tests
# Spec: TOP-001..019
# ════════════════════════════════════════════════════════════════════════════

def test_top001_customer_counter_visible(page, setup_base_test):
    """TOP-001: Customer counter block is visible on the page"""
    _ = setup_base_test
    header = Header(page)
    header.verify_customer_counter_visible()


def test_top002_customer_counter_has_five_digits(page, setup_base_test):
    """TOP-002: Counter renders exactly 5 digit spans"""
    _ = setup_base_test
    header = Header(page)
    assert header.get_counter_digit_count() == 5


def test_top003_shopping_plus_visible(page, setup_base_test):
    """TOP-003: Shopping+ link is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_shopping_plus_visible()


def test_top004_inventory_link_visible(page, setup_base_test):
    """TOP-004: Inventory Management link is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_inventory_link_visible()


def test_top005_payment_link_visible(page, setup_base_test):
    """TOP-005: Payment Slider link is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_payment_link_visible()


def test_top006_lab_tracker_link_visible(page, setup_base_test):
    """TOP-006: Lab Case Tracker link is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_lab_tracker_link_visible()


def test_top007_three_vip_badges_visible(page, setup_base_test):
    """TOP-007: Exactly 3 VIP badges are present"""
    _ = setup_base_test
    header = Header(page)
    assert header.get_vip_badge_count() == 3


def test_top008_shopping_plus_href_is_home(page, setup_base_test):
    """TOP-008: Shopping+ link href is '/'"""
    _ = setup_base_test
    header = Header(page)
    assert header.get_shopping_plus_href() == "/"


def test_top009_inventory_href_contains_drstorelist(page, setup_base_test):
    """TOP-009: Inventory link href contains 'drstorelist'"""
    _ = setup_base_test
    header = Header(page)
    assert "drstorelist" in header.get_inventory_href()


def test_top010_payment_href_contains_drslider(page, setup_base_test):
    """TOP-010: Payment link href contains 'drslider'"""
    _ = setup_base_test
    header = Header(page)
    assert "drslider" in header.get_payment_href()


def test_top011_lab_tracker_href_contains_account_lab(page, setup_base_test):
    """TOP-011: Lab Tracker link href contains 'account/lab'"""
    _ = setup_base_test
    header = Header(page)
    assert "account/lab" in header.get_lab_tracker_href()


def test_top012_account_button_visible(page, setup_base_test):
    """TOP-012: Account button is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_account_button_visible()


def test_top015_greeting_text_non_empty_when_logged_in(page, setup_logged_in_test):
    """TOP-015 (AUTH): Greeting text in account button is non-empty when logged in"""
    _ = setup_logged_in_test
    header = Header(page)
    greeting = header.get_account_greeting_text()
    assert len(greeting.strip()) > 0, f"Expected non-empty greeting, got: '{greeting}'"


def test_top016_my_account_link_visible_when_logged_in(page, setup_logged_in_test):
    """TOP-016 (AUTH): My Account link visible in dropdown after login"""
    _ = setup_logged_in_test
    header = Header(page)
    header.click_account_button_desktop()
    header.verify_account_dropdown_visible()
    header.verify_my_account_link_visible()


def test_top018_my_account_href_contains_account_account(page, setup_logged_in_test):
    """TOP-018 (AUTH): My Account link href contains 'account/account'"""
    _ = setup_logged_in_test
    header = Header(page)
    header.click_account_button_desktop()
    assert "account/account" in header.get_my_account_href()


def test_top019_logout_href_contains_account_logout(page, setup_logged_in_test):
    """TOP-019 (AUTH): Logout link href contains 'account/logout'"""
    _ = setup_logged_in_test
    header = Header(page)
    header.click_account_button_desktop()
    assert "account/logout" in header.get_logout_href()


# ════════════════════════════════════════════════════════════════════════════
# ZONE-2: Logo & Slogan — new tests
# Spec: LOGO-001..004
# ════════════════════════════════════════════════════════════════════════════

def test_logo001_slogan_visible(page, setup_base_test):
    """LOGO-001: Slogan 'Serving the Dental Professionals Since 2015' is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_slogan_visible()


def test_logo002_main_logo_visible(page, setup_base_test):
    """LOGO-002: Main logo image is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_main_logo_visible()


def test_logo003_aao_logo_visible(page, setup_base_test):
    """LOGO-003: AAO logo image is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_aao_logo_visible()


def test_logo004_main_logo_links_to_home(page, setup_base_test):
    """LOGO-004: Main logo link href is '/'"""
    _ = setup_base_test
    header = Header(page)
    assert header.get_main_logo_href() == "/"


# ════════════════════════════════════════════════════════════════════════════
# ZONE-3: Navigation & Phone — new tests
# Spec: NAV-001..007
# ════════════════════════════════════════════════════════════════════════════

def test_nav001_phone_link_visible(page, setup_base_test):
    """NAV-001: Phone link visible with correct number"""
    _ = setup_base_test
    header = Header(page)
    header.verify_phone_link_visible()


def test_nav002_to_nav006_nav_links_visible(page, setup_base_test):
    """NAV-002..006: Clearance, Brands, Dashboard, Your Orders, Buy again are visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_nav_links_visible()


def test_nav007_phone_href_is_tel_link(page, setup_base_test):
    """NAV-007: Phone href equals 'tel:800-833-7132'"""
    _ = setup_base_test
    header = Header(page)
    assert header.get_phone_href() == "tel:800-833-7132"


# ════════════════════════════════════════════════════════════════════════════
# ZONE-4: Search — new tests
# Spec: SRCH-001, SRCH-002, SRCH-005
# ════════════════════════════════════════════════════════════════════════════

def test_srch001_search_input_visible(page, setup_base_test):
    """SRCH-001: Desktop search input is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_search_input_visible()


def test_srch002_search_button_visible(page, setup_base_test):
    """SRCH-002: Desktop search button is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_search_button_visible()


def test_srch005_short_query_no_dropdown(page, setup_base_test):
    """SRCH-005: Typing < 3 chars does NOT trigger the autocomplete dropdown"""
    _ = setup_base_test
    header = Header(page)
    header.verify_short_query_no_dropdown("br")


# ════════════════════════════════════════════════════════════════════════════
# ZONE-5: Wishlist & Cart — new tests
# Spec: CART-001..005, CART-010..014
# ════════════════════════════════════════════════════════════════════════════

def test_cart001_wishlist_button_visible(page, setup_base_test):
    """CART-001: Wishlist button is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_wishlist_button_visible()


def test_cart002_wishlist_href_contains_wishlist(page, setup_base_test):
    """CART-002: Wishlist button href contains 'account/wishlist'"""
    _ = setup_base_test
    header = Header(page)
    assert "wishlist" in header.get_wishlist_href()


def test_cart003_cart_button_visible(page, setup_base_test):
    """CART-003: Cart button is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_cart_button_visible()


def test_cart004_cart_count_badge_visible(page, setup_base_test):
    """CART-004: Cart count badge is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_cart_count_badge_visible()


def test_cart005_cart_modal_hidden_before_click(page, setup_base_test):
    """CART-005: Cart modal is hidden before the cart button is clicked"""
    _ = setup_base_test
    header = Header(page)
    assert not header.cart_modal_is_visible(), (
        "Cart modal should be hidden on page load before any interaction"
    )


def test_cart010_cart_modal_shows_subtotal(page, setup_cart_with_product):
    """CART-010: Cart modal shows Sub-Total row"""
    _ = setup_cart_with_product
    header = Header(page)
    header.open_cart_modal()
    keys = header.get_cart_total_row_keys()
    assert any("Sub-Total" in k for k in keys), (
        f"Sub-Total row not found in cart modal. Rows: {keys}"
    )


def test_cart011_cart_modal_shows_total(page, setup_cart_with_product):
    """CART-011: Cart modal shows Total row"""
    _ = setup_cart_with_product
    header = Header(page)
    header.open_cart_modal()
    keys = header.get_cart_total_row_keys()
    assert any(k.strip() == "Total" for k in keys), (
        f"Total row not found in cart modal. Rows: {keys}"
    )


def test_cart012_view_cart_href(page, setup_cart_with_product):
    """CART-012: View Cart button href contains 'checkout/cart'"""
    _ = setup_cart_with_product
    header = Header(page)
    header.open_cart_modal()
    assert "checkout/cart" in header.get_view_cart_href()


def test_cart013_checkout_button_href(page, setup_cart_with_product):
    """CART-013: Checkout button href contains 'check-out'"""
    _ = setup_cart_with_product
    header = Header(page)
    header.open_cart_modal()
    assert "check-out" in header.get_checkout_modal_href()


def test_cart014_close_button_hides_modal(page, setup_cart_with_product):
    """CART-014: Clicking Close button hides the cart modal"""
    _ = setup_cart_with_product
    header = Header(page)
    header.open_cart_modal()
    assert header.cart_modal_is_visible(), "Modal should be open before testing close"
    header.close_cart_modal()
    assert not header.cart_modal_is_visible(), "Cart modal should be hidden after Close click"


# ════════════════════════════════════════════════════════════════════════════
# ZONE-6: Category Pills — new tests
# Spec: CAT-001..005
# ════════════════════════════════════════════════════════════════════════════

def test_cat001_to_cat003_all_pills_visible(page, setup_base_test):
    """CAT-001..003: Dental, Surgery, Orthodontic category pills are all visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_category_pills_visible()


def test_cat004_dental_pill_href(page, setup_base_test):
    """CAT-004: Dental pill href contains 'general-dentistry'"""
    _ = setup_base_test
    header = Header(page)
    assert "general-dentistry" in header.get_dental_pill_href()


def test_cat005_surgery_pill_href(page, setup_base_test):
    """CAT-005: Surgery pill href contains 'surgical-and-implant'"""
    _ = setup_base_test
    header = Header(page)
    assert "surgical-and-implant" in header.get_surgery_pill_href()
