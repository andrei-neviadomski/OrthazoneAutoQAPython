"""Component Header"""

from playwright.sync_api import expect
from pages.base_page import BasePage


class Header(BasePage):
    """Component Header for all pages"""

      # ── ZONE-1: Top Bar ─────────────────────────────────────────────────────
    CUSTOMER_COUNTER = '.int-header-top-counter'
    COUNTER_DIGIT_SPANS = '.int-header-top-counter span'
    SHOPPING_PLUS_LINK = 'a.int-header-top-right-link.is_current'
    INVENTORY_LINK = 'a.int-header-top-right-link[href*="drstorelist"]'
    DASHBOARD_LINK = '.int-header-top-right a[href*="sampledashboard"]'
    PAYMENT_LINK = 'a.int-header-top-right-link[href*="drslider"]'
    LAB_TRACKER_LINK = 'a.int-header-top-right-link[href*="account/lab"]'
    VIP_BADGES = 'a.int-header-top-right-link:not(.is_current) .int-header-top-badge:text("VIP")'
    FREE_BADGES = 'a.int-header-top-right-link .int-header-top-badge:text("Free")'
    ACCOUNT_MODAL_DESKTOP = '.int-header-top-right-account .y-modal.is_user'
    ACCOUNT_BUTTON_DESKTOP = 'button.int-account-button'
    MY_ACCOUNT_LINK = '.int-header-top-right-account a[href*="account/account"]'
    LOGOUT_LINK_DESKTOP = '.int-header-top-right-account a[href*="account/logout"]'
    ACCOUNT_GREETING = '.int-account-button-text span:first-child'
    PHONE_LINK = 'a.int-header-center-top-call[href="tel:800-833-7132"]'

    # ── ZONE-2: Logo & Slogan ───────────────────────────────────────────────
    SLOGAN = 'p.int-header-left-serving'
    MAIN_LOGO_LINK = '.int-header-left a[href="/"]'
    MAIN_LOGO_IMG = '.int-header-left img[alt="logo"]'
    AAO_LOGO_IMG = '.int-header-left img[alt="aao"]'
    SLOGAN_TEXT = "Serving the Dental Professionals Since 2015"

    # ── ZONE-3: Navigation & Search ──────────────────────────────────────────

    CLEARANCE_LINK = '.int-header-center-top a[href*="clearance"]'
    BRANDS_LINK = '.int-header-center-top a[href*="/brands"]'
    DENTAL_LINK = 'a.int-header-categories-pill[href*="general-dentistry"]'
    SURGERY_LINK = 'a.int-header-categories-pill[href*="surgical"]'
    ORTHODONTIC_LINK = 'a.int-header-categories-pill:nth-of-type(3)'
    SEARCH_INPUT = 'input.y-search__inp.int-header-search-input'
    SEARCH_BUTTON = 'button.int-header-search-button'

    # ── ZONE-4: Wishlist & Cart ─────────────────────────────────────────────
    WISHLIST_BUTTON = 'a.int-wishlist-button'
    WISHLIST_COUNT = '.int-wishlist-button-indicator'
    ORDERS_LINK = '.int-header-right .y-modal.is_user a[href*="allorders"]'
    BUY_AGAIN_LINK = '.int-header-right .y-modal.is_user a[href*="quickreorder"]'
    CART_BUTTON = 'button.int-cart-button.is_cart'
    LOGIN_BUTTON = 'span:has-text("Login")'
    LOGOUT_BUTTON = 'span:has-text("Logout")'
    REGISTER_BUTTON = 'span:has-text("Register")'


    # ════════════════════════════════════════════════════════════════════════
    # ZONE-1: Top Bar — new methods
    # ════════════════════════════════════════════════════════════════════════

    def verify_customer_counter_visible(self):
        """ZONE-1: Verify customer counter block is visible"""
        expect(self.page.locator(self.CUSTOMER_COUNTER)).to_be_visible(timeout=10000)

    def get_counter_digit_count(self) -> int:
        """ZONE-1: Return number of digit spans inside customer counter (expect 5)"""
        return self.page.locator(self.COUNTER_DIGIT_SPANS).count()

    def verify_shopping_plus_visible(self):
        """ZONE-1: Verify Shopping+ link is visible"""
        expect(self.page.locator(self.SHOPPING_PLUS_LINK)).to_be_visible(timeout=10000)

    def verify_inventory_link_visible(self):
        """ZONE-1: Verify Inventory Management link is visible"""
        expect(self.page.locator(self.INVENTORY_LINK)).to_be_visible(timeout=10000)

    def verify_dashboard_link_visible(self):
        """ZONE-1: Verify Dashboard link is visible"""
        expect(self.page.locator(self.DASHBOARD_LINK)).to_be_visible(timeout=10000)

    def verify_payment_link_visible(self):
        """ZONE-1: Verify Payment Slider link is visible"""
        expect(self.page.locator(self.PAYMENT_LINK)).to_be_visible(timeout=10000)

    def verify_lab_tracker_link_visible(self):
        """ZONE-1: Verify Lab Case Tracker link is visible"""
        expect(self.page.locator(self.LAB_TRACKER_LINK)).to_be_visible(timeout=10000)

    def get_vip_badge_count(self) -> int:
        """ZONE-1: Return count of VIP badges (expect 3)"""
        return self.page.locator(self.VIP_BADGES).count()

    def get_free_badge_count(self) -> int:
        """ZONE-1: Return count of Free badges (expect 2)"""
        return self.page.locator(self.FREE_BADGES).count()

    def get_shopping_plus_href(self) -> str:
        """ZONE-1: Return Shopping+ link href"""
        return self.page.locator(self.SHOPPING_PLUS_LINK).get_attribute("href") or ""

    def get_inventory_href(self) -> str:
        """ZONE-1: Return Inventory link href"""
        return self.page.locator(self.INVENTORY_LINK).get_attribute("href") or ""

    def get_payment_href(self) -> str:
        """ZONE-1: Return Payment link href"""
        return self.page.locator(self.PAYMENT_LINK).get_attribute("href") or ""

    def get_lab_tracker_href(self) -> str:
        """ZONE-1: Return Lab Tracker link href"""
        return self.page.locator(self.LAB_TRACKER_LINK).get_attribute("href") or ""


    def verify_logout_link_visible(self):
        """ZONE-1 (AUTH): Verify Logout link is visible in dropdown"""
        expect(self.page.locator(self.LOGOUT_LINK_DESKTOP)).to_be_visible(timeout=10000)

    def verify_phone_link_visible(self):
        """ZONE-1: Verify phone link is visible and contains expected number"""
        phone = self.page.locator(self.PHONE_LINK)
        expect(phone).to_be_visible(timeout=10000)
        expect(phone).to_contain_text("(800) 833-7132", timeout=10000)

    def get_phone_href(self) -> str:
        """ZONE-1: Return phone link href"""
        return self.page.locator(self.PHONE_LINK).get_attribute("href") or ""

    # ════════════════════════════════════════════════════════════════════════
    # ZONE-2: Logo & Slogan — new methods
    # ════════════════════════════════════════════════════════════════════════

    def verify_slogan_visible(self):
        """ZONE-2: Verify slogan text is visible"""
        slogan = self.page.locator(self.SLOGAN)
        expect(slogan).to_be_visible(timeout=10000)
        expect(slogan).to_contain_text(self.SLOGAN_TEXT, timeout=10000)

    def verify_main_logo_visible(self):
        """ZONE-2: Verify main logo image is visible"""
        expect(self.page.locator(self.MAIN_LOGO_IMG)).to_be_visible(timeout=10000)

    def verify_aao_logo_visible(self):
        """ZONE-2: Verify AAO logo image is visible"""
        expect(self.page.locator(self.AAO_LOGO_IMG)).to_be_visible(timeout=10000)

    def get_main_logo_href(self) -> str:
        """ZONE-2: Return main logo link href"""
        return self.page.locator(self.MAIN_LOGO_LINK).first.get_attribute("href") or ""

    # ════════════════════════════════════════════════════════════════════════
    # ZONE-3: Navigation & Search
    # ════════════════════════════════════════════════════════════════════════

    def verify_nav_links_visible(self):
        """ZONE-3: Verify all 5 nav links are visible"""
        for selector in [
            self.CLEARANCE_LINK,
            self.BRANDS_LINK,
            self.DENTAL_LINK,
            self.SURGERY_LINK,
            self.ORTHODONTIC_LINK,
        ]:
            expect(self.page.locator(selector)).to_be_visible(timeout=10000)


    def verify_search_input_visible(self):
        """ZONE-3: Verify desktop search input is visible"""
        expect(self.page.locator(self.SEARCH_INPUT)).to_be_visible(timeout=10000)

    def verify_search_button_visible(self):
        """ZONE-3: Verify desktop search button is visible"""
        expect(self.page.locator(self.SEARCH_BUTTON)).to_be_visible(timeout=10000)

    def verify_short_query_no_dropdown(self, query: str = "br"):
        """ZONE-3: Type < 3 chars, confirm NO dropdown appears.

        Uses fill() (instant) to avoid triggering the JS debounce,
        then waits longer than the 1000ms debounce to confirm nothing appears.
        """
        assert len(query) < 3, "This method is for queries shorter than 3 chars"
        self.page.locator(self.SEARCH_INPUT).type(query, delay=100)
        self.page.wait_for_timeout(2000)
        expect(self.page.locator(
            "div.search_results_container").first).not_to_be_visible(timeout=10000)


    def input_data_search_field(self, search_request: str):
        """Input data in the search field of the header"""
        search_popup = self.page.locator("div.search_results_container").filter(visible=True).first
        self.page.locator(
            "input.y-search__inp.int-header-search-input").type(
                search_request, delay=100)
        search_popup.wait_for(state="visible", timeout=15000)


    def verify_search_popup(self, product_name: str):
        """Verify a product in the search popup by name"""
        search_popup = self.page.locator("div.search_results_right").filter(visible=True).first
        expect(search_popup).to_contain_text(product_name, timeout=15000)


    # ════════════════════════════════════════════════════════════════════════
    # ZONE-4: Wishlist & Cart
    # ════════════════════════════════════════════════════════════════════════

    def verify_wishlist_button_visible(self):
        """ZONE-4: Verify wishlist button is visible"""
        expect(self.page.locator(self.WISHLIST_BUTTON)).to_be_visible(timeout=10000)

    def verify_wishlist_count_visible(self):
        """ZONE-4: Verify wishlist count badge is visible"""
        expect(self.page.locator(self.WISHLIST_COUNT)).to_be_visible(timeout=10000)

    def get_wishlist_href(self) -> str:
        """ZONE-4: Return wishlist button href"""
        return self.page.locator(self.WISHLIST_BUTTON).get_attribute("href") or ""

    def verify_cart_button_visible(self):
        """ZONE-4: Verify cart button is visible"""
        cart_btn = self.page.locator(self.CART_BUTTON).filter(visible=True).first
        expect(cart_btn).to_be_visible(timeout=10000)

    def verify_cart_count_badge_visible(self):
        """ZONE-4: Verify cart count badge is visible"""
        badge = self.page.locator(".int-cart-text-indicator").filter(visible=True).first
        expect(badge).to_be_visible(timeout=10000)

    def verify_account_button_visible(self):
        """ZONE-4: Verify account button is visible"""
        account_btn = self.page.locator(self.ACCOUNT_BUTTON_DESKTOP).filter(visible=True).first
        expect(account_btn).to_be_visible(timeout=10000)

    def get_account_greeting_text(self) -> str:
        """ZONE-4: Return greeting text from account button (e.g. 'Hi Name!')"""
        greeting = self.page.locator(self.ACCOUNT_GREETING).filter(visible=True).first
        return greeting.text_content() or ""

    def click_account_button_desktop(self):
        """ZONE-4: Click account button (desktop) and wait for dropdown animation"""
        btn = self.page.locator(self.ACCOUNT_BUTTON_DESKTOP).filter(visible=True).first
        btn.click()
        self.page.wait_for_selector(self.ACCOUNT_MODAL_DESKTOP, state="visible")

    def verify_account_dropdown_visible(self):
        """ZONE-4: Verify the account dropdown modal is visible"""
        expect(self.page.locator(self.ACCOUNT_MODAL_DESKTOP)).to_be_visible(timeout=10000)

    def verify_my_account_link_visible(self):
        """ZONE-4 (AUTH): Verify My Account link is visible in dropdown"""
        expect(self.page.locator(self.MY_ACCOUNT_LINK)).to_be_visible(timeout=10000)

    def verify_orders_link_visible(self):
        """ZONE-4 (AUTH): Verify Your Orders link is visible in dropdown"""
        expect(self.page.locator(self.ORDERS_LINK)).to_be_visible(timeout=10000)

    def verify_buy_again_link_visible(self):
        """ZONE-4 (AUTH): Verify Buy Again link is visible in dropdown"""
        expect(self.page.locator(self.BUY_AGAIN_LINK)).to_be_visible(timeout=10000)

    def get_my_account_href(self) -> str:
        """ZONE-4 (AUTH): Return My Account link href"""
        return self.page.locator(self.MY_ACCOUNT_LINK).get_attribute("href") or ""

    def get_orders_href(self) -> str:
        """ZONE-4 (AUTH): Return Orders link href"""
        return self.page.locator(self.ORDERS_LINK).get_attribute("href") or ""

    def get_buy_again_href(self) -> str:
        """ZONE-4 (AUTH): Return Buy Again link href"""
        return self.page.locator(self.BUY_AGAIN_LINK).get_attribute("href") or ""

    def get_logout_href(self) -> str:
        """ZONE-4 (AUTH): Return Logout link href (scoped to desktop modal)"""
        return self.page.locator(self.LOGOUT_LINK_DESKTOP).get_attribute("href") or ""

    def click_register_button(self):
        """Click the Register button in the header"""
        self.click(self.REGISTER_BUTTON)


    def click_cart_popup_button(self):
        """Open the cart popup"""
        self.click(self.CART_BUTTON)
        assert self.get_text("div.y-modal__title") == "SHOPPING CART"

    def click_login_button(self):
        """Click the Login button"""
        self.click(self.LOGIN_BUTTON)

    def click_logout_button(self):
        """Click the logout button"""
        self.click(self.LOGOUT_BUTTON)

    def verify_working_cart_counter(self):
        """Verify that the cart counter isn't 0"""
        cart_counter = self.page.locator(".int-cart-text-indicator").filter(visible=True).first
        cart_counter.wait_for(state="visible", timeout=15000)
        expect(cart_counter).not_to_have_text("0", timeout=15000)
