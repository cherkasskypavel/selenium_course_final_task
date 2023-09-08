from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#registration_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ADDED_TO_BASKET_NAME = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1) strong')
    ADDED_TO_BASKET_PRICE = (By.CSS_SELECTOR, '#messages .alert-info:nth-child(3) strong')

#   в процессе реализации :)
class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs a.btn')
    PRODUCT_NAME = (By.CSS_SELECTOR,) # Добавить селектор
    PRODUCT_PRICE = (By.CSS_SELECTOR,) # Добавить селектор