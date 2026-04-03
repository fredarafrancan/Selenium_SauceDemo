from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_saucedemo():
    # Use local ChromeDriver (must be in PATH)
    driver = webdriver.Chrome()
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Wait and enter username
    username = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    username.clear()
    username.send_keys("standard_user")

    # Wait and enter password
    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.clear()
    password.send_keys("secret_sauce")

    # Click login button
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()

    # Verify login success (inventory page loaded)
    inventory = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Assertion (important!)
    assert inventory.is_displayed(), "Login failed!"

    print("Login successful!")
    time.sleep(20)
    driver.quit()


# Run test
test_login_saucedemo()