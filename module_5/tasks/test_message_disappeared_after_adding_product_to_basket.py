from final import ProductPage


def test_guest_cant_see_success_message (browser):
    # Data
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    # Arrange
    page = ProductPage(browser, link)

    # Act
    page.open()
    page.add_to_basket()

    # Assert
    page.disappear_of_success_message()
