from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.account_page import AccountPage
import pytest
import time


class TestUserCanGoToAccountPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = "TestTest@fakemail.org"
        password = "Start123+"
        page.login_user(email, password)
        page.should_be_authorized_user()
        self.browser = browser

    def test_user_can_go_to_account(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        # Arrange
        page = AccountPage(browser,link)
        # Act
        page.open()
        # Assert
        page.go_to_account_page()

    def test_user_can_edit_profile_data(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/profile/"
        # Arrange
        page = AccountPage(browser,link)
        # Act
        page.open()
        # Assert
        page.go_to_account_page()
        page.edit_user_profile("TestFN", "TestLN")



