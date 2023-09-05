from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page() # закомментировать при использовании варианта с возвратом
    # login_page = page.go_to_login_page()  # Параметры передаются при возврате
    # login_page.should_be_login_page()
    login_page = LoginPage(browser=browser, url=browser.current_url) # закомментировать при использовании варианта с возвратом
    login_page.should_be_login_page() # закомментировать при использовании варианта с возвратом
def test_guest_can_see_login_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_page()

# Закоментирован код для варианта с возвратом объекта LoginPage методом из класса MainPage
