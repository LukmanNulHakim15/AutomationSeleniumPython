# Handling pop up/ modal dialog
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()

for i in range (2):
    #cara looping di selenium QA python for i in range (2):
    response = driver.get('https://tees.co.id/')


    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]')))
        print("Pop up muncul woi")
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, 'Gak mau gratisan ah, mau beli aja!').click()
        print('popup di tutup')
        time.sleep(2)
    except TimeoutException:
        print("Popup tidak muncul pak")
        pass
