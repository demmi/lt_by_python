import time
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://suninjuly.github.io/cats.html")

time.sleep(5)
bullet_cat = driver.find_element(By.XPATH, "//img[@id='bullet']/..//button[text()='View']").click()
time.sleep(5)

def test_1():
    bullet_cat_text = driver.find_element(By.XPATH, "//p[text()='Bullet cat']").text
    assert bullet_cat_text == 'Bullet cat', 'wrong!'
    time.sleep(5)