import math

import calc as calc
import click as click
from selenium import webdriver
import time

from selenium.webdriver.remote.webelement import WebElement

try:
    # Открыть страницу http://suninjuly.github.io/selects1.html
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x, y):
        return str(int(x) + int(y))

    # Посчитать сумму заданных чисел
    num1 = browser.find_element_by_id('num1')
    x = num1.text
    num2 = browser.find_element_by_id("num2")
    y = num2.text
    sum = calc (x, y)
    print (sum)

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(sum)  # ищем элемент с значением x

    # Нажать на кнопку Submit
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()


finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта

    time.sleep(10)

    # закрываем браузер после всех манипуляций

    browser.quit()
