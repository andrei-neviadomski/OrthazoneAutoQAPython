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


    registration_page.fill_email()
    registration_page.fill_phone()
    registration_page.fill_password()
    registration_page.fill_confirm_password()
    registration_page.check_business_account()
    registration_page.click_next_batton()

    registration_page.verify_business_acount()
    registration_page.fill_first_name()
    registration_page.fill_last_name()
    registration_page.click_next_batton()

    registration_page.verify_register_acount_step()
    registration_page.check_agree_checkbox()
    registration_page.click_register_batton()
    registration_page.verify_registation()


    registration_page.take_screenshot()
