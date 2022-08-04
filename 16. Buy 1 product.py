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

d.find_element(By.XPATH, "/html/body/div[3]/div[1]/header/div[2]/div[1]/div/div/div[3]/div/div/nav/div/table/tbody/tr/td[1]/div/a/div").click()
d.find_element(By.XPATH, "/html/body/div[3]/div[1]/header/div[2]/div[1]/div/div/div[3]/div/div/nav/div/table/tbody/tr/td[1]/div/a/div").click()
d.find_element(By.LINK_TEXT, "Одежда").click()
d.find_element(By.LINK_TEXT, "Рубашка мужская Salomon").click()
d.find_element(By.XPATH, "/html/body/div[3]/div[6]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/span/span").click()
d.find_element(By.LINK_TEXT, "Корзина").click()
d.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div/div/div/div[1]/div[1]/div/div/div[2]/div/div[3]/button").click() # оформить заказ
d.find_element(By.CSS_SELECTOR, "#bx-soa-region > div.bx-soa-section-content.container-fluid > div.row.bx-soa-more > div > a").click() # Далее
d.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[2]/div/div/div/form/div/div[1]/div[5]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]").click() # Самовывоз
time.sleep(1.5)
d.find_element(By.CSS_SELECTOR, "#bx-soa-delivery > div.bx-soa-section-content.container-fluid > div.row.bx-soa-more > div > a.pull-right.btn.btn-default.btn-md").click() # Далее
d.find_element(By.CSS_SELECTOR, "#bx-soa-paysystem > div.bx-soa-section-content.container-fluid > div.bx-soa-pp.row > div.col-sm-7.bx-soa-pp-item-container > div:nth-child(2) > div.bx-soa-pp-company-graf-container > div").click()
time.sleep(1.5)
d.find_element(By.CSS_SELECTOR, "#bx-soa-paysystem > div.bx-soa-section-content.container-fluid > div.row.bx-soa-more > div > a.pull-right.btn.btn-default.btn-md").click() # Далее
d.find_element(By.NAME, "ORDER_PROP_1").send_keys("Фамилия")
d.find_element(By.NAME, "ORDER_PROP_2").send_keys("email@email.com", Keys.TAB)
ActionChains(d) \
    .send_keys("4951234567") \
    .perform()
d.find_element(By.NAME, "ORDER_PROP_7").send_keys("Москва, ул. Новый Арбат, 14")
d.find_element(By.CSS_SELECTOR, "#bx-soa-properties > div.bx-soa-section-content.container-fluid > div.row.bx-soa-more > div > a.pull-right.btn.btn-default.btn-md").click() # Далее
wait = WebDriverWait(d, 20)
original_window = d.current_window_handle # Первое окно
d.find_element(By.CSS_SELECTOR, "#bx-soa-order > div.col-sm-9.bx-soa > div.form > div > div > label.license").click() #checkbox
wait.until(EC.number_of_windows_to_be(2)) # Ожидаем загрузки второго окна
for window_handle in d.window_handles: # Перебираем до тех пор, пока не найдем новый дескриптор окна
        if window_handle != original_window:
            d.switch_to.window(window_handle)
            break
wait.until(EC.url_to_be("http://test2.itcobra.ru/include/licenses_detail.php")) # Дождитесь завершения загрузки содержимого на новой вкладке
d.switch_to.window(original_window) # Переходим в первое окно
d.find_element(By.CSS_SELECTOR, "#bx-soa-orderSave > a").click() # Оформить заказ
d.find_element(By.NAME, "BuyButton").click()