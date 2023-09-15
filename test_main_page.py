import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import LinksToTest
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    link = LinksToTest.LINK
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.xfail(reason='invalid link used for prduct page tests purposes')
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser=browser, url=browser.current_url)
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = LinksToTest.LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    next_page = BasketPage(browser, url=browser.current_url)
    next_page.should_be_basket_page()
    next_page.should_be_nothing_in_basket()


if __name__ == '__main__':
    pytest.main()

