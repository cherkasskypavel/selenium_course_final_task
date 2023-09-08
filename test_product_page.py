from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import math
from selenium.common.exceptions import NoAlertPresentException

class TestShopBasket():
    def test_quest_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.add_to_basket()
        page.should_be_first_allert()
        page.should_be_answer_for_promo_quiz()

    def test_guest_can_enter_basket(self, browser):
        pass

# проверить, совпадают ли названия товаров на странице с товаром и в корзине