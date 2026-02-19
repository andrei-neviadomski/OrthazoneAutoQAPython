from .base_page import BasePage
from playwright.sync_api import expect

class LogoutPage(BasePage):

    EXPECTED_TITLE = "Account Logout"

    def check_title(self):
        # Используем встроенный expect от Playwright для проверки
        expect(self.page).to_have_title(self.EXPECTED_TITLE)