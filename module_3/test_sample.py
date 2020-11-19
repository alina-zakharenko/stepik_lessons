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
        browser.find_element_by_xpath(check_book_name)
        browser.find_element_by_xpath(check_deferred_benefit_offer)
        browser.find_element_by_xpath(check_basket_price)

        browser.find_element_by_xpath(check_basket_button)
        browser.find_element_by_xpath(checkout_button)


    finally:
        time.sleep(5)
        browser.quit()

add_book_to_basket()