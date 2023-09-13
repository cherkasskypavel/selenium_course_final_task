from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):                #   проверка перехода в корзину по подстроке в ссылке
        assert '/basket/' in self.browser.current_url, 'Страница с корзиной не открылась'

    def should_be_nothing_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_ELEM)


