from selenium import webdriver
import time



main_page_link = "http://selenium1py.pythonanywhere.com/ru"

search_input_locator = "#id_q"
search_button_locator = "input.btn.btn-default"
search_title_locator = "h1"


def test_item_search():
    # Data
    search_text = "The shellcoder's handbook"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        search_input = browser.find_element_by_css_selector(search_input_locator)
        search_input.clear()

        # Act
        search_input.send_keys(search_text)
        browser.find_element_by_css_selector(search_button_locator).click()

        # Assert
        search_title = browser.find_element_by_css_selector(search_title_locator)
        assert search_text in search_title.text, \
            "Page title should contain searching item name"

    finally:
        time.sleep(15)
        browser.quit()

test_item_search()