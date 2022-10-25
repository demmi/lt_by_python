import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://suninjuly.github.io/cats.html")

time.sleep(5)
bullet_cat=driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[1]/div/div/div/div/button[1]").click()
time.sleep(5)


# ////////// 1:25:55
