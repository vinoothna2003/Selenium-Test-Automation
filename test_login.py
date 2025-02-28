import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Initialize Chrome
    driver.get("https://www.saucedemo.com/")  # Open website
    yield driver  # Return driver instance
    driver.quit()  # Close browser after test

def test_login_success(setup):
    driver = setup

    # Enter username & password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click login button
    driver.find_element(By.ID, "login-button").click()

    # Verify successful login
    assert "inventory.html" in driver.current_url, "Login failed!"

