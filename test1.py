from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.set_window_size(990, 695)

driver.get("https://www.amazon.com/")
time.sleep(2)


element = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
element.clear()
element.send_keys("shoe")

element.send_keys(Keys.ENTER)
time.sleep(1)


time.sleep(2)
driver.quit()