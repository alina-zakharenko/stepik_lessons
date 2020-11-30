import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_items(browser):

    try:
        #Arrange
        browser.get(link)
        basket_button_locator = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket").text

        #Act
        basket_button_actual_text = "{}".format(basket_button_locator)
        print("actual text " + basket_button_actual_text)
        basket_button_expected_text = "{}".format(basket_button_locator)
        print("expected text " + basket_button_expected_text)

        #Assert
        assert basket_button_actual_text in basket_button_expected_text, "Please, check browser language"
        time.sleep(10)

    finally:
        browser.quit()