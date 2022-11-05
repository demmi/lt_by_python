# from .base_page import BasePage  # относительный путь к импортируемому модулю
# # from pages.base_page import BasePage  # абсолютный путь к импортируемому модулю
# from selenium.webdriver.common.by import By

# При указании относительного импорта мы используем запись через точку (. или ..).
# Одиночная точка base_page указывает на тот же каталог, из которого вызывается импорт.
# Пара точек перед названием модуля означает переход на два уровня вверх от текущего.
# Абсолютный импорт более предпочтителен. Вы указываете абсолютный путь к импортируемому модулю из корня проекта


# class MainPage(BasePage):
#     def go_to_catalogue(self):
#         self.browser.find_element(By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a').click()


# --- Локаторы - '//*[@id="browse"]/li/ul/li[1]/a' - обычно для удобства выносятся в отдельный файл (locators.py)
from .base_page import BasePage
# from selenium.webdriver.common.by import By  # перенесли в locators.py
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_link_to_product_page(self):
        assert self.element_is_present(*MainPageLocators.CATALOGUE_LINK)

    def go_to_catalogue(self):
        self.browser.find_element(*MainPageLocators.CATALOGUE_LINK).click()

