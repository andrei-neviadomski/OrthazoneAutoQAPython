"""Home page"""
from playwright.sync_api import expect
from components.header import Header
from .base_page import BasePage

class HomePage(BasePage):
    """Home page"""

    def __init__(self, page):
        super().__init__(page)  # Передаем управление в BasePage
        self.header = Header(page) # Создаем объект хедера

    # Выносим ожидаемый заголовок в константу
    EXPECTED_TITLE = "Orthodontic Supplies Store, Orthodontic Products & Instruments at Orthazone"
    BRACKET_SYSTEM_BUTTON = 'span:has-text("Bracket Systems")'

    def check_title(self):
        """Используем встроенный expect от Playwright для проверки"""
        expect(self.page).to_have_title(self.EXPECTED_TITLE)

    def click_category_by_name (self, name: str):
        """Click a category by name"""
        category_locator = self.page.locator(f"span.catagory-wrap__item--name:has-text('{name}')")
        category_locator.wait_for(state="visible", timeout=20000)
        category_locator.click()

    def set_stripe_cookie(self):
        """Это полный аналог ввода команды в консоль браузера"""
        self.page.evaluate('document.cookie = "stripe_dev_test=1"')
