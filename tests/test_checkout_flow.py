"""Test sutes for orthazone checkout."""

import os
from components.header import Header
from components.checkout_popup import CheckoutPopUp
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from pages.checkout_success_page import CheckoutSuccessPage

def test_checkout_flow(page):
    """Test of the checkout."""
    home_page = HomePage(page)
    category_page = CategoryPage(page)
    product_page = ProductPage(page)
    header = Header(page)
    checkout_pop_up = CheckoutPopUp(page)
    login_page = LoginPage(page)
    checkout_page = CheckoutPage (page)
    checkout_success_page = CheckoutSuccessPage(page)

    base_url = os.getenv("BASE_URL", "https://orthazone.com")

    home_page.open(base_url)
    home_page.check_title()
    home_page.set_stripe_cookie()

    home_page.header.click_account_button()
    home_page.header.click_login_button()

    login_page.add_creds_and_login()
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
    checkout_pop_up.click_checkout_button()
    checkout_page.check_url()

    checkout_page.click_continue_button_delivery_method_step()
    checkout_page.click_continue_button_shipping_adress_step()
    checkout_page.click_continue_button_coupon_voucher_step()
    checkout_page.fill_cc_data()
    checkout_page.click_continue_button_payment_info_step()
    checkout_page.sign_cc_payment()
    checkout_page.click_submit_button_signature_step()
    checkout_success_page.verify_checkout_success_page()
