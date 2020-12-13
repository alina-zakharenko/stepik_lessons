from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
       assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TXT), \
           "Text isn't present"