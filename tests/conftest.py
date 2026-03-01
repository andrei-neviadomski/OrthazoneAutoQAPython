"""Autotest Framework Setings"""
from datetime import datetime
import os
from playwright.sync_api import Error as PlaywrightError
import pytest
from pages.home_page import HomePage

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Setup a screenshot when a test failed"""
    _ = call
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page_fixture = item.funcargs.get("page")
        if page_fixture:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_path = f"screenshots/FAILED_{item.name}_{timestamp}.png"
            page_fixture.screenshot(path=file_path)

@pytest.fixture(scope="function")
def setup_base_test(page, context):
    """Setup fixtures for tests"""
    home_page = HomePage(page)
    base_url = os.getenv("BASE_URL", "https://orthazone.com")
    home_page.open(base_url)
    home_page.check_title()

    yield home_page

    try:
        context.clear_cookies()
        page.evaluate("localStorage.clear(); sessionStorage.clear();")
    except PlaywrightError as e:
        print(f"Ошибка при очистке данных: {e}")
