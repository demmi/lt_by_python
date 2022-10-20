from selenium.webdriver.common.by import By


class MainPageLocators:
    CATALOGUE_LINK = (By.CSS_SELECTOR, '#browse > li > ul > li:nth-child(1) > a')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login_link"]')

class AddToCartLocators:
    ADD_BUTTON = (By.XPATH, '//*[@id="default"]/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/form/button')
    CHECK_CART = (By.XPATH, '//*[@id="messages"]/div[1]/div')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form > h2')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form > h2')
    REGISTER_EMAIL = (By.XPATH, '//*[@id="id_registration-email"]')
    REGISTER_PASSWORD = (By.XPATH, '//*[@id="id_registration-password1"]')
    CONFIRM_PASSWORD = (By.XPATH, '//*[@id="id_registration-password2"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="register_form"]/button')

class BasePageLocator:
    USER_ICON = (By.XPATH, '//*[@id="top_page"]/div[2]/div/ul/li[1]/a/i')
