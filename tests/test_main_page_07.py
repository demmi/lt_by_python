# Lesson 07 SELENIUM, WEBDRIVER, PYTEST, ФИКСТУРЫ, PAGE OBJECT MODEL
# ---------- WEBDRIVER ----------
import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # библиотека для скачивания свежего вебрайвера
from selenium.webdriver.chrome.service import Service  # класс Service отвечает за запуск и остановку chromedriver
from selenium.webdriver.common.by import By  # By - методы для нахождения элементов кода

# Напишем тест: открыть сайт
# def test_01():
#     # под каждый тест создается свой экземпляр драйвера
#     # создаем объект - экземпляр драйвера для хрома, и после "service=Service" указываем путь, где его взять
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get('http://selenium1py.pythonanywhere.com/ru/')  # метод driver. get() откроет веб-страницу (URL)
#     driver.quit()  # команда закрытия браузера и остановки драйвера браузера
# в Терминале запустим тест: pytest -v test_main_page_07.py
# флаг -v для показа, сколько % теста прошло, сколько нет

# Напишем тест: открыть catalogue - кликнуть по кнопке "Все товары" на сайте
# def test_02():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get('http://selenium1py.pythonanywhere.com/ru/')
#     driver.find_element(By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a').click()  # поиск кнопки и ее нажатие
#     time.sleep(3)
#

# ---------- FIXTURES. ФИКСТУРЫ - вспомогательные функции для тестов ----------
#
# --- Фикстуры внутри класса
# link = 'http://selenium1py.pythonanywhere.com/ru/'
#
# Код для открытия браузера выносим в метод setup. Для закрытия браузера - метод teardown.
#
# class TestMainPage():
#     def setup(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
#     def test_01(self):
#         self.driver.get(link)  # метод driver. get() откроет веб-страницу (URL)
#
#     def test_02(self):
#         self.driver.get(link)
#         self.driver.find_element(By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a').click()  # поиск кнопки и ее нажатие
#         time.sleep(3)
#
#     def teardown(self):
#         self.driver.quit()  # команда закрытия браузера и остановки драйвера браузера

# --- Фикстуры внутри теста
# Импорты и фикстуры обычно выносят в отдельный файл
link = 'http://selenium1py.pythonanywhere.com/ru/'


@pytest.fixture(scope='class')  # область видимости фикстуры - 'class'
def browser():
    print('\nstart browser...')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    print('\nquit browser...')
    browser.quit()

class TestMainPage():

    def test_01(self, browser):
        browser.get(link)  # метод get() откроет веб-страницу (URL)

    def test_02(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a').click()  # поиск кнопки и ее нажатие
        time.sleep(3)

# Чтобы распеатались наши сообщения при запуске теста в Терминале, ставим флаг S:
# pytest -s -v test_main_page_07.py
# Видим, что браузер открылся один раз за два теста.
# Если область видимости поменять на функцию: @pytest.fixture(scope='function')
# то браузер откроется и закроется два раза/
#

# ///// 53:20
