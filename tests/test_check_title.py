import os
from pages.home_page import HomePage

def test_example_site(page):
    # 1. Инициализируем страницу
    home_page = HomePage(page)
    
    # 2. Получаем URL (логика остается той же)
    base_url = os.getenv("BASE_URL", "https://orthazone.com") 
    
    # 3. Используем методы класса
    home_page.open(base_url)
    home_page.check_title()
    home_page.header.open_cart_popup()
    #home_page.take_screenshot("screen")