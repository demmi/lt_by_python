import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://suninjuly.github.io/cats.html")  # открыть сайт, страницу cats
time.sleep(3)  # задержка 3 сек


# # --- найдем картинку кота по имени bullet и нажмем под ней кнопку
# bullet_cat = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[1]/div/div/div/div/button[1]").click()
# time.sleep(5)


# # --- протестируем текст 'Bullet cat'
def test_1():
    bullet_cat_text = driver.find_element(By.XPATH, '//p[text()="Bullet cat"]').text
    assert bullet_cat_text == 'Bullet cat', 'wrong!'
    time.sleep(3)
# 1 passed, 1 warning in 12.86ss


# # --- протестируем текст с ошибкой 'Bulletcat'
# def test_2():
#     bullet_cat_text = driver.find_element(By.XPATH, '//p[text()="Bullet cat"]').text
#     assert bullet_cat_text == 'Bulletcat', 'wrong!'
#     time.sleep(3)
# test_mytest01.py::test_2 FAILED                                          [100%]
# test_mytest01.py:24 (test_2)
# 'Bullet cat' != 'Bulletcat'
#
# Expected :'Bulletcat'
# Actual   :'Bullet cat'
# 1 failed, 1 warning in 9.46s
