from selenium import webdriver
from selenium.webdriver.common.by import By

site = "http://test2.itcobra.ru"
loginmail = "maillogin"

d = webdriver.Chrome()
d.delete_all_cookies()
d.get(site)
d.implicitly_wait(10)
d.set_window_size(1440, 1024)

d.find_element(By.XPATH, "/html/body/div[3]/div[1]/header/div[1]/div/div/div/div[5]/div/div").click()
d.find_element(By.ID, "bx_auth_href_formMailRuOpenID").click()
d.find_element(By.NAME, "OPENID_IDENTITY_MAILRU").send_keys(loginmail)
d.find_element(By.XPATH, "/html/body/div[9]/div/div[2]/div/div/div[2]/div/div[2]/form/div/div[2]/input[4]").click()
d.quit()