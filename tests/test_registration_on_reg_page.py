"""Test Suite for registartion on the registration page"""
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage

def test_reg_on_reg_page(page, setup_order_test: HomePage):
    """Test for registartion on the registration page"""
    home_page = setup_order_test
    registration_page = RegistrationPage(page)

    home_page.header.click_account_button()
    home_page.header.click_register_button()
    registration_page.verify_reg_page_title()
