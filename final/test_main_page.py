from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
import pytest


@pytest.mark.login_guest
class TestMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логинa
        # Act
        login_page = LoginPage(browser, browser.current_url)
        # Assert
        login_page.should_be_login_page()
        login_page.should_be_login_url()
        login_page.should_be_register_form()
        login_page.should_be_login_form()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = MainPage(browser, link)
        page.open()
        # Act
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.should_be_empty_msg()
        basket_page.should_be_no_products_in_the_basket()
