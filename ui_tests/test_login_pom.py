import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("--headless")
    d = webdriver.Chrome(options=options)
    yield d
    d.quit()


def test_valid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.enter_username("tomsmith")
    page.enter_password("SuperSecretPassword!")
    page.click_login()
    assert "success" in page.get_flash_class()

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.enter_username("tomm")
    page.enter_password("SuperSecretPassword!")
    page.click_login()
    assert "error" in page.get_flash_class()