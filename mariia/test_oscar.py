import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.add_to_cart_page import AddToCart

link = 'http://selenium1py.pythonanywhere.com/ru/'


def test_guest_can_go_to_catalogue(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.should_be_view_products()
    page.go_to_catalogue()


def test_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_login_page()
    page = LoginPage(browser, link)
    page.should_be_login_page()


def test_user_should_be_authorized(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open_page()
    page.register_user(email=str(time.time()) + "@gmail.com", password='fjksfakhfadjf234')
    time.sleep(2)
    page.user_should_be_authorized()
    time.sleep(3)


def test_add_to_cart(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.should_be_view_products()
    page.go_to_catalogue()
    page = AddToCart(browser, link)
    page.add_item_to_cart()
    time.sleep(2)
    page.check_cart()
    time.sleep(2)