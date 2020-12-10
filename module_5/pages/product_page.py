from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_login_url()
        self.should_be_add_btn()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "?promo=newYear" in self.browser.current_url, "String '?promo=newYear' is not in current url of browser"
        assert True

    def should_be_add_btn(self):
        # проверка, что есть кнопка добавленияв корзину
        basket_btn = self.is_element_present(*ProductPageLocators.ADD_TO_BASKET)
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button is not presented"
        assert True

    def add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_btn.click()
        assert True


#    def check_product_name(self):
#        expected_product_name_dict = {"The shellcoder's handbook", "Coders at Work"}
#        expected_product_name = self.browser.find_element(By.CSS_SELECTOR, ".alert:nth-child(1) strong").text
#        #return expected_product_name
#        assert expected_product_name in expected_product_name_dict

    def check_product_name(self):
        expected_product_name = self.browser.find_element(By.CSS_SELECTOR, ".alert:nth-child(1) strong").text
        actual_product_name = self.browser.find_element(By.CSS_SELECTOR, "h1").text
        print("Actual product name is " + actual_product_name, "Expected product name is "+ expected_product_name)
        assert actual_product_name in expected_product_name

    def check_product_price(self):
        expected_product_price = self.browser.find_element(By.CSS_SELECTOR, ".alertinner>p>strong").text
        actual_product_price = self.browser.find_element(By.CSS_SELECTOR, ".price_color:nth-child(2)").text
        print("Actual product price is " + actual_product_price, "Expected product price is " + expected_product_price)
        assert actual_product_price in expected_product_price






