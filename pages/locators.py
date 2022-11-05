from selenium.webdriver.common.by import By  # By - методы поиска элементов страницы


class MainPageLocators:
    CATALOGUE_LINK = (By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a')
    LOGIN_BTN = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocator:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
