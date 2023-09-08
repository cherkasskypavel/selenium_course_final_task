from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators, BasketPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'Нет кнопки "Добавить в корзину"'
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_first_allert(self):
        assert BasePage.is_alert_present(self), 'Первый Алерт не обнаружен'

    def should_be_answer_for_promo_quiz(self):
        self.solve_quiz_and_get_code()

    def get_product_name_on_product_page(self):
        text = self.get_text_of_element(*ProductPageLocators.PRODUCT_NAME)
        return text

    def get_product_price_on_product_page(self):
        text = self.get_text_of_element(*ProductPageLocators.PRODUCT_PRICE)
        return text

    def should_be_basket_button(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_BUTTON), 'Кнопка с корзиной не найдена'

    def go_to_basket(self):
        basket_button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)



