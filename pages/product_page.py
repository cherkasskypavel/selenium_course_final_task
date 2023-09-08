from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators, BasketPageLocators

class ProductPage(BasePage):

    #   добавляем товар в корзину, решаем загадку для получения скидки
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'Нет кнопки "Добавить в корзину"'
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_first_allert(self):
        assert BasePage.is_alert_present(self), 'Первый Алерт не обнаружен'

    def should_be_answer_for_promo_quiz(self):
        self.solve_quiz_and_get_code()


    #   проверяем наличие и корректность фидбека на странице после добавления товара в корзину
    def should_be_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_NAME), "Товар не добавился в корзину"

    def is_page_and_message_product_name_equal(self):
        on_page = self.get_text_of_element(*ProductPageLocators.PRODUCT_NAME)
        in_message = self.get_text_of_element(*ProductPageLocators.ADDED_TO_BASKET_NAME)
        assert on_page == in_message

    def is_page_and_message_product_price_equal(self):
        on_page = self.get_text_of_element(*ProductPageLocators.PRODUCT_PRICE)
        in_message = self.get_text_of_element(*ProductPageLocators.ADDED_TO_BASKET_PRICE)
        assert on_page == in_message




    #   переходим в корзину
    def should_be_basket_button(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_BUTTON), 'Кнопка с корзиной не найдена'

    def go_to_basket(self):
        basket_button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        basket_button.click()



