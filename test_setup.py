from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
print(driver.title)
driver.quit()
