#Mouse Hover / Hover Menu

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/menu")
driver.implicitly_wait(5)

#Terdapat dua cara yaitu
#cara1
menu = driver.find_element(By.LINK_TEXT,"Main Item 2")
Hover = ActionChains(driver).move_to_element(menu)
Hover.perform()


#cara2
# ActionChains(driver).move_to_element((driver.find_elements(By.LINK_TEXT,"Main Item 2"))).perform()
