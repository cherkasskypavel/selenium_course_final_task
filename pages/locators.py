from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#registration_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main.price_color')
class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs a.btn')
    PRODUCT_NAME = (By.CSS_SELECTOR,) # Добавить селектор
    PRODUCT_PRICE = (By.CSS_SELECTOR,) # Добавить селектор