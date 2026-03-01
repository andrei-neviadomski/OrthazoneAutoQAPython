"""Component checkout popup"""
from playwright.sync_api import expect
from pages.base_page import BasePage

class CheckoutPopUp(BasePage):
    """Component checkout popup"""

    def verify_adding_product_by_name(self, name: str):
        """Verify adding products by name"""
        product_title = self.page.locator(".line-clamp-2").first
        expect(product_title).to_have_text(f"{name}", timeout=20000)

    def remove_product_from_popup(self):
        """remove a first product from popup"""
        remove_button = self.page.locator("button.y-basket-card__remove").first
        remove_button.wait_for(state="visible", timeout=20000)
        remove_button.click()

    def verify_product_removed_from_popup(self):
        """Verify that products was removed from the popup"""
        empty_message = self.page.locator(
            ".y-modal__header").get_by_text("YOUR SHOPPING CART IS EMPTY!").filter(visible=True
            )
        expect(empty_message).to_be_visible(timeout=20000)

    def click_checkout_button(self):
        """click checkout button"""
        checkout_button = self.page.locator(
            "a.y-modal__cart-btn:has-text('Checkout')"
            ).first
        checkout_button.wait_for(state="visible", timeout=20000)
        checkout_button.click()
