from .base_page import BasePage
from.locators import AddToCartLocators


class AddToCart(BasePage):
    def add_item_to_cart(self):
        self.browser.find_element(*AddToCartLocators.ADD_BUTTON).click()


    def check_cart(self):
        self.browser.find_element(*AddToCartLocators.CHECK_CART)
