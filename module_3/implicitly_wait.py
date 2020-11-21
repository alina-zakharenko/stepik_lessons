from selenium import webdriver
import time

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд (Ожидание называется неявным (Implicit wait),
# так как его не надо явно указывать каждый раз, когда мы выполняем поиск элементов,
# оно автоматически будет применяться при вызове каждой последующей команды.)
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

time.sleep(1)
button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

# закрываем браузер после всех манипуляций
browser.quit()