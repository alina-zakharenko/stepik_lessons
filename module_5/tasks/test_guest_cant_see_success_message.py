from final import ProductPage


def test_guest_cant_see_success_message (browser):
    # Data
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    # Arrange
    page = ProductPage(browser, link)

    # Act
    page.open()

    # Assert
    page.should_not_be_success_message()
