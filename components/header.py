"""Component Header"""

from playwright.sync_api import expect
from pages.base_page import BasePage


class Header(BasePage):
    """Methodos for Header"""

    CART_BUTTON = 'button.int-cart-button.is_cart'
    ACCOUNT_BUTTON = 'span:has-text("Account")'
    LOGIN_BUTTON = 'span:has-text("Login")'
    LOGOUT_BUTTON = 'span:has-text("Logout")'

    def open_cart_popup(self):
        """Open the cart popup"""
        self.click(self.CART_BUTTON)
        assert self.get_text("div.y-modal__title") == "SHOPPING CART"

    def click_account_button(self):
        """Click the account button"""
        self.click(self.ACCOUNT_BUTTON)

    def click_login_button(self):
        """Click the Login button"""
        self.click(self.LOGIN_BUTTON)

    def click_logout_button(self):
        """Click the logout button"""
        self.click(self.LOGOUT_BUTTON)

    def verify_working_cart_counter(self):
        """Verify that the cart counter isn't 0"""
        cart_counter = self.page.locator(".int-cart-text-indicator").filter(visible=True).first
        cart_counter.wait_for(state="visible", timeout=15000)
        expect(cart_counter).not_to_have_text("0", timeout=15000)
