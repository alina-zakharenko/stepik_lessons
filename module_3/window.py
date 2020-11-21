import math

from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Открыть страницу http://suninjuly.github.io/redirect_accept.html.
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

#Нажать на кнопку
button = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
button.click()

#Переключиться на новую вкладку
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
first_window = browser.window_handles[0]


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

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()
