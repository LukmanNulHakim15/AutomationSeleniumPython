#datePicker
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pyautogui

driver = webdriver.Chrome()

# driver.get("https://jqueryui.com/datepicker/")
# driver.implicitly_wait(10)
# driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="content"]/iframe'))
# time.sleep(3)
#cara pertama
# driver.find_element('id', 'datepicker').click()
# time.sleep(3)
# driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[1]/a').click()
# time.sleep(3)

#cara kedua
# driver.find_element('id', 'datepicker').send_keys('07/22/2023')
# time.sleep(3)
# #jika ingin mengganti value dari date picker kita menggunakan clear
# driver.find_element('id', 'datepicker').clear()
# time.sleep(3)


#cara ketiga
driver.get('https://demoqa.com/date-picker')
# driver.switch_to.frame(driver.find_element(By.XPATH,'/html/body/iframe[1]'))
time.sleep(3)
driver.find_element('id', 'datePickerMonthYearInput').click()
pyautogui.press('backspace',presses=10)
time.sleep(3)
driver.find_element('id', 'datePickerMonthYearInput').send_keys('07/22/1992')
time.sleep(3)