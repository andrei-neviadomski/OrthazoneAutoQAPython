from pages.base_page import BasePage
from playwright.sync_api import expect

class CheckoutPopUp(BasePage):
    
    def verify_adding_product_by_name(self):
        assert self.get_text(".line-clamp-2") == "Metal Brackets - Mini Size"

    def remove_product_from_popup(self):
        remove_button = self.page.locator("button.y-basket-card__remove").first
        #expect(remove_button).to_be_visible()
        remove_button.click()

    def verify_product_removed_from_popup(self):
        expect(self.page.locator(".line-clamp-2")).to_have_count(0)
