from selenium import webdriver
import time

def add_book_to_basket():
    # Data
    main_page_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/category/books/fiction_3/"
    in_storage = "// p[contains( @class ,'instock availability')] // i[contains( @ class, 'icon-ok')]"
    add_to_basket = "//div[contains(@class, 'product_price')]//form[contains(@action, '/ru/basket/add/97/')]"
    check_book_name = "//strong[contains(text(),'Ariel')]"
    check_deferred_benefit_offer = "//strong[contains(text(),'Deferred benefit offer')]"
    check_basket_price = "//strong[contains(text(),'26,99')]"
    check_basket_button = "//p//a[contains(text(),'Посмотреть корзину')]"
    checkout_button = "//p//a[contains(text(),'Оформить')]"
    #//div[contains(@class, 'container-fluid.page')]
    add_to_basket_text = "был добавлен в вашу корзину"
    meet_condition_text = "Ваша корзина удовлетворяет условиям предложения"
    price_text = "Стоимость корзины теперь составляет "
    basket_button_text = "Посмотреть корзину"
    checkout_basket_button_text = "Оформить"


    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)
        browser.find_element_by_xpath(in_storage)

        # Act
        browser.find_element_by_xpath(add_to_basket).click()

        # Assert
        browser.find_element_by_xpath(check_book_name)
        check_add_to_basket_text = browser.find_element_by_xpath("//div[contains(@class,'alertinner ')]")
        assert add_to_basket_text in check_add_to_basket_text.text, "Неверный текст о добавлении товара в корзину"

        browser.find_element_by_xpath(check_deferred_benefit_offer)
        check_meet_condition_text = browser.find_element_by_css_selector("div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(2)")
        assert meet_condition_text in check_meet_condition_text.text, "Неверный текст об удовлетворении условиям предложения"

        browser.find_element_by_xpath(check_basket_price)
        check_price_text = browser.find_element_by_xpath("//div[contains(@class,'alertinner ')]//p[contains(text(),'Стоимость')]")
        assert price_text in check_price_text.text, "Неверный текст о стоимости корзины"


        browser.find_element_by_xpath(check_basket_button)
        check_basket_button_text =browser.find_element_by_xpath("//p//a[contains(text(),'Посмотреть корзину')]")
        assert basket_button_text in check_basket_button_text.text, "Неверное имя кнопки"

        browser.find_element_by_xpath(checkout_button)
        check_checkout_button_text = browser.find_element_by_xpath("//p//a[contains(text(),'Оформить')]")
        assert checkout_basket_button_text in check_checkout_button_text.text, "Неверное имя кнопки оформления заказа"

    finally:
        time.sleep(5)
        browser.quit()

add_book_to_basket()