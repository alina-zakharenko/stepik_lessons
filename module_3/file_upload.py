
from selenium import webdriver
import time



# Открыть страницу http://suninjuly.github.io/file_input.html.
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

# Заполнить текстовые поля: имя, фамилия, email
input1 = browser.find_element_by_xpath("//input[contains(@placeholder, \"Enter first name\")]")
input1.send_keys("Ivan")
input2 = browser.find_element_by_xpath("//input[contains(@placeholder, 'Enter last name')]")
input2.send_keys("Petrov")
input3 = browser.find_element_by_xpath("//input[contains(@placeholder, 'Enter email')]")
input3.send_keys("Smolensk@ru")

# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
button = browser.find_element_by_id("file")
button.send_keys(file_path)

print(os.path.abspath(__file__))


# Нажать на кнопку "Submit"
button = browser.find_element_by_css_selector(".btn.btn-primary")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()
