import pytest
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-GB',
                     help="Choose browser language: 'ru', 'en-GB', 'es', 'fr'")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    if language in ["ru", 'en-GB', 'es', 'fr']:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.implicitly_wait(5)
        browser.user_language = language

    else:
        raise pytest.UsageError("browser language must be in range of: 'ru', 'en-GB', 'es', 'fr'")

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    try:
        # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
        browser.save_screenshot('Screenshots/screenshot-%s.png' % now)
    finally:
        browser.quit()
