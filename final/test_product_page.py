from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import pytest
import time


class TestProductPage:

    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                              ])
    # @pytest.mark.xfail(reason="Задание: независимость контента, ищем баг")
    def test_guest_can_add_product_to_basket(self, browser, link):
        # Data
        product_name = "Coders at Work"
        template = "{} has been added to your basket."
        basket_total_price = "£19.99"
        # Arrange
        link = f"{link}"
        page = ProductPage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        # Act
        page.open()  # открываем страницу
        page.should_be_add_btn()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        # Assert
        page.check_add_to_basket_notification(product_name, template)
        page.check_product_and_basket_price(basket_total_price)

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Arrange
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логинa
        # Act
        login_page = LoginPage(browser, browser.current_url)
        # Assert
        login_page.should_be_login_page()
        login_page.should_be_login_url()
        login_page.should_be_register_form()
        login_page.should_be_login_form()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Arrange
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.should_be_empty_msg()

    def test_guest_can_add_product_to_basket_from_fiction_section(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        common_product_locator = "//article[contains(@class,'product_pod')]"
        product_name = "Ariel"
        product_locator = "{}[contains(., '{}')]".format(common_product_locator, product_name)
        template = "{} был добавлен в вашу корзину.".format(product_name)
        expected_product_price = "26,99 £"

        # Arrange
        page = BasePage(browser, link)
        page.open()
        page.go_to_all_goods_section_page()
        page.go_to_fiction_section_page()
        product = page.browser.find_element_by_xpath(product_locator)
        product.find_element_by_css_selector('.col-xs-6:nth-child(1) .btn').click()

        # Assert
        page.check_add_to_basket_notification_from_base_page(product_name, template)
        page.check_product_and_basket_price_from_base_page(expected_product_price)


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "Start123+"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        self.browser = browser

    def test_user_cant_see_success_message(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        # Arrange
        page = ProductPage(browser, link)
        # Act
        page.open()
        # Assert
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="Необходимо имплементировать уникальный локатор")
    def test_user_can_add_product_to_basket_from_non_fiction_section(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/books/non-fiction_5/"
        product_name = "Coders at Work"
        template = "{} has been added to your basket."
        basket_total_price = "£19.99"
        # Arrange
        page = ProductPage(browser, link)
        # Act
        page.open()  # открываем страницу
        page.should_be_add_btn()
        page.add_to_basket()
        # Assert
        page.check_add_to_basket_notification(product_name, template)
        page.check_product_and_basket_price(basket_total_price)
