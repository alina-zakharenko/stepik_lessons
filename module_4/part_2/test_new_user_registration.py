import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


def test_new_user_registration(browser):
    # Data
    main_page_link = "http://selenium1py.pythonanywhere.com/"
    email_input_field_locator = "id_registration-email"
    password_input_field_locator = "id_registration-password1"
    password_reinput_field_locator = "id_registration-password2"
    reg_btn_locator = "//button[contains(@value,'Register')]"
    search_title_locator = ".alertinner.wicon"

    expected_welcome_text = "Thanks for registering!"


    # Arrange
    browser.implicitly_wait(5)
    browser.get(main_page_link)

    # Act
    button = browser.find_element_by_id("login_link")
    button.click()

    email_input_field = browser.find_element_by_id(email_input_field_locator)
    email_input_field.send_keys("TesterTest17@gmail.com")
    password_input_field = browser.find_element_by_id(password_input_field_locator)
    password_input_field.send_keys("Start123+")
    password_reinput_field = browser.find_element_by_id(password_reinput_field_locator)
    password_reinput_field.send_keys("Start123+")

    reg_button = browser.find_element_by_xpath(reg_btn_locator)
    reg_button.click()

    # Assert
    search_title = browser.find_element_by_css_selector(search_title_locator)
    assert expected_welcome_text == search_title.text, "Page should contain welcome text"
