#Тест Добавление одного товара в корзину
#Предусловия: Пользователь находится в разделе "Fiction",
#Проверка: выбранный товар есть на складе
#Шаг 1  пользователь добавляет первую книгу в корзину, нажатием на кнопку "В корзину"
#Ожидаемый результат: товар добавлен в корзину; пользователь может посмотреть корзину, нажав на кнопку "Посмотреть корзину" или начать оформление, нажав кнопку "Оформить"
#Проверка: Сообщение о добавленном товаре (Ariel был добавлен в вашу корзину.), сообщение о стоимости корзины (Стоимость корзины теперь составляет 26,99

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Main data
catalog_fiction_section_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/category/books/fiction_3/"
common_product_locator = "//article[contains(@class,'product_pod')]"


def add_book_to_basket():
    # Test Data
    product_name = "Ariel"
    product_locator = "{}[contains(text(), '{}')]".format(common_product_locator, product_name)
    expected_message_text = "Товар {} добавлен в корзину".format(product_name)


    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(catalog_fiction_section_link)

        # Act
        product = browser.find_element_by_xpath(product_locator)
        product.find_element_by_xpath("//button[contains(@type,'submit')]").click()


        # Assert
        result_message_text = browser.find_element_by_xpath("//strong[contains(text(),'Ariel')]").text
        assert result_message_text in expected_message_text, "Product should be added, but it doesn't"


        notifications_block = browser.find_element_by_css_selector("div#messages")
        basket_notification = notifications_block.find_element_by_css_selector("div.alert-info")
        basket_button = basket_notification.find_element_by_css_selector("a[href='/ru/basket/']")
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((basket_button, "Оформить")))
        checkout_button = basket_notification.find_element_by_css_selector("a[href='/ru/checkout/']")
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((checkout_button, "Оформить")))


    finally:
        time.sleep(5)
        browser.quit()

add_book_to_basket()