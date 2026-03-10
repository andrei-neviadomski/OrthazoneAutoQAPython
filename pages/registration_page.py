"""Registration page"""
import os
from playwright.sync_api import expect
from .base_page import BasePage


class RegistrationPage(BasePage):
    """Registration page"""

    EXPECTED_TITLE = "Create Account"

    def verify_reg_page_title(self):
        """Check and verify title"""
        expect(self.page).to_have_title(self.EXPECTED_TITLE)

    def fill_email(self):
        """fill email"""
        value = os.getenv("ADMIN_NEW_EMAIL")
        locator = self.page.locator('input[name="email"]')
        locator.click()
        locator.press_sequentially(value, delay=50)

    def fill_phone(self):
        """fill phone"""
        value = "5656565656"
        locator = self.page.locator('input[name="telephone"]')
        locator.click()
        locator.press_sequentially(value, delay=50)

    def fill_password(self):
        """fill password"""
        value = os.getenv("ADMIN_TEST_PASSWORD")
        locator = self.page.locator('input[name="password"]')
        locator.click()
        locator.press_sequentially(value, delay=50)

    def fill_confirm_password(self):
        """fill confirm password"""
        value = os.getenv("ADMIN_TEST_PASSWORD")
        locator = self.page.locator('input[name="confirm"]')
        locator.click()
        locator.press_sequentially(value, delay=50)

    def check_business_account(self):
        """check business account type"""
        self.page.wait_for_timeout(1000)
        self.page.evaluate("""
            () => {
                var radio = document.getElementById('registration_type_id_2');
                radio.checked = true;
                jQuery(radio).trigger('change');
                jQuery('[data-block-acc]').hide();
                jQuery('[data-block-acc="registration_block_2"]').css('display', 'inline-block');
            }
        """)

    def click_next_batton(self):
        """Click next button"""
        self.page.locator('button[data-step-btn="next"]').click()
        self.page.wait_for_timeout(2000)

    def verify_business_acount(self):
        """verify business account"""
        locator = self.page.locator('input[name="company_name"]')
        expect(locator).to_be_visible(timeout=20000)

    def fill_first_name(self):
        """fill first name field"""
        value = "Auto test new"
        locator = self.page.locator('input[name="firstname"]').filter(visible=True)
        locator.click()
        locator.press_sequentially(value, delay=50)

    def fill_last_name(self):
        """fill last name field"""
        value = "Auto test new"
        locator = self.page.locator('input[name="lastname"]').filter(visible=True)
        locator.click()
        locator.press_sequentially(value, delay=50)

    def verify_register_acount_step(self):
        """verify register acount_step"""
        locator = self.page.locator('.aform__head').filter(visible=True)
        expect(locator).to_have_text("Register Account")

    def check_agree_checkbox(self):
        """Check "I have read and agree to the Privacy Policy" checkbox"""
        self.page.locator('label[for="agree"]').click()

    def click_register_batton(self):
        """Click register button"""
        self.page.locator('button[data-step-btn="send"]').click()
        self.page.wait_for_timeout(2000)

    def verify_registation(self):
        """verify finishing regitration"""
        locator = self.page.locator('.asteps__head').filter(visible=True)
        expect(locator).to_have_text("Your Account Has Been Created!")
