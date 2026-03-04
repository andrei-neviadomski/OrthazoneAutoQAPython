"""Component Header for all pages"""

from pages.base_page import BasePage


class Header(BasePage):
    """Component Header for all pages"""

    CART_BUTTON = 'button.int-cart-button.is_cart'
    ACCOUNT_BUTTON = 'span:has-text("Account")'
    LOGIN_BUTTON = 'span:has-text("Login")'
    LOGOUT_BUTTON = 'span:has-text("Logout")'
    REGISTER_BUTTON = 'span:has-text("Register")'

    def click_cart_popup_button(self):
        """Click the cart popup batton in the header"""
        self.click(self.CART_BUTTON)
        assert self.get_text("div.y-modal__title") == "SHOPPING CART"

    def click_account_button(self):
        """Click the account button in the header"""
        self.click(self.ACCOUNT_BUTTON)

    def click_login_button(self):
        """Click the login button in the header"""
        self.click(self.LOGIN_BUTTON)

    def click_logout_button(self):
        """Click the logout button in the header"""
        self.click(self.LOGOUT_BUTTON)

    def click_register_button(self):
        """Click the Register button in the header"""
        self.click(self.REGISTER_BUTTON)
