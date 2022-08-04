from selenium import webdriver
from selenium.webdriver.common.by import By
import time

site = "http://test2.itcobra.ru"
loginmail = "maillogin"

d = webdriver.Chrome()
d.delete_all_cookies()
d.get(site)
d.implicitly_wait(10)
d.set_window_size(1440, 1024)

d.find_element(By.XPATH, "/html/body/div[3]/div[1]/header/div[1]/div/div/div/div[5]/div/div").click()

d.find_element(By.ID, "bx_auth_href_formLivejournal").click()
d.find_element(By.XPATH, '//*[@id="bx_auth_serv_formLivejournal"]/input[4]').click()
print("Livejournal auth error - ", d.find_element(By.ID, "OPENID_IDENTITY_LIVEJOURNAL-error").text)

d.find_element(By.ID, "bx_auth_href_formMailRuOpenID").click()
d.find_element(By.XPATH, '//*[@id="bx_auth_serv_formMailRuOpenID"]/input[4]').click()
print("MailRuOpenID auth error - ", d.find_element(By.ID, "OPENID_IDENTITY_MAILRU-error").text)

d.find_element(By.ID, "bx_auth_href_formLiveinternet").click()
d.find_element(By.XPATH, '//*[@id="bx_auth_serv_formLiveinternet"]/input[4]').click()
print("Liveinternet auth error - ", d.find_element(By.ID, "OPENID_IDENTITY_LIVEINTERNET-error").text)

d.find_element(By.ID, "bx_auth_href_formOpenID").click()
d.find_element(By.XPATH, '//*[@id="bx_auth_serv_formOpenID"]/input[4]').click()
print("OpenID auth error - ", d.find_element(By.ID, "OPENID_IDENTITY_OPENID-error").text)

d.quit()