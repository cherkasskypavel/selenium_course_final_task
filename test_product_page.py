import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import math
from selenium.common.exceptions import NoAlertPresentException
import time
from .pages.locators import LinksToTest, LoginPageLocators
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage



class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, LoginPageLocators.TEST_PASSWORD)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = LinksToTest.LINK
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = LinksToTest.LINK
        page = ProductPage(browser, link)
        page.open()
        page.adding_to_basket()
        page.should_be_basket_message()
        page.is_page_and_message_product_name_equal()
        page.is_page_and_message_product_price_equal()

@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = LinksToTest.LINK
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = LinksToTest.LINK
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.should_succes_message_disappeared()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
@pytest.mark.xfail(reason='forcibly failed by using invalid link in locators.py')
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.skip
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = LinksToTest.MAIN_PAGE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    next_page = BasketPage(browser, url=browser.current_url)
    next_page.should_be_basket_page()   #   проверяем, открылась ли страница с корзиной, по URL
    next_page.should_be_nothing_in_basket() #   проверяем пустоту корзины через отсуствие формы
                                            #   c добавленными товарами

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = LinksToTest.LINK
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.should_be_basket_message()
    page.is_page_and_message_product_name_equal()
    page.is_page_and_message_product_price_equal()
