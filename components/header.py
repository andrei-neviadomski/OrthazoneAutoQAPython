from pages.base_page import BasePage
from playwright.sync_api import expect

class Header(BasePage):

    CART_BUTTON = 'button.int-cart-button.is_cart'
    ACCOUNT_BUTTON = 'span:has-text("Account")'
    LOGIN_BUTTON = 'span:has-text("Login")'
    LOGOUT_BUTTON = 'span:has-text("Logout")'

    def open_cart_popup(self):
        self.click(self.CART_BUTTON)
        assert self.get_text("div.y-modal__title") == "SHOPPING CART"

    def click_account_button(self):
        self.click(self.ACCOUNT_BUTTON)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def click_logout_button(self):
        self.click(self.LOGOUT_BUTTON)   