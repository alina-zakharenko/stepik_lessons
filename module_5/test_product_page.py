from selenium.webdriver.common.by import By

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest



class TestMainPage:

    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

    def test_guest_can_add_product_to_basket(self, browser, link):
        # TestData
        #product_name = "The shellcoder's handbook"
        #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        link = f"{link}"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_product_page()
        #page.should_be_login_url()
        page.should_be_add_btn()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_product_name()
        page.check_product_price()

        #add_to_basket_expected_message_text = "{} был добавлен в вашу корзину.".format(product_name)
        #add_to_basket_actual_message_text = browser.find_element_by_xpath("//strong[contains(text(), \"The shellcoder's handbook\")]").text
        #assert add_to_basket_actual_message_text in add_to_basket_expected_message_text, "Product should be added, but it doesn't"

