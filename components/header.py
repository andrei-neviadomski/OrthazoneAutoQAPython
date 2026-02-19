from pages.base_page import BasePage
from playwright.sync_api import expect

class Header(BasePage):

    CART_BUTTON = 'button.int-cart-button.is_cart'

    def open_cart_popup(self):
        self.click(self.CART_BUTTON)
        assert self.get_text("div.y-modal__title") == "SHOPPING CART"