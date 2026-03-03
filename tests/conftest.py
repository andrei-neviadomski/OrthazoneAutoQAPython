"""Autotest Framework Settings"""
from datetime import datetime
import os
from playwright.sync_api import Error as PlaywrightError
import pytest
from dotenv import load_dotenv
from pages.home_page import HomePage
from admin.admin_login_page import AdminLoginPage

load_dotenv()

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
def setup_order_test(page, context):
    """Setup fixtures for tests with orders"""
    home_page = HomePage(page)
    base_url = os.getenv("BASE_URL", "https://orthazone.com/")
    home_page.open(base_url)
    home_page.check_title()

    yield home_page

    try:
        context.clear_cookies()
        page.evaluate("localStorage.clear(); sessionStorage.clear();")
    except PlaywrightError as e:
        print(f"Error during clinning up: {e}")

    admin_login_page = AdminLoginPage(page)
    base_admin_url = base_url +"admin/"
    admin_login_page.open(base_admin_url)
    admin_login_page.fill('[name="username"]', os.getenv("ADMIN_USERNAME"))
    admin_login_page.fill('[name="password"]', os.getenv("ADMIN_PASSWORD"))
    admin_login_page.click('a.button')

    admin_login_page.click("a.top:has-text('Sales')")
    admin_login_page.click('a[href*="sale/order"]')
    admin_login_page.fill("[name='filter_customer_email']", os.getenv("ADMIN_TEST_EMAIL"))
    admin_login_page.click("a.button:has-text('Filter')")

    admin_login_page.page.on("dialog", lambda dialog: dialog.accept())

    while True:
        rows = admin_login_page.page.locator("table.list tbody tr:not(.filter)")
        if rows.count() == 0:
            break
        cell = rows.first.locator("td:nth-child(6)")
        if cell.inner_text() == os.getenv("ADMIN_TEST_EMAIL"):
            admin_login_page.page.locator('input[name="selected[]"]').first.click()
            admin_login_page.click("a.button:has-text('Delete')")
        else:
            break

@pytest.fixture(scope="function")
def setup_base_test(page, context):
    """Setup fixtures for tests without orders"""
    home_page = HomePage(page)
    base_url = os.getenv("BASE_URL", "https://orthazone.com/")
    home_page.open(base_url)
    home_page.check_title()

    yield home_page

    try:
        context.clear_cookies()
        page.evaluate("localStorage.clear(); sessionStorage.clear();")
    except PlaywrightError as e:
        print(f"Error during clinning up: {e}")
