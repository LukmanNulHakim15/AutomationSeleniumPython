from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
#Jadi method "driver.maximaze_window()" berfungsi untuk memperluas window secara maksimal
#Sedangkan method "drive.minimaze_window()" berfungsi untuk memperkecil window
time.sleep(5)