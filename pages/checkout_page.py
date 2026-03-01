"""Checkout page"""
import re
from playwright.sync_api import expect
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Checkout page"""

    def check_url(self):
        """Сheck checkout page title"""
        expect(self.page).to_have_url(re.compile('check-out'))

    def click_continue_button_delivery_method_step(self):
        """click continue button on the delivery method step"""
        checkout_button = self.page.locator(
            "#button-shipping-method"
            ).first
        checkout_button.wait_for(state="visible", timeout=20000)
        checkout_button.click()

    def click_continue_button_shipping_adress_step(self):
        """click continue button on the shipping adress step"""
        checkout_button = self.page.locator(
            "#button-shipping-address"
            ).first
        checkout_button.wait_for(state="visible", timeout=20000)
        checkout_button.click()

    def click_continue_button_coupon_voucher_step(self):
        """click continue button on the shipCoupon/voucher step"""
        checkout_button = self.page.locator(
            "#button-coupon-voucher"
            ).first
        checkout_button.wait_for(state="visible", timeout=20000)
        checkout_button.click()

    def fill_cc_data(self):
        """Add cc data to the CC Number, Card expired, CVC fields"""
        card_frame = self.page.frame_locator('iframe[title="Secure card number input frame"]')
        card_frame.locator('input[name="cardnumber"]').fill("4242424242424242")
        expdate_frame = self.page.frame_locator(
            'iframe[title="Secure expiration date input frame"]'
            )
        expdate_frame.locator('input[name="exp-date"]').fill("0133")
        cvc_frame = self.page.frame_locator('iframe[title="Secure CVC input frame"]')
        cvc_frame.locator('input[name="cvc"]').fill("111")

    def click_continue_button_payment_info_step(self):
        """click continue button on the Payment info step"""
        checkout_button = self.page.locator(
            "#button-confirm"
            ).first
        checkout_button.wait_for(state="visible", timeout=20000)
        checkout_button.click()

    def sign_cc_payment(self):
        """Sign in the sign fields"""
        canvas = self.page.locator("canvas.jSignature")
        canvas.scroll_into_view_if_needed()
        box = canvas.bounding_box()
        if box:
            start_x = box['x'] + box['width'] / 4
            start_y = box['y'] + box['height'] / 2
            self.page.mouse.move(start_x, start_y)
            self.page.mouse.down()

        self.page.mouse.move(start_x + 50, start_y + 20, steps=10)
        self.page.mouse.move(start_x + 100, start_y - 20, steps=10)

        self.page.mouse.up()

    def click_submit_button_signature_step(self):
        """click Submit order button on the Signature step"""
        checkout_button = self.page.locator(
            "#button-submit-order"
            ).first
        checkout_button.wait_for(state="visible", timeout=20000)
        checkout_button.click()
