"""Autotest Framework Settings"""
from datetime import datetime
import os
from playwright.sync_api import Error as PlaywrightError
import pytest
from dotenv import load_dotenv
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
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
        if admin_login_page.page.locator('input[name="selected[]"]').count() == 0:
            break
        cell = admin_login_page.page.locator(
            "table.list tbody tr:not(.filter) td:nth-child(6)").first
        if cell.inner_text() == os.getenv("ADMIN_TEST_EMAIL"):
            admin_login_page.page.locator('input[name="selected[]"]').first.click()
            admin_login_page.click("a.button:has-text('Delete')")
        else:
            break

    admin_login_page.click("#sale > a.top")
    admin_login_page.click("#sale a.parent:text('Customers')")
    admin_login_page.click("a[href*='route=sale/customer&']")


    admin_login_page.fill("[name='filter_email']", os.getenv("ADMIN_NEW_EMAIL"))
    admin_login_page.click("a.button:has-text('Filter')")
    admin_login_page.page.on("dialog", lambda dialog: dialog.accept())
    while True:
        if admin_login_page.page.locator('input[name="selected[]"]').count() == 0:
            break
        cell = admin_login_page.page.locator(
            "table.list tbody tr:not(.filter) td:nth-child(4)").first
        if cell.inner_text() == os.getenv("ADMIN_NEW_EMAIL"):
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


@pytest.fixture(scope="function")
def setup_logged_in_test(page, context):
    """Setup fixture for header tests that require an authenticated user.

    Logs in using ADMIN_TEST_EMAIL / ADMIN_TEST_PASSWORD env vars.
    Yields HomePage after successful login.
    Clears cookies/storage on teardown.
    """
    home_page = HomePage(page)
    base_url = os.getenv("BASE_URL", "https://orthazone.com/")
    login_page = LoginPage(page)

    home_page.open(base_url)
    home_page.header.click_account_button()
    home_page.header.click_login_button()
    login_page.add_creds_and_login()
    home_page.check_title()

    yield home_page

    try:
        context.clear_cookies()
        page.evaluate("localStorage.clear(); sessionStorage.clear();")
    except PlaywrightError as e:
        print(f"Error during cleanup: {e}")


@pytest.fixture(scope="function")
def setup_cart_with_product(page, context):
    """Setup fixture for cart modal tests.

    Opens homepage, navigates to Metal Brackets - Mini, adds one item
    (MBT .018 / Hooks On 3 / Maxillary Right Canine UR3) to the cart.
    Yields HomePage so tests can interact with the header immediately.
    Clears cookies/storage on teardown.

    Used by: test_cart010..test_cart014
    """
    home_page = HomePage(page)
    base_url = os.getenv("BASE_URL", "https://orthazone.com/")
    category_page = CategoryPage(page)
    product_page = ProductPage(page)

    home_page.open(base_url)
    home_page.check_title()

    home_page.click_category_by_name("Bracket Systems")
    category_page.click_category_by_name(
        "Metal Brackets (Standard, Mini, Self-Ligating, Vertical Slot)"
    )
    category_page.click_category_by_name("Metal Brackets - Mini Size")
    category_page.click_product_by_name("Metal Brackets - Mini")

    product_page.select_option_value_by_name("MBT .018")
    product_page.select_option_value_by_name("Hooks On 3")
    product_page.select_option_value_by_name("Maxillary Right Canine (UR3)")
    product_page.click_add_to_cart_button()

    yield home_page

    try:
        context.clear_cookies()
        page.evaluate("localStorage.clear(); sessionStorage.clear();")
    except PlaywrightError as e:
        print(f"Error during cleanup: {e}")
