import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose browser language: 'ru', 'en-GB', 'es', 'fr'")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    if language in ["ru",'en', 'es', 'fr']:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.implicitly_wait(5)
        browser.user_language = language

    else:
        raise pytest.UsageError("browser language must be in range of: 'ru', 'en', 'es', 'fr'")

    yield browser
    browser.quit()