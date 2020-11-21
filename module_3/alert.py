import math

from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Открыть страницу http://suninjuly.github.io/alert_accept.html.
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

#Нажать на кнопку
button = browser.find_element_by_css_selector(".btn.btn-primary")
button.click()

#Принять confirm
confirm = browser.switch_to.alert
confirm.accept()

#На новой странице решить капчу для роботов, чтобы получить число с ответом
browser.find_element_by_xpath("// span[contains( @ id, 'input_value')]")

x_element = browser.find_element_by_xpath("// span[contains( @ id, 'input_value')]")
x = x_element.text
y = calc(x)

input = browser.find_element_by_xpath("//input[contains(@id,'answer')]")
input.send_keys(y)

# Нажать на кнопку "Submit"
button = browser.find_element_by_css_selector(".btn.btn-primary")
button.click()