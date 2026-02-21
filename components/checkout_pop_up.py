from pages.base_page import BasePage
from playwright.sync_api import expect

class CheckoutPopUp(BasePage):
    
    def verify_adding_product_by_name(self):
        assert self.get_text(".line-clamp-2") == "Metal Brackets - Mini Size"