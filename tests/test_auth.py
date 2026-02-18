""" import os
from pages.login_page import LoginPage

def test_failed_login(page):
    # 1. Инициализируем страницу
    login_page = LoginPage(page)
    
    # 2. Используем URL из переменной окружения (которую мы настроили в GitHub)
    base_url = os.getenv("BASE_URL", "https://orthazone.com")
    login_page.open(f"{base_url}/login")

    # 3. Выполняем действие
    login_page.login("wrong@email.com", "wrong_password")

    # 4. Проверяем результат
    assert "Invalid login" in login_page.get_error_text() """