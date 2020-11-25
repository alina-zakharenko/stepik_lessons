#Тест Добавление одного товара в корзину
#Предусловия: Пользователь находится в разделе "Fiction",
#Проверка: выбранный товар есть на складе
#Шаг 1  пользователь добавляет первую книгу в корзину, нажатием на кнопку "В корзину"
#Ожидаемый результат: товар добавлен в корзину; пользователь может посмотреть корзину, нажав на кнопку "Посмотреть корзину" или начать оформление, нажав кнопку "Оформить"
#Проверка: Сообщение о добавленном товаре (Ariel был добавлен в вашу корзину.), сообщение о стоимости корзины (Стоимость корзины теперь составляет 26,99

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# MainData
catalog_fiction_section_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/category/books/fiction_3/"
common_product_locator = "//article[contains(@class,'product_pod')]"


def add_book_to_basket():

    # TestData
    browser = webdriver.Chrome()
    product_name = "Ariel"
    product_locator = "{}[contains(., '{}')]".format(common_product_locator, product_name)
    add_to_basket_expected_message_text = "{} был добавлен в вашу корзину.".format(product_name)

    in_stock_expected_text = "Товар находится На складе"

    try:
        # Arrange
        browser.implicitly_wait(5)
        browser.get(catalog_fiction_section_link)

        # Вспомогательная проверка: товар находится на складе
        in_stock_locator = browser.find_element_by_xpath("//p[contains(@class,'instock availability')]").text
        in_stock_actual_text = "Товар находится {}".format(in_stock_locator)
        print(in_stock_actual_text in in_stock_expected_text)


        # Act
        product = browser.find_element_by_xpath(product_locator)
        product.find_element_by_xpath("//button[contains(@data-loading-text,'Добавление...')]").click()

        # Assert
        # Проверка: сообщение о добавленном товаре
        add_to_basket_actual_message_text = browser.find_element_by_xpath("//strong[contains(text(), 'Ariel')]/parent::div").text
        print("add_to_basket_result_message_text: " + add_to_basket_actual_message_text)
        print("add_to_basket_expected_message_text: " + add_to_basket_expected_message_text)
        assert add_to_basket_actual_message_text in add_to_basket_expected_message_text, "Product should be added, but it doesn't"

        # Проверка: сообщение о стоимости корзины
        product_price_locator = browser.find_element_by_xpath("//div[contains(@class, 'alert-info')]/child::div/p/strong").text
        basket_price_expected_message_text = "Стоимость корзины теперь составляет {}".format(product_price_locator)
        basket_price_actual_message_text = browser.find_element_by_xpath("//div[contains(@class, 'alert-info')]/child::div/p").text
        print("basket_price_actual_message_text: " + basket_price_actual_message_text)
        print("basket_price_expected_message_text: " + basket_price_expected_message_text)
        assert basket_price_actual_message_text in basket_price_expected_message_text, "Please, check product price"

        #Проверка: наличие кнопок "Посмотреть корзину" и "Оформить"
        notifications_block = browser.find_element_by_css_selector("div#messages")
        basket_notification = notifications_block.find_element_by_css_selector("div.alert-info")
        basket_notification.find_element_by_css_selector("a[href='/ru/basket/']")
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Посмотреть корзину")))
        basket_notification.find_element_by_css_selector("a[href='/ru/checkout/']")
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Оформить")))


    finally:
        browser.quit()

add_book_to_basket()