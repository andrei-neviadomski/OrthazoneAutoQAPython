"""Base page for storefront"""
from datetime import datetime
import os
from playwright.sync_api import Page

class BasePage:
    """Base page class for storefront"""

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        """Open"""
        self.page.goto(url, wait_until="domcontentloaded", timeout=60000)

    def click(self, selector: str):
        """Click"""
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        """Fill a field"""
        self.page.fill(selector, text)

    def get_text(self, selector: str):
        """Get a text"""
        return self.page.inner_text(selector)

    def take_screenshot(self, name: str = "screenshot"):
        """Screenshot"""
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        self.page.wait_for_timeout(1000)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = f"screenshots/{name}_{timestamp}.png"
        self.page.screenshot(path=file_path, full_page=True)
        return file_path
