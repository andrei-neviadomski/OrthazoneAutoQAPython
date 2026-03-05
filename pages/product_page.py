""""Product Page"""
from pages.base_page import BasePage

class ProductPage(BasePage):
    """Product Page"""

    def select_option_value_by_name(self,name: str):
        """Select an option value by name"""
        self.click(f"label:has-text('{name}')")

    def click_add_to_cart_button(self):
        """Click the Add to Cart Button and verify that a product was added"""
        self.click("a:has-text('Add to Cart')")
