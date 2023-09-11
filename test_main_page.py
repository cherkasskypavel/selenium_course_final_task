import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import LinksToTest
from .pages.basket_page import BasketPage
@pytest.mark.skip
def test_guest_can_see_login_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page() # закомментировать при использовании варианта с возвратом
    # login_page = page.go_to_login_page()  # Параметры передаются при возврате
    # login_page.should_be_login_page()
    login_page = LoginPage(browser=browser, url=browser.current_url) # закомментировать при использовании варианта с возвратом
    login_page.should_be_login_page() # закомментировать при использовании варианта с возвратом

# Закоментирован код для варианта с возвратом объекта LoginPage методом из класса MainPage

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = LinksToTest.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    next_page = BasketPage(browser, url=browser.current_url)
    next_page.should_be_basket_page()   #   проверяем, открылась ли страница с корзиной, по URL
    next_page.should_be_nothing_in_basket() #   проверяем пустоту корзины через отсуствие формы
                                            #   c добавленными товарами

