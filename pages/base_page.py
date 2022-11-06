from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_page(self):
        self.browser.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_BTN).click()

    def should_be_authorized_user(self):
        assert self.element_is_present(*BasePageLocators.USER_ICON)
