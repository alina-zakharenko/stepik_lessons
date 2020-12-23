from .base_page import BasePage
from .locators import AccountPageLocators
from .locators import LoginPageLocators


class AccountPage(BasePage):
    def go_to_account_page(self):
        account_btn = self.browser.find_element(*LoginPageLocators.ACCOUNT_BTN)
        account_btn.click()
        assert self.is_element_present(*AccountPageLocators.PROFILE_SECTION), "You are not in profile section"

    def edit_user_profile(self, firstname, lastname):
        edit_btn = self.browser.find_element(*AccountPageLocators.EDIT_PROFILE_BTN)
        edit_btn.click()
        first_name = self.browser.find_element(*AccountPageLocators.FIRST_NAME)
        first_name.clear()
        first_name.send_keys(firstname)
        last_name = self.browser.find_element(*AccountPageLocators.LAST_NAME)
        last_name.clear()
        last_name.send_keys(lastname)
        save_button = self.browser.find_element(*AccountPageLocators.SAVE_BTN)
        save_button.click()
