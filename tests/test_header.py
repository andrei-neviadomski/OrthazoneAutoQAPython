"""Test Suite for Header"""
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from components.header import Header

# ════════════════════════════════════════════════════════════════════════════
# Existing tests (DO NOT change)
# ════════════════════════════════════════════════════════════════════════════








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

def test_top012_two_free_badges_visible(page, setup_base_test):
    """TOP-012: Exactly 2 Free badges are present"""
    _ = setup_base_test
    header = Header(page)
    assert header.get_free_badge_count() == 2

def test_top013_dashboard_link_visible(page, setup_base_test):
    """TOP-013: Dashboard link is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_dashboard_link_visible()

def test_top014_phone_link_visible(page, setup_base_test):
    """TOP-014: Phone link visible with correct number"""
    _ = setup_base_test
    header = Header(page)
    header.verify_phone_link_visible()

def test_top015_phone_href_is_tel_link(page, setup_base_test):
    """TOP-015: Phone href equals 'tel:800-833-7132'"""
    _ = setup_base_test
    header = Header(page)
    assert header.get_phone_href() == "tel:800-833-7132"

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
# ZONE-3: Navigation & Search
# ════════════════════════════════════════════════════════════════════════════

def test_nav001_nav_links_visible(page, setup_base_test):
    """NAV-001: Clearance, Brands, Dental, Surgery, Orthodontic are visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_nav_links_visible()

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


def test_search_popup(page, setup_base_test):
    """Test the search pop-up in the header"""

    _ = setup_base_test
    header = Header(page)

    header.input_data_search_field("12355")
    header.verify_search_popup("Articulating Paper 200 micron Strips Plastic Box Blue 300/Pk")


# ════════════════════════════════════════════════════════════════════════════
# ZONE-4: Wishlist & Cart
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
    assert "index.php?route=account/wishlist" in header.get_wishlist_href()


def test_cart003_account_button_visible(page, setup_base_test):
    """CART-003: Account button is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_account_button_visible()

def test_cart004_greeting_text_non_empty_when_logged_in(page, setup_logged_in_test):
    """CART-004 (AUTH): Greeting text in account button is non-empty when logged in"""
    _ = setup_logged_in_test
    header = Header(page)
    greeting = header.get_account_greeting_text()
    assert len(greeting.strip()) > 0, f"Expected non-empty greeting, got: '{greeting}'"

def test_cart005_my_account_link_visible_when_logged_in(page, setup_logged_in_test):
    """CART-005 (AUTH): My Account links visible in dropdown after login (
    My Account, Your Orders, Bay again, Logout)"""
    _ = setup_logged_in_test
    header = Header(page)
    header.click_account_button_desktop()
    header.verify_account_dropdown_visible()
    header.verify_my_account_link_visible()
    header.verify_orders_link_visible()
    header.verify_buy_again_link_visible()
    header.verify_logout_link_visible()

def test_cart006_my_account_href_contains_account_account(page, setup_logged_in_test):
    """CART-006 (AUTH): My Account links href have needed urls (
    My Account, Your Orders, Bay again, Logout)"""
    _ = setup_logged_in_test
    header = Header(page)
    header.click_account_button_desktop()
    assert "account/account" in header.get_my_account_href()
    assert "allorders" in header.get_orders_href()
    assert "quickreorder" in header.get_buy_again_href()
    assert "account/logout" in header.get_logout_href()


def test_cart006_cart_button_visible(page, setup_base_test):
    """CART-006: Cart button is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_cart_button_visible()


def test_cart007_cart_count_badge_visible(page, setup_base_test):
    """CART-007: Cart count badge is visible"""
    _ = setup_base_test
    header = Header(page)
    header.verify_cart_count_badge_visible()


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


def test_check_login_logout(page, setup_base_test):
    """Test login and logout"""
    home_page = setup_base_test
    login_page = LoginPage(page)
    logout_page = LogoutPage(page)

    home_page.header.click_account_button_desktop()
    home_page.header.click_login_button()
    login_page.add_creds_and_login()
    home_page.check_title()
    home_page.header.click_account_button_desktop()
    home_page.header.click_logout_button()
    logout_page.check_title()
