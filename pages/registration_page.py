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
        self.fill('input[name="email"]', os.getenv("ADMIN_NEW_EMAIL"))

    def fill_phone(self):
        """fill phone"""
        self.fill('input[name="telephone"]', "5656565656")

    def fill_password(self):
        """fill password"""
        self.fill('input[name="password"]', os.getenv("ADMIN_TEST_PASWORD"))

    def fill_confirm_password(self):
        """fill confirm password"""
        self.fill('input[name="confirm"]', os.getenv("ADMIN_TEST_PASWORD"))

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
