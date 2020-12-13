from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT_FORM =(By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT_FORM =(By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REINPUT_FORM =(By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN =(By.XPATH, "//button[contains(@value,'Register')]")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR,".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_EMPTY_MSG=(By.CSS_SELECTOR, "#content_inner p")
    ITEMS_IN_BASKET_MSG = (By.CSS_SELECTOR, ".basket-title .col-sm-6")

