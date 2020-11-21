import math

from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Открыть страницу http://suninjuly.github.io/math.html.
browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

# Считать значение для переменной x
browser.find_element_by_xpath("// span[contains( @ id, 'input_value')]")

# Посчитать математическую функцию от x
x_element = browser.find_element_by_xpath("// span[contains( @ id, 'input_value')]")
x = x_element.text
y = calc(x)

# Проскроллить страницу вниз
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True

# Ввести ответ в текстовое поле
input = browser.find_element_by_xpath("//input[contains(@id,'answer')]")
input.send_keys(y)

# Выбрать checkbox "I'm the robot".
option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()

# Переключить radiobutton "Robots rule!".
option1 = browser.find_element_by_css_selector("#robotsRule")
option1.click()

# Нажать на кнопку "Submit"
button = browser.find_element_by_css_selector(".btn.btn-primary")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()
