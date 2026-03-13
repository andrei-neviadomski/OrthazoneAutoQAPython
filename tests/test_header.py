"""Test Suite for Header"""
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from components.header import Header

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
