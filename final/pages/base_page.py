import math
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


class BasePage():

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def go_to_all_goods_section_page(self):
        link = self.browser.find_element(*BasePageLocators.CATALOG_GOODS_LINK)
        link.click()

    def go_to_fiction_section_page(self, timeout=5):
        self.browser.find_element(*BasePageLocators.FICTION_SECTION_LINK)
        catalog_fiction_section_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/category/books/fiction_3/"
        self.browser.implicitly_wait(timeout)
        self.browser.get(catalog_fiction_section_link)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_add_to_basket_notification_from_base_page(self, expected_product_name, expected_notification_template):
        expected_notification_text = expected_notification_template.format(expected_product_name)
        actual_notification_text = self.browser.find_element(By.XPATH,
                                                             "//strong[contains(text(), 'Ariel')]/parent::div").text
        print("Actual product name is " + actual_notification_text,
              "Expected product name is " + expected_notification_text)
        assert actual_notification_text == expected_notification_text, "Product name isn't correct"

    def check_product_and_basket_price_from_base_page(self, expected_product_price):
        actual_product_price = self.browser.find_element(By.XPATH,
                                                         "//div[contains(@class, 'alert-info')]/child::div/p/strong").text
        print("Actual product price is " + actual_product_price, "Expected product price is " + expected_product_price)
        assert actual_product_price == expected_product_price, "Product price isn't correct"
