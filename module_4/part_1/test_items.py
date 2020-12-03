def test_items(browser):
    #Data

    expected_btn_text_dict = {
        "ru": "Добавить в корзину",
        "en_GB": "Add to basket",
        "es": "Añadir al carrito",
        "fr": "Ajouter au panier"
    }

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    expected_language_code = browser.user_language
    expected_btn_text = expected_btn_text_dict [expected_language_code]

    basket_btn_locator = ".btn.btn-lg.btn-primary.btn-add-to-basket"

    try:
        #Arrange
        browser.get(link)

        #Act
        button_add_to_basket = browser.find_element_by_css_selector(basket_btn_locator)
        basket_button_actual_text = button_add_to_basket.text


        #Assert
        assert basket_button_actual_text in expected_btn_text, "text is different"
        print("actual text " + basket_button_actual_text)
        print("expected_btn_text " + expected_btn_text)

    finally:
        browser.quit()