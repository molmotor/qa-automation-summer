from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def enter_username(self, username):
        field = self.driver.find_element(By.ID, "username")
        field.send_keys(username)

    def enter_password(self, password):
        field = self.driver.find_element(By.ID, "password")
        field.send_keys(password)

    def click_login(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "button.radius")
        button.click()

    def get_flash_class(self):
        flash_element = self.driver.find_element(By.ID, "flash")
        return flash_element.get_attribute("class")