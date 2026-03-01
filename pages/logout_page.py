"""Logout page"""
from playwright.sync_api import expect
from .base_page import BasePage


class LogoutPage(BasePage):
    """Logout page"""
    EXPECTED_TITLE = "Account Logout"

    def check_title(self):
        """Verify the title of the logout page"""
        expect(self.page).to_have_title(self.EXPECTED_TITLE)
