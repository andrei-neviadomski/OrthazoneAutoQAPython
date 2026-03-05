"""Test Suite for Header"""
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
