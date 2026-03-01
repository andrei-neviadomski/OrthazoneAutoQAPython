"""Checkout Success page"""
from playwright.sync_api import expect
from .base_page import BasePage


class CheckoutSuccessPage(BasePage):
    """Checkout Success page"""

    def verify_checkout_success_page(self):
        """Verify that system processed an order"""
        success_message = self.page.locator(".asteps__head")
        expect(success_message).to_have_text("Your Order Has Been Processed!", timeout=20000)
