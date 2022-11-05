# Lesson 07 SELENIUM, WEBDRIVER, PYTEST, ФИКСТУРЫ, PAGE OBJECT MODEL

# ---------- WEBDRIVER ----------
# import time
# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager  # библиотека для скачивания свежего вебрайвера
# from selenium.webdriver.chrome.service import Service  # класс Service отвечает за запуск и остановку chromedriver
# from selenium.webdriver.common.by import By  # By - методы поиска элементов страницы

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
# link = 'http://selenium1py.pythonanywhere.com/ru/'
#
#
# @pytest.fixture(scope='class')  # область видимости фикстуры - 'class'
# def browser():
#     print('\nstart browser...')
#     browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     yield browser
#     print('\nquit browser...')
#     browser.quit()


# class TestMainPage:
#     @pytest.mark.open_page  # маркировка тестa
#     @pytest.mark.smoke
#     def test_01(self, browser):
#         browser.get(link)  # метод get() откроет веб-страницу (URL)
#
#     @pytest.mark.view_products
#     def test_02(self, browser):
#         browser.get(link)
#         browser.find_element(By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a').click()  # поиск кнопки и ее нажатие
#         time.sleep(3)

# Чтобы распеатались наши сообщения при запуске теста в Терминале, ставим флаг -S:
# pytest -s -v test_main_page_07.py
# Видим, что браузер открылся один раз за два теста.
# Если область видимости поменять на функцию: @pytest.fixture(scope='function')
# то браузер откроется и закроется два раза/

# ----- Маркировка тестов
# Для запуска в Терминале теста с маркировкой ставим флаг -m
# Маркировку необходимо зарегистрировать в файле pytest.ini, создав его в корне проекта
# pytest -s -v -m open_page test_main_page_07.py - запустится маркированный тест - test_01
# pytest -s -v -m view_products test_main_page_07.py - запустится маркированный тест - test_02
# pytest -s -v -m 'not open_page' test_main_page_07.py - чтобы НЕ запустился маркированный test_01
# pytest -s -v -m 'open_page and not view_products' test_main_page_07.py - запуск и пропуск определенных тестов
# Маркерами можно выбирать для запуска, например, только smoke тесты или только regression тесты
#
# --- Маркировка xfail - для теста, который ожидаемо упадет из-за еще не исправленного бага
#     @pytest.mark.xfail  # тест пропускается, а остальные тесты выполняются: pytest -s -v test_main_page_07.py
#     def test_02(self, browser):
#         browser.get(link)
#         browser.find_element(By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a').click()  # вместо id="browse" - "brows"
#         time.sleep(3)
# pytest выдаст сообщение - XFAIL
# если ошибки уже нет, то pytest выдаст сообщение - XPASS. Тогда маркировку @pytest.mark.xfail можно убирать

# ---------- Глобальные настройки ----------
#
# Для глобальных настроек в корневой директории создаем файл conftest.py
# Туда выносим фикстуры:
# @pytest.fixture(scope='class')  # область видимости фикстуры - 'class'
# def browser():
#     print('\nstart browser...')
#     browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     yield browser
#     print('\nquit browser...')
#     browser.quit()
#
# И выносим туда следующие импорты:
# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager  # библиотека для скачивания свежего вебрайвера
# from selenium.webdriver.chrome.service import Service  # класс Service отвечает за запуск и остановку chromedriver
#
# Что остается в нашем тестовом файле:
# import time
# import pytest
# from selenium.webdriver.common.by import By  # By - методы поиска элементов страницы - переносим в main_psge.py
#
# link = 'http://selenium1py.pythonanywhere.com/ru/'
#
#
# class TestMainPage:
#     @pytest.mark.open_page
#     @pytest.mark.smoke
#     def test_01(self, browser):
#         browser.get(link)
#
#     @pytest.mark.view_products
#     def test_02(self, browser):
#         browser.get(link)
#         # browser.find_element(By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a').click()  # поиск и нажатие кнопки - эти
#         # действия пользователя переносим в файл main_psge.py
#         time.sleep(3)
#

# ---------- POM - Page Object Model ----------
#
# Это паттерн проектирования в Selenium, создающий репозиторий объектов для хранения всех веб-элементов
#
# --- Разделяем действия пользователя и тесты по разным файлам!
# В корне проекта создаем папку pages, в ней файл main_page.py, куда выносим действия пользователя
# В папке pages создаем файл base_page.py, где будут методы, общие для всех страниц
# Пишем классы и методы в эти файлы
#
# На практике локаторы - '//*[@id="browse"]/li/ul/li[1]/a' - для удобства тоже выносятся в отдельный файл,
# чтобы при изменениях править их в одном месте
# Создаем в корне проекта __init__.py — пустой файл для того, чтобы Python распознавал папку проекта,
# как Python модуль, что позволяет нам использовать его объекты внутри других частей проекта.

# import time
# import pytest
# from .pages.main_page import MainPage
#
# link = 'http://selenium1py.pythonanywhere.com/ru/'
#
#
# def test_guest_can_go_to_catalogue(browser):  # даем тесту говорящее название
#     page = MainPage(browser, link)  # Создаём объект page класса MainPage
#     page.open_page()  # для открытия страницы используем метод, унаследованный из класса BasePage
#     page.go_to_catalogue()  # для перехода в каталог используем метод, унаследованный из класса MainPage
#     time.sleep(1)
#

# Выносим локаторы в отдельный файл locators.py
# Для поиска элементов пишем туда: from selenium.webdriver.common.by import By
# и создаем класс:
# class MainPageLocators:
#     catalogue_link = (By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a')
# В main_page делаем импорт класса MainPageLocators
# и ссылаемся на локатор: self.browser.find_element(*MainPageLocators.catalogue_link).click()

# ----- Создаем общий метод для тестирования наличия элементов
# Добавляем в base_page.py функцию
#     def element_is_present(self, method, locator):
#         try:
#             self.browser.find_element(method, locator)
#         except NoSuchElementException:
#             print('Element is not present')
# и импортируем из селениума исключение NoSuchElementException
# Аргументы: method - как искать, locator - что искать
#
# import time
# import pytest
# from .pages.main_page import MainPage
#
# link = 'http://selenium1py.pythonanywhere.com/ru/'
#
#
# def test_guest_can_go_to_catalogue(browser):  # даем тесту говорящее название
#     page = MainPage(browser, link)  # Создаём объект page класса MainPage
#     page.open_page()  # для открытия страницы используем метод, унаследованный из класса BasePage
#     page.should_be_link_to_product_page()  # Проверяем, есть ли ссылка перехода в каталог
#     page.go_to_catalogue()  # для перехода в каталог используем метод, унаследованный из класса MainPage
#     time.sleep(1)
#

# ----- Добавим авторизацию
# Проверим:
# 1) что мы действительно на этой странице
# 2) что есть поля для авторизации - форма "Войти" и форма "Зарегистрировавться"
# Создадим локаторы LOGIN_FORM и REGISTER_FORM
# Создаем в папке page файл login_page.py
# мпортируем в него from .locators import LoginPageLocator
#
import pytest
import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/ru/'

# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу с товарами
# @pytest.mark.smoke
# def test_guest_can_go_to_catalogue(browser):
#     # создает экземпляр главной страницы - Main Page
#     page = MainPage(browser, link)
#     # открывает страницу
#     page.open_page()
#     # проверяет, что на главной странице присутствует ссылка на страницу товаров
#     page.should_be_link_to_product_page()
#     # переходит на страницу с товарами
#     page.go_to_product_page()



# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу авторизации
@pytest.mark.regression
def test_guest_can_go_to_login_page(browser):
    # создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    # открывает страницу
    page.open_page()
    # переходит на страницу авторизации
    page.go_to_login_page()
    time.sleep(2)
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет, что текущая страница является страницей авторизации
    page.should_be_login_page()

# ///// 2:36:25

# Тест проверяет, что пользователь может зарегистрироваться
# def test_user_сan_autorize(browser):
#     link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
#     # создает экземпляр страницы авторизации
#     page = LoginPage(browser, link)
#     # открывает страницу авторизации
#     page.open_page()
#     # регистрирует нового пользователя
#     page.register_user(email=str(time.time()) + '@mail.org', password='QAZ123edc!')
#     # проверяет, что пользователь авторизован
#     page.should_be_autorized_user()


# /////
