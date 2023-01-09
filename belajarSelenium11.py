#belajar drag and drop
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://demoqa.com/droppable")
driver.maximize_window()
driver.implicitly_wait(5)

elemen = driver.find_element('id','draggable')
kotak = driver.find_element('id', 'droppable')

action = ActionChains(driver)

action.drag_and_drop(elemen, kotak).perform()