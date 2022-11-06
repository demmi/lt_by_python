from selenium.webdriver.common.by import By  # By - методы поиска элементов страницы


class MainPageLocators:
    CATALOGUE_LINK = (By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a')
    LOGIN_BTN = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocator:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.XPATH, '//*[@id="register_form"]/button')


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')  # когда ищем не по имени, а по селектору, то перед .icon-user точка
