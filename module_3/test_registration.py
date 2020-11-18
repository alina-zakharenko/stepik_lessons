from selenium import webdriver
import time

import unittest

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//input[contains(@placeholder, \"Input your first name\")]")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[contains(@placeholder, 'Input your last name')]")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[contains(@placeholder, 'Input your email')]")
        input3.send_keys("Smolensk@ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироватьс, ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(str(welcome_text), "Congratulations! You have successfully registered!", "Неправильный welcome text!")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)

        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//input[contains(@placeholder, \"Input your first name\")]")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[contains(@placeholder, 'Input your last name')]")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[contains(@placeholder, 'Input your email')]")
        input3.send_keys("Smolensk@ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться, ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(str(welcome_text), "Congratulations! You have successfully registered!", "Неправильный welcome text!")

