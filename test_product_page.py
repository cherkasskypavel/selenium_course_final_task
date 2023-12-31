import pytest
from .pages.product_page import ProductPage
import time
from .pages.locators import LinksToTest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link_coders = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
link_stars = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
main_page_link = LinksToTest.LINK
test_password = '123456789abcABC'
class TestUserAddToBasketFromProductPage():


    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login_link = LinksToTest.LOGIN_PAGE_LINK
        email = str(time.time()) + "@fakemail.org"
        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(email, test_password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_coders)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_coders)
        page.open()
        page.adding_to_basket()
        page.should_be_basket_message()
        page.is_page_and_message_product_name_equal()
        page.is_page_and_message_product_price_equal()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = LinksToTest.LINK
    page = ProductPage(browser, link_coders)
    page.open()
    page.adding_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason='success message is always on page')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_coders)
    page.open()
    page.adding_to_basket()
    page.should_succes_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_stars)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_stars)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, main_page_link)
    page.open()
    page.go_to_basket()
    next_page = BasketPage(browser, url=browser.current_url)
    next_page.should_be_basket_page()
    next_page.should_be_nothing_in_basket()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link_coders)
    page.open()
    page.adding_to_basket()
    page.should_be_basket_message()
    page.is_page_and_message_product_name_equal()
    page.is_page_and_message_product_price_equal()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_coders)
    page.open()
    page.should_not_be_success_message()

if __name__ == '__main__':
    pytest.main()