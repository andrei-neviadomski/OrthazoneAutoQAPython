"""Login and Logout test sutes"""
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

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
