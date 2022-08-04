from selenium import webdriver
from selenium.webdriver.common.by import By

site = "http://test2.itcobra.ru"
loginmail = "goel.rengis@yandex.ru"
passw = "gXenKs09X40e1"

#Chrome
d = webdriver.Chrome()
d.get(site)
d.implicitly_wait(10)
d.set_window_size(1440, 768)

d.find_element(By.XPATH, "/html/body/div[3]/div[1]/header/div[1]/div/div/div/div[5]/div/div/a/span/span").click()
d.find_element(By.NAME, "USER_LOGIN").send_keys(loginmail)
d.find_element(By.NAME,"USER_PASSWORD").send_keys(passw)
d.find_element(By.NAME,"Login").click()

d.quit()

