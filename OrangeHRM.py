import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BrowesrInteractions:
    def test(self):
        driver = webdriver.Chrome()  # intializes the driver object
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')  # opening the website
        driver.maximize_window()  # maximizes the window
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys('Admin')  # Entering username
        password = driver.find_element(By.XPATH,
                                   "//input[@placeholder='Password']")  # locating the input field for password
        password.send_keys('admin123')  # Entering the password
        password.send_keys(Keys.ENTER)  # Entering the Enter Key
        time.sleep(5)
        driver.find_element(By.XPATH,
                        '//a[@href="/web/index.php/admin/viewAdminModule"]').click()  # clicking on admin option in the home page
        driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
        #driver.find_element(By.XPATH, "//button[@type='submit']").click()
        User_Role = driver.find_element(By.XPATH,
                                    "//label[text()='User Role']/following::div[1]/div/div/div[text()='-- Select --']")
        action = ActionChains(driver)
        ActionChains(driver).move_to_element(User_Role).click().perform()
        # ActionChains(driver).move_to_element(User_Role).perform().send_keys(Keys.PAGE_DOWN)
        selecting_role = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Admin']")
        ActionChains(driver).move_to_element(selecting_role).click().perform()
        Status = driver.find_element(By.XPATH,
                                 "//label[text()='Status']/following::div[1]/div/div/div[text()='-- Select --']")
        ActionChains(driver).move_to_element(Status).click().perform()
        Status_option = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Enabled']")
        ActionChains(driver).move_to_element(Status_option).click().perform()
        Employee_name = driver.find_element(By.XPATH,
                                        "//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']/input").send_keys(
        "Odis")
        Selecting_Employee_name = "//span[text()='Odis  Adalwin']"
        wait = WebDriverWait(driver, 5)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Selecting_Employee_name)))
        driver.find_element(By.XPATH, "//span[text()='Odis  Adalwin']").click()
        input_name = input("enter the name:")
        input_user_name = "//label[text()='Username']/following::div[1]/input"
        driver.find_element(By.XPATH, input_user_name).send_keys(input_name)
        input_password = "//div/label[text()='Password']/following::div[1]/input"
        driver.find_element(By.XPATH, input_password).send_keys("Admin@123")
        input_password = "//div/label[text()='Confirm Password']/following::div[1]/input"
        driver.find_element(By.XPATH, input_password).send_keys("Admin@123")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        ver_string = driver.find_element(By.XPATH,'//div/label[text()="Username"]/following::div[1]/input')
        ver_string.send_keys(input_name)
        ver_string.send_keys(Keys.ENTER)
        time.sleep(15)
        driver.find_element(By.XPATH,'//span[text()="(1) RecordFound"]')
gc = BrowesrInteractions()
gc.test()