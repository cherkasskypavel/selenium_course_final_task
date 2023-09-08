from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        assert '/basket/' in self.browser.current_url, 'Страница с корзиной не открылась'
    def get_product_name_on_basket_page(self):
        text = self.get_text_of_element(*BasketPageLocators.PRODUCT_NAME)
        return text
    def get_product_price_on_basket_page(self):
        text = self.get_text_of_element(*BasketPageLocators.PRODUCT_PRICE)
        return text

# проверить, совпадают ли названия товаров на странице с товаром и в корзине