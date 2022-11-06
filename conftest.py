import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # библиотека для скачивания свежего вебрайвера
from selenium.webdriver.chrome.service import Service  # класс Service отвечает за запуск и остановку chromedriver


@pytest.fixture(scope='class')  # область видимости фикстуры - 'class'
def browser():
    print('\nstart browser...')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    print('\nquit browser...')
    browser.quit()
