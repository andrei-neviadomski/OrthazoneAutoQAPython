from pages.base_page import BasePage

class ProductPage(BasePage):

    def check_option_value_by_name(self,name: str):
        self.click(f"label:has-text('{name}')")

    def click_add_to_cart_button(self):
        self.click("a:has-text('Add to Cart')")