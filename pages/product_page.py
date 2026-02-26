from pages.base_page import BasePage
from playwright.sync_api import expect

class ProductPage(BasePage):

    def select_option_value_by_name(self,name: str):
        self.click(f"label:has-text('{name}')")

    #def click_add_to_cart_button(self):
        #self.click("a:has-text('Add to Cart')")
        #cart_counter = self.page.locator(".int-cart-text-indicator").filter(visible=True).first
        #expect(cart_counter).not_to_have_text("0", timeout=15000)

    def click_add_to_cart_button(self):
        with self.page.expect_response(
            lambda r: "checkout/cart/add" in r.url and r.status == 200
        ) as response_info:
            self.click("a:has-text('Add to Cart')")
        
        body = response_info.value.json()
        assert "success" in body, f"Add to Cart failed. Server response: {body}"