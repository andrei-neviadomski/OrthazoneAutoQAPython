from .base_page import BasePage
from playwright.sync_api import expect

class HomePage(BasePage):
    # Выносим ожидаемый заголовок в константу
    EXPECTED_TITLE = "Orthodontic Supplies Store, Orthodontic Products & Instruments at Orthazone"

    def check_title(self):
        # Используем встроенный expect от Playwright для проверки
        expect(self.page).to_have_title(self.EXPECTED_TITLE)