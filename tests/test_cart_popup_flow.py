"""Test Suite for the checkout flow"""
import os
from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from components.header import Header
from components.checkout_popup import CheckoutPopUp


def test_add_product_to_cart_popup(page):
    """Test checks addin a product to the cart"""

    home_page = HomePage(page)
    category_page = CategoryPage(page)
    product_page = ProductPage(page)
    header = Header(page)
    checkout_pop_up = CheckoutPopUp(page)

    base_url = os.getenv("BASE_URL", "https://orthazone.com")

    home_page.open(base_url)
    home_page.check_title()

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

    header.open_cart_popup()
    checkout_pop_up.verify_adding_product_by_name("Metal Brackets - Mini Size")

def test_remove_product_from_cart_popup(page):
    """Test checks removingn a product from the cart"""

    home_page = HomePage(page)
    category_page = CategoryPage(page)
    product_page = ProductPage(page)
    header = Header(page)
    checkout_pop_up = CheckoutPopUp(page)

    base_url = os.getenv("BASE_URL", "https://orthazone.com")

    home_page.open(base_url)
    home_page.check_title()

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

    header.open_cart_popup()
    checkout_pop_up.verify_adding_product_by_name("Metal Brackets - Mini Size")
    checkout_pop_up.remove_product_from_popup()
    checkout_pop_up.verify_product_removed_from_popup()
