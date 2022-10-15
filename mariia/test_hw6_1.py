
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.saucedemo.com/")


def test_title():
    title = driver.title
    assert title == 'Swag Labs'


def test_login_form():
    user_name = driver.find_element(By.CSS_SELECTOR, 'input#user-name')
    user_name.send_keys('standard_user')

    user_password = driver.find_element(By.CSS_SELECTOR, 'input#password')
    user_password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    button_login.click()

    # assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
    add_cart = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_cart.click()

    check_cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    check_cart.click()

    assert driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
