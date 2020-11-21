import math

import calc as calc
import click as click
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    #Открыть страницу http://suninjuly.github.io/math.html
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Считать значение для переменной x
    browser.find_element_by_xpath("// span[contains( @ id, 'input_value')]")
    #browser.find_element_by_id("#input_value")

    #Посчитать математическую функцию от x
    x_element = browser.find_element_by_xpath("// span[contains( @ id, 'input_value')]")
    x = x_element.text
    y = calc(x)

    #Ввести ответ в текстовое поле
    input = browser.find_element_by_xpath("//input[contains(@id,'answer')]")
    input.send_keys(y)

    #Отметить checkbox "I'm the robot"
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()

    #Выбрать radiobutton "Robots rule!"
    option1 = browser.find_element_by_css_selector("#robotsRule")
    option1.click()

    #Нажать на кнопку Submit
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()


finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта

    time.sleep(10)

    # закрываем браузер после всех манипуляций

    browser.quit()
