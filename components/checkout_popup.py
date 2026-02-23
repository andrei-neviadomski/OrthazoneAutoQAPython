from pages.base_page import BasePage
from playwright.sync_api import expect

class CheckoutPopUp(BasePage):
    
    def verify_adding_product_by_name(self):
        assert self.get_text(".line-clamp-2") == "Metal Brackets - Mini Size"

    def remove_product_from_popup(self):
        remove_button = self.page.locator("button.y-basket-card__remove").first
        remove_button.click()

    def verify_product_removed_from_popup(self):
        cart_items = self.page.locator(".y-modal__inner .line-clamp-2")
        expect(cart_items).to_have_count(0)   
