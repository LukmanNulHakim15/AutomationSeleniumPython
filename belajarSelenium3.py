from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/windows")

time.sleep(2)
driver.find_element(By.LINK_TEXT,'Click Here').click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
#Jadi method "driver.switch_to.window(driver.window_handles[0])" jadi method ini berfungsi untuk melakukan perpindahan tab.
# Dengan parameter array  
time.sleep(5)