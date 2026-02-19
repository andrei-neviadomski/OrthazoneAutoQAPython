from .base_page import BasePage
from playwright.sync_api import expect
from components.header import Header

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)  # Передаем управление в BasePage
        self.header = Header(page) # Создаем объект хедера

    # Выносим ожидаемый заголовок в константу
    EXPECTED_TITLE = "Orthodontic Supplies Store, Orthodontic Products & Instruments at Orthazone"

    def check_title(self):
        # Используем встроенный expect от Playwright для проверки
        expect(self.page).to_have_title(self.EXPECTED_TITLE)