from final import ProductPage


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Data
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    # Arrange
    page = ProductPage(browser, link)

    # Act
    page.open()
    page.add_to_basket()

    # Assert
    page.should_not_be_success_message()
