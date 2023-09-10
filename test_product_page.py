import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import math
from selenium.common.exceptions import NoAlertPresentException
import time
from .pages.locators import LinksToTest

# def test_quest_can_add_product_to_basket(browser):
#     link = LinksToTest.LINK
#     page = ProductPage(browser, link)
#     page.open()
#     page.adding_to_basket()
#     page.should_be_basket_message()
#     page.is_page_and_message_product_name_equal()
#     page.is_page_and_message_product_price_equal()
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = LinksToTest.LINK
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = LinksToTest.LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = LinksToTest.LINK
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.should_succes_message_disappeared()