import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


#открыть страницу
#ввести правильный ответ
#нажать кнопку "Отправить"
#дождаться фидбека о том, что ответ правильный
#проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"




@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

@pytest.mark.parametrize('pagenumber', ["236895", "236896","236897","236898","236899","236903","236904","236905"])

def test_parametrize(browser, pagenumber):
    # открыть страницу
    link = f"https://stepik.org/lesson/{pagenumber}/step/1"
    browser.get(link)

    # ввести правильный ответ
    answer = str(math.log(int(time.time())))
    input = browser.find_element_by_css_selector('textarea')
    input.send_keys(answer)
    time.sleep(5)

    # Нажать на кнопку "Отправить"
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    time.sleep(5)

    # дождаться фидбека о том, что ответ правильный
    #WebDriverWait(browser, 12).until(EC.presence_of_element_located((By.ID, "correct")))


    # проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
    expected_text = "Correct!"
    expected_text_locator=browser.find_element_by_css_selector(".smart-hints__hint").text
    actual_text = "{}".format(expected_text_locator)
    assert actual_text in expected_text, "Text isn't correct"