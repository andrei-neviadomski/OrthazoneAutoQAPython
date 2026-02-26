from pages.base_page import BasePage

class CategoryPage(BasePage):

    def click_category_by_name(self, name: str):
        category_locator = self.page.locator(f"span.catagory-wrap__item--name:has-text('{name}')")
        category_locator.wait_for(state="visible", timeout=20000)
        category_locator.click()

    def click_product_by_name(self, name: str):
        product_locator = self.page.locator(f"a.prodcard__link:has-text('{name}')").first
        product_locator.wait_for(state="visible", timeout=20000)
        product_locator.click()