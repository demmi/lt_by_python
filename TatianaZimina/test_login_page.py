import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.saucedemo.com/')

def test_title():
    title = driver.title
    assert title == 'Swag Labs'


def test_login():
    time.sleep(1)
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(1)

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'wrong url'

    driver.quit()