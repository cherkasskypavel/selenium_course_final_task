from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
# from .login_page import LoginPage

class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(self.browser, self.browser.current_url)
    def should_be_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'element isn`t present on this page'



# Закоментирован код для варианта с возвратом объекта LoginPage