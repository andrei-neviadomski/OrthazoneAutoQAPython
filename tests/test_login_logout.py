"""Login and Logout test sutes"""
#import pytest
#from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

#@pytest.mark.usefixtures("setup_base_test")
def test_check_login_logout(page, setup_base_test):
    """Test login and logout"""
    home_page = setup_base_test
    login_page = LoginPage(page)
    logout_page = LogoutPage(page)
    #base_url = os.getenv("BASE_URL", "https://orthazone.com")
    #home_page.open(base_url)

    home_page.header.click_account_button()
    home_page.header.click_login_button()
    login_page.add_creds_and_login()
    home_page.check_title()
    home_page.header.click_account_button()
    home_page.header.click_logout_button()
    logout_page.check_title()
