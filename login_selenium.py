from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.clear()
password_field.clear()

username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPssword!")

button = driver.find_element(By.CSS_SELECTOR, "button.radius")
button.click()

time.sleep(1)

flash_element = driver.find_element(By.ID, "flash")
flash_class = flash_element.get_attribute("class")

if "success" in flash_class:
    print("Login succeeded")
else:
    print("Login failed")