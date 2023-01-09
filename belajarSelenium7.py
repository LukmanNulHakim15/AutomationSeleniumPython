from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
time.sleep(5)
driver.find_element('id','timerAlertButton').click()

try:
    WebDriverWait(driver,10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("Berhasil pencet oke")
except TimeoutException:
    print("Gagal pencet oke di alaert")
    pass

#Untuk menggunakan method explicitly await ada beberapa driver yang harus di import
#serta menggunakan try and except
#pengertian pass disini jika fungsi tidak berjalan makan sistem akan terus membaca kodingan selanjutnya