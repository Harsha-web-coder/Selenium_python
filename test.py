from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("sample test case started")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element("name", "q").send_keys("Harsha")
driver.find_element("name", "btnK").send_keys(Keys.ENTER)
time.sleep(3)
driver.close()
print("sample test case Executed")
