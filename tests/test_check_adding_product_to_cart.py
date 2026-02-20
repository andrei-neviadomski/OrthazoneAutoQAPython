import os
from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from components.header import Header

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

    product_page = ProductPage(page)

    product_page.check_option_value_by_name("MBT .018")
    product_page.check_option_value_by_name("Hooks On 3")
    product_page.check_option_value_by_name("Maxillary Right Canine (UR3)")
    product_page.click_add_to_cart_button()

    header = Header(page)

    header.open_cart_popup()



    home_page.take_screenshot("BRACKET_SYSTEM")