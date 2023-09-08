import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import math
from selenium.common.exceptions import NoAlertPresentException
import time
from .pages.locators import LinksToTest
@pytest.mark.parametrize("link", LinksToTest.LINK_LIST)
def test_quest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.should_be_first_allert()
    page.should_be_answer_for_promo_quiz()
    page.should_be_basket_message()
    page.is_page_and_message_product_name_equal()
    page.is_page_and_message_product_price_equal()





