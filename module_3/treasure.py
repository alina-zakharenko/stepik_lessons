import math

import calc as calc
import click as click
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    #Открыть страницу http://suninjuly.github.io/get_attribute.html
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    img = browser.find_element_by_xpath("//img")

    #Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    # Посчитать математическую функцию от x (сама функция остаётся неизменной)
    x = img.get_attribute("valuex")
    y = calc(x)
    print (x)
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
