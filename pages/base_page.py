from playwright.sync_api import Page
from datetime import datetime
import os

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded", timeout=60000)

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.page.fill(selector, text)

    def get_text(self, selector: str):
        return self.page.inner_text(selector)
    
    def take_screenshot(self, name: str = "screenshot"):
        #Делает скриншот страницы и сохраняет его в папку screenshots
        # 1. Создаем папку, если её еще нет
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        # Добавляем небольшую задержку (например, 1000 мс = 1 секунда)
        self.page.wait_for_timeout(1000)
        
        # 2. Формируем имя файла: время + твое название
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = f"screenshots/{name}_{timestamp}.png"
        
        # 3. Делаем скриншот через Playwright
        self.page.screenshot(path=file_path, full_page=True)
        return file_path