"""Login button"""
import os
from dotenv import load_dotenv
from .base_page import BasePage
load_dotenv()


class LoginPage(BasePage):
    """Login"""
    EMAIL_INPUT = 'input[name="email"]'
    PASSWORD_INPUT = 'input[name="password"]'
    LOGIN_SUBMIT_BUTTON = 'button:has-text("Login")'

    def add_creds_and_login(self):
        """add creds and login"""
        self.fill(self.EMAIL_INPUT, os.getenv("ADMIN_TEST_EMAIL"))
        self.fill(self.PASSWORD_INPUT, os.getenv("ADMIN_TEST_PASWORD"))
        self.click(self.LOGIN_SUBMIT_BUTTON)
