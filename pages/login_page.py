from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'URL страницы логина некорректный'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Отсутствует форма логина'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Отсутствует форма регистрации'

    def register_new_user(self, email, password):
        email_input = self.find_element_by_CSS(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        password_input = self.find_element_by_CSS(*LoginPageLocators.REGISTER_PASSWORD1)
        password_input.send_keys(password)
        repeat_password = self.find_element_by_CSS(*LoginPageLocators.REGISTER_PASSWORD2)
        repeat_password.send_keys(password)
        registration_button = self.find_element_by_CSS(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()




