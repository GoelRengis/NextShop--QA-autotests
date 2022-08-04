from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


site = "http://test2.itcobra.ru"


#Chrome

d = webdriver.Chrome()
d.delete_all_cookies()
d.get(site)
d.implicitly_wait(10)
d.set_window_size(1440, 1024)

Location2 = "Мос"
Location3 = "312"
Location4 = "Moscow"


d.find_element(By.XPATH, "/html/body/div[3]/div[1]/header/div[2]/div[1]/div/div/div[3]/div/div/nav/div/table/tbody/tr/td[1]/div/a/div").click()
d.find_element(By.XPATH, "/html/body/div[3]/div[1]/header/div[2]/div[1]/div/div/div[3]/div/div/nav/div/table/tbody/tr/td[1]/div/a/div").click()
d.find_element(By.LINK_TEXT, "Одежда").click()
d.find_element(By.LINK_TEXT, "Рубашка мужская Salomon").click()
d.find_element(By.XPATH, "/html/body/div[3]/div[6]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/span/span").click()
d.find_element(By.LINK_TEXT, "Корзина").click()
d.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div/div/div/div[1]/div[1]/div/div/div[2]/div/div[3]/button").click() # оформить заказ
time.sleep(1)
d.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div/div/div/form/div/div[1]/div[4]/div[2]/div[2]/div/div[2]/div/div[1]/div[4]").click()
print("Error Location1 (empty)",  d.find_element(By.CSS_SELECTOR, "#tooltip-soa-property-6 > div.tooltip-inner").text)

d.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div/div/div/form/div/div[1]/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/input[2]").send_keys(Location2)
print("Error Location2", Location2, d.find_element(By.CSS_SELECTOR, "#tooltip-soa-property-6 > div.tooltip-inner").text)

d.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div/div/div/form/div/div[1]/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/input[2]").send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
d.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div/div/div/form/div/div[1]/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/input[2]").send_keys(Location3)
print("Error Location3", Location3, d.find_element(By.CSS_SELECTOR, "#tooltip-soa-property-6 > div.tooltip-inner").text)

d.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div/div/div/form/div/div[1]/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/input[2]").send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE)
d.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div/div/div/form/div/div[1]/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/input[2]").send_keys(Location4)
print("Error Location4", Location4, d.find_element(By.CSS_SELECTOR, "#tooltip-soa-property-6 > div.tooltip-inner").text)

d.quit()

