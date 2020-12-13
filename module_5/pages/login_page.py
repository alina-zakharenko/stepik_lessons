from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self,email, password):
        email_form = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_FORM)
        email_form.send_keys(email)
        passwd_1 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_FORM)
        passwd_1.send_keys(password)
        passwd_2 = self.browser.find_element(*LoginPageLocators.PASSWORD_REINPUT_FORM)
        passwd_2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REG_BTN)
        register_button.click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "String 'login' is not in current url of browser"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not found"
        assert True