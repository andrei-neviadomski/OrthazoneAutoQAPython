from pages.base_page import BasePage

class ProductPage(BasePage):

    def select_option_value_by_name(self, name: str):
        self.click(f"label:has-text('{name}')")

    def click_add_to_cart_button(self):
        # 1) add-to-cart
        with self.page.expect_response(
            lambda r: "index.php?route=checkout/cart/add" in r.url,
            timeout=15000
        ) as add_info:
            self.click("a:has-text('Add to Cart')")

        add_resp = add_info.value

        # 2) refresh mini-cart (gives count_products)
        with self.page.expect_response(
            lambda r: "index.php?route=module/cart&response=1" in r.url,
            timeout=15000
        ) as cart_info:
            pass

        cart_resp = cart_info.value

        try:
            data = cart_resp.json()
        except Exception:
            # на случай если вернулось не JSON
            body = cart_resp.text()
            raise AssertionError(
                "Cart response is not JSON. "
                f"add_url={add_resp.url} add_status={add_resp.status} "
                f"cart_url={cart_resp.url} cart_status={cart_resp.status} "
                f"body_head={body[:500]}"
            )

        count = int(data.get("count_products", 0))
        assert count >= 1, (
            f"Expected cart count >= 1, got {count}. "
            f"add_url={add_resp.url} add_status={add_resp.status} "
            f"cart_url={cart_resp.url} cart_status={cart_resp.status}"
        )