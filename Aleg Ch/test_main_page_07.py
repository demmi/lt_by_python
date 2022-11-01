# Lesson 07 SELENIUM, WEBDRIVER, PYTEST, ФИКСТУРЫ, PAGE OBJECT MODEL

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # библиотека для скачивания свежего вебрайвера
from selenium.webdriver.chrome.service import Service  # класс Service отвечает за запуск и остановку chromedriver
from selenium.webdriver.common.by import By  # By - методы для нахождения элементов кода


def test_01():
    # под каждый тест создается свой экземпляр драйвера
    # создаем объект - экземпляр драйвера для хрома, и после "service=Service" указываем путь, где его взять
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://selenium1py.pythonanywhere.com/ru/')  # метод driver. get() откроет веб-страницу (URL)

# в Терминале запустим тест: pytest -v test_main_page_07.py
# флаг -v для показа, сколько % теста прошло, сколько нет

# ///// 25:46
