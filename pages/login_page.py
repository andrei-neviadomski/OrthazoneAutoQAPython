from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = 'input[name="email"]' # Проверь селектор на сайте
    PASSWORD_INPUT = 'input[name="password"]'
    LOGIN_SUBMIT_BUTTON = 'button:has-text("Login")'

    def login(self, email, password):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_SUBMIT_BUTTON)