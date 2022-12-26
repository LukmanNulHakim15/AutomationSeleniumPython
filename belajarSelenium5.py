#Materi kali ini mengajarkan error handle

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
time.sleep(2)
# driver.find_element('id','alertButton').click()
# time.sleep(2)
# driver._switch_to.alert.accept()
# time.sleep(2)
#method "driver._switch_to.alert.accept()" berfungsi untuk menekan button alert OKE
###################################################################################

# driver.find_element('id','confirmButton').click()
# time.sleep(2)
# driver._switch_to.alert.dismiss()
# time.sleep(5)
#method "driver._switch_to.alert.dismiss" berfungsi untuk menekan button alert cancel
###################################################################################

driver.find_element('id','promtButton').click()
time.sleep(2)
driver._switch_to.alert.send_keys("Lukman ganteng")
time.sleep(5)
driver._switch_to.alert.accept()
time.sleep(2)
#method "driver._switch_to.alert.send_keys("Lukman ganteng")" berfungsi untuk mengisi field dialert