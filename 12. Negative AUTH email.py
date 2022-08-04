from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

d = webdriver.Chrome()

site = "http://test2.itcobra.ru"
loginmail1 = "goel.rengis@yandex.r"
loginmail2 = "goel.rengis"
passw = "gXenKs09X40e1"
wait = WebDriverWait(d, 20)

d.delete_all_cookies()
d.get(site)
d.implicitly_wait(10)
d.set_window_size(1440, 1024)

d.find_element(By.XPATH, "/html/body/div[3]/div[1]/header/div[1]/div/div/div/div[5]/div/div").click()
d.find_element(By.NAME, "USER_LOGIN").send_keys(loginmail1)
d.find_element(By.NAME, "USER_PASSWORD").send_keys(passw)
d.find_element(By.CSS_SELECTOR, "#avtorization-form > div.but-r > div.buttons.clearfix > input").click()

print("Error with loginmail1 - ", d.find_element(By.CSS_SELECTOR, "#ajax_auth > div.alert.alert-danger").text)

d.find_element(By.NAME, "USER_LOGIN").clear()
d.find_element(By.NAME, "USER_PASSWORD").clear()
d.find_element(By.NAME, "USER_LOGIN").send_keys(loginmail2)
d.find_element(By.NAME, "USER_PASSWORD").send_keys(passw)
d.find_element(By.CSS_SELECTOR, "#avtorization-form > div.but-r > div.buttons.clearfix > input").click()

print("Error with loginmail2 - ", d.find_element(By.CSS_SELECTOR, "#ajax_auth > div.alert.alert-danger").text)



d.quit()