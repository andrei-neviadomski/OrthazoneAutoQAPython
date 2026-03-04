"""Registration page"""
from playwright.sync_api import expect
from .base_page import BasePage


class RegistrationPage(BasePage):
    """Registration page"""

    EXPECTED_TITLE = "Create Account"

    def verify_reg_page_title(self):
        """Check and verify title"""
        expect(self.page).to_have_title(self.EXPECTED_TITLE)
