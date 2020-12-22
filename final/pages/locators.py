from selenium.webdriver.common.by import By


class AccountPageLocators():
    WLCM_MSG = (By.CSS_SELECTOR, "#messages")
    # BASKET_INFO = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    PROFILE_SECTION = (By.XPATH, "//h1[text()='Profile']")
    EDIT_PROFILE_BTN = (By.CSS_SELECTOR, "[href$='/edit/']")
    FIRST_NAME = (By.CSS_SELECTOR, "#id_first_name")
    LAST_NAME = (By.CSS_SELECTOR, "#id_last_name")
    SAVE_BTN = (By.CSS_SELECTOR, "[data-loading-text='Saving...']")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REINPUT_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.XPATH, "//button[contains(@value,'Register')]")

    EMAIL_INPUT_FORM_FOR_REG_USER = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_INPUT_FORM_FOR_REG_USER = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[data-loading-text='Входим...']")
    ACCOUNT_BTN = (By.CSS_SELECTOR, "a[href$='/accounts/']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner")
    ADD_TO_BASKET_FROM_FICTION_SECTION = (By.CSS_SELECTOR, '.col-xs-6:nth-child(1) .btn')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    CATALOG_GOODS_LINK = (By.CSS_SELECTOR, "[href$='/catalogue/']")
    FICTION_SECTION_LINK = (By.CSS_SELECTOR, ".nav-list > li > ul > li:nth-child(1)")


class BasketPageLocators():
    BASKET_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner p")
    ITEMS_IN_BASKET_MSG = (By.CSS_SELECTOR, ".basket-title .col-sm-6")
