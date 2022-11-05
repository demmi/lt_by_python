from .locators import LoginPageLocator
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_link(self):  # находимся ли мы на логин пейдж - сравним в адресной строке 'title'
        assert 'login' in self.browser.current_url, 'wrong url'

    def should_be_login_form(self):
        assert self.element_is_present(*LoginPageLocator.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.element_is_present(*LoginPageLocator.REGISTER_FORM)
