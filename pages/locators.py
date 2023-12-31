from selenium.webdriver.common.by import By
class LinksToTest():
    LINK = 'https://selenium1py.pythonanywhere.com/'
    LOGIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/accounts/login/'
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ADDED_TO_BASKET_NAME = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1) strong')
    ADDED_TO_BASKET_PRICE = (By.CSS_SELECTOR, '#messages .alert-info:nth-child(3) strong')


class BasketPageLocators():
    SHOW_BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs a.btn')
    NOT_EMPTY_ELEM = (By.CSS_SELECTOR, '#basket_formset')
