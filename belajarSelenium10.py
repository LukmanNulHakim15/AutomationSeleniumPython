#Upload file selenium python

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


import pyautogui

driver = webdriver.Chrome()
#Upload file cara ke 1
# driver.get("https://demoqa.com/upload-download")

# driver.find_element('id','uploadFile').send_keys("C:/Users/Dell/Downloads/sertifikat.pdf")
# time.sleep(5)

#Upload file cara ke dua harus menambahkan dependencies import pyautogui namun perlu install dahulu dengan cara
#pip install pyautogui di CMD
driver.get("https://gofile.io/uploadFiles")
time.sleep(5)
driver.find_element(By.XPATH,"/html//div[@id='filesUpload']//button").click()
time.sleep(5)
pyautogui.write(r"C:\Users\Dell\Downloads\berita.pdf")
time.sleep(5)
pyautogui.press("enter")
time.sleep(5)
