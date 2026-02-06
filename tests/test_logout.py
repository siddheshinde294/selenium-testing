from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logout():
    driver = webdriver.Chrome()
    
    try:
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com")
        
        wait = WebDriverWait(driver, 10)
        
        # Login first
        username = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username.send_keys("Admin")
        
        password = driver.find_element(By.NAME, "password")
        password.send_keys("admin123")
        
        login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_btn.click()
        
        # Verify Dashboard (login successful)
        dashboard = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )
        assert dashboard.is_displayed()
        
        # Click on user dropdown (top-right corner)
        user_dropdown = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab"))
        )
        user_dropdown.click()
        
        # Click logout option
        logout_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
        )
        logout_link.click()
        
        # Verify redirect to login page (logout successful)
        login_heading = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h5[text()='Login']"))
        )
        assert login_heading.is_displayed()
        
        print("✅ Logout test passed!")
    
    finally:
        # Always cleanup - whether test passes or fails
        driver.quit()