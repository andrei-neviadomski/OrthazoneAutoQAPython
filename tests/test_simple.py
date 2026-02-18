import os
from playwright.sync_api import Page, expect

def test_example_site(page: Page):
    # Берем URL из переменной окружения 'BASE_URL'. 
    # Если она не задана, по умолчанию идем на продакшен.
    base_url = os.getenv("BASE_URL", "https://orthazone.com") 
    
    page.goto(base_url)

    # Проверяем заголовок
    expect(page).to_have_title("Orthodontic Supplies Store, Orthodontic Products & Instruments at Orthazone")
