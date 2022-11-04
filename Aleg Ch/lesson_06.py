# Lesson 06 html, css-selectors, xpath

# ----- импорт методов -----
import time
# import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# ----- поиск элементов -----
driver.get("http://suninjuly.github.io/cats.html")  # открыть сайт, страницу cats
time.sleep(3)  # задержка 3 сек

# --- найдем картинку кота по имени bullet и нажмем под ней кнопку
bullet_cat=driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[1]/div/div/div/div/button[1]").click()
time.sleep(5)

# # --- протестируем текст 'Bullet cat'
# создаем test_mytest01.py и дальше работаем в нем
# вписать там: import pytest
# запустить test_mytest01 с функцией:
# def test_1():
#     bullet_cat_text = driver.find_element(By.XPATH, '//p[text()="Bullet cat"]').text
#     assert bullet_cat_text == 'Bullet cat', 'wrong!'
#     time.sleep(5)


# ////////// End
