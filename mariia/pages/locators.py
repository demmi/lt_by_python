from selenium.webdriver.common.by import By


class MainPageLocators:
    CATALOGUE_LINK = (By.CSS_SELECTOR, '#browse > li > ul > li:nth-child(1) > a')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login_link"]')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form > h2')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form > h2')
    REGISTER_EMAIL = (By.XPATH, '//*[@id="id_registration-email"]')
    REGISTER_PASSWORD = (By.XPATH, '//*[@id="id_registration-password1"]')
    CONFIRM_PASSWORD = (By.XPATH, '//*[@id="id_registration-password2"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="register_form"]/button')

class BasePageLocator:
    USER_ICON = (By.XPATH, '//*[@id="top_page"]/div[2]/div/ul/li[1]/a/i')
