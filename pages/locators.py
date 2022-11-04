from selenium.webdriver.common.by import By  # By - методы поиска элементов страницы


class MainPageLocators:
    catalogue_link = (By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a')
