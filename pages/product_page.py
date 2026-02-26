from pages.base_page import BasePage
from playwright.sync_api import expect

class ProductPage(BasePage):

    def select_option_value_by_name(self,name: str):
        self.click(f"label:has-text('{name}')")

    def click_add_to_cart_button(self):
        self.click("a:has-text('Add to Cart')")
        cart_counter = self.page.locator(".int-cart-text-indicator").filter(visible=True).first
        expect(cart_counter).not_to_have_text("0", timeout=15000)