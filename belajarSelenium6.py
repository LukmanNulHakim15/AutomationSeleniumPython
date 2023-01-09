from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://demoqa.com/login")
driver.get("https://demoqa.com/books")
driver.find_element('id', 'login').click()

#method driver.implecity_wait(5) 5 itu waktu dalam detik. Method ini berfungsi untuk memberikan jeda waktu dalam setiap method.
#untuk menghindari berjalannya fungsi dengan internet atau devace yang tidak mendukung
