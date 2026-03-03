import re
from pages.base_page import BasePage
from playwright.sync_api import expect

class ProductPage(BasePage):

    def select_option_value_by_name(self,name: str):
        self.click(f"label:has-text('{name}')")

    def click_add_to_cart_button(self):
        self.click("a:has-text('Add to Cart')")
        self.page.evaluate("window.scrollTo(0, 0)")
        desktop = self.page.locator(
        ".int-header-wrap button.int-cart-button .int-cart-text-indicator"
        )
        mobile = self.page.locator(
        ".y-header-mobile button.int-cart-button .int-cart-text-indicator"
        )
        cart_counter = desktop if desktop.first.is_visible() else mobile
        expect(cart_counter.first).to_have_attribute(
        "data-quantity",
        re.compile(r"Cart:\s*1\s*items"),
        timeout=15000
        )
        expect(cart_counter.first).to_have_text("1", timeout=15000)
