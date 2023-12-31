from selenium.common.exceptions import NoAlertPresentException, TimeoutException
import math
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from .locators import BasePageLocators, BasketPageLocators
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(10)
    def open(self):
        self.browser.get(self.url)
    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except:
            return False
        return True
    def find_element_by_CSS(self, how, what, timeout=6):
        element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        return element

    def is_alert_present(self, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]                            # из первого алерта вытаскиваем переменную
        answer = str(math.log(abs((12 * math.sin(float(x))))))  #   подставляем в функцию
        print(answer)                                           #   выводим ответ в консоль на всякий случай (-s)
        alert.send_keys(answer)
        alert.accept()                                          #   отправляем результат в поле ввода
        try:
            alert = self.browser.switch_to.alert                #   выводим ответ из второго алерта в консоль,
            alert_text = alert.text                             #   если алерта не последовало, перехватываем
            print(f"Your code: {alert_text}")                   #   исключение
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_text_of_element(self, how, what):
        text = self.browser.find_element(how, what).text
        return text

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            return False
        except TimeoutException:
            return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((how, what)))
            return True
        except TimeoutException:
            return False

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link isn`t presented'

    def go_to_basket(self, timeout=4):
        basket_button = WebDriverWait(
            self.browser, timeout).until(EC.presence_of_element_located(BasketPageLocators.SHOW_BASKET_BUTTON))
        basket_button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"

