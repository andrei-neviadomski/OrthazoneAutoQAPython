"""Login button"""
from .base_page import BasePage


class LoginPage(BasePage):
    """Login"""
    EMAIL_INPUT = 'input[name="email"]'
    PASSWORD_INPUT = 'input[name="password"]'
    LOGIN_SUBMIT_BUTTON = 'button:has-text("Login")'

    def add_creds_and_login(self):
        """add creds and login"""
        self.fill(self.EMAIL_INPUT, "autotest-old@orthazone.com")
        self.fill(self.PASSWORD_INPUT, "123456789")
        self.click(self.LOGIN_SUBMIT_BUTTON)
