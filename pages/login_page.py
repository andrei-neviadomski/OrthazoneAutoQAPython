from .base_page import BasePage

class LoginPage(BasePage):
    # Локаторы выносим в начало, чтобы их было легко менять
    EMAIL_INPUT = 'input[name="email"]'
    PASSWORD_INPUT = 'input[name="password"]'
    LOGIN_BUTTON = 'button[type="submit"]'
    ERROR_MESSAGE = '.alert-danger'

    def login(self, email, password):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_text(self):
        return self.get_text(self.ERROR_MESSAGE)