from selenium.webdriver.common.by import By
import time
from webbrowser import BaseBrowser

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("web page URL")
driver.get("http://suninjuly.github.io/cats.html")

# ////////// 1:15:06
