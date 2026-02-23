from pages.base_page import BasePage

class CategoryPage(BasePage):

    def click_category_by_name(self, name: str):
        self.click(f"span:has-text('{name}')")

    def click_product_by_name(self, name: str):
        self.click(f"a.prodcard__link:has-text('{name}')")