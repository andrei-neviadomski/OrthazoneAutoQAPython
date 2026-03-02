"""Admin pages"""
import os
from admin.admin_login_page import AdminLoginPage


def test_admin_page(page):
    """test admin page"""

    admin_login_page = AdminLoginPage(page)
    base_admin_url = os.getenv("BASE_ADMIN_URL", "https://orthazone.com/admin/")
    admin_login_page.open(base_admin_url)
    admin_login_page.take_screenshot()
