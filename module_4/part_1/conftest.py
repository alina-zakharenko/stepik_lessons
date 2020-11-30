import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_language', action='store', default="ru", help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("browser_language")

    if browser_language == "de":
        print("\nstart de browser for test..")
        browser = webdriver.Firefox()
    elif browser_language == "ru":
        print("\nstart ru browser for test..")
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--browser_language should be ru or de")
    yield browser
    print("\nquit browser..")
    browser.quit()
