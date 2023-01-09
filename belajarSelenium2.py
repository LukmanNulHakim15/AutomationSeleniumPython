from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

browser = driver.get("https://the-internet.herokuapp.com/login")
trial = driver.find_element("id", "username") #menggunakan locating method menggunakan atribut id disebuat element
#jika mencari by name " trial = driver.find_element("name", "username") "
trial.send_keys("tomsmith")
print("assert pass input field")
time.sleep(5)
driver.find_element("id","password").send_keys("SuperSecretPassword!")
print("assert pass input password")
time.sleep(5)
trial.submit() #action submit
assertisinstance(browser, webdriver, "Comparation Done")
#Contoh diatas menggunakan variabel
time.sleep(5)
driver.find_element(By.LINK_TEXT, 'Elemental Selenium').click()
time.sleep(15)