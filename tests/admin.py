"""Admin pages"""
import os
from admin.admin_login_page import AdminLoginPage


def test_admin_page(page):
    """test admin page"""

    admin_login_page = AdminLoginPage(page)
    base_url = os.getenv("BASE_URL", "https://staged2.dentazone.com/")
    base_admin_url = base_url +"admin/"
    admin_login_page.open(base_admin_url)
    admin_login_page.fill('[name="username"]', "andrein")
    admin_login_page.fill('[name="password"]', "X9rAQH8s")
    admin_login_page.click('a.button')

    admin_login_page.click("a.top:has-text('Sales')")
    admin_login_page.click('a[href*="sale/order"]')
    admin_login_page.fill("[name='filter_customer_email']", "autotest-old@orthazone.com")
    admin_login_page.click("a.button:has-text('Filter')")


    while True:
        if admin_login_page.page.locator('input[name="selected[]"]').count() > 0:
            admin_login_page.page.locator('input[name="selected[]"]').first.click()
            admin_login_page.page.on("dialog", lambda dialog: dialog.accept())
            admin_login_page.click("a.button:has-text('Delete')")
        else:
            break

    admin_login_page.take_screenshot()
