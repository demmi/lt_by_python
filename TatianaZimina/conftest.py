import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service




@pytest.fixture(scope='function')
def browser():
    print('\nbrowser')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    yield browser
    print('/\nquit')
    browser.quit()