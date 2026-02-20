import os
from pages.home_page import HomePage
from pages.category_page import CategoryPage

def test_check_login_logout(page):
    home_page = HomePage(page)
    
    base_url = os.getenv("BASE_URL", "https://orthazone.com") 
    
    home_page.open(base_url)
    home_page.check_title()
    home_page.click_category_by_name("Bracket Systems")

    category_page = CategoryPage(page)
    
    category_page.click_category_by_name("Metal Brackets (Standard, Mini, Self-Ligating, Vertical Slot)")
    category_page.click_category_by_name("Metal Brackets - Mini Size")
    category_page.click_product_by_name("Metal Brackets - Mini")

    home_page.take_screenshot("BRACKET_SYSTEM")