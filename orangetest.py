from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class  BrowesrInteractions() :
    def test(self):
        driver = webdriver.Chrome()
        # meaningful variables and comment code as a habit
        url1 = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        xpath_of_username_box = "//input[@name='username']"
        xpath_of_pwd_box = "//input[@name='password']"
    # open the webpage
        driver.get(url1)
    # maximize the window
        driver.maximize_window()
        time.sleep(5)
    # write the string to search in the query box
        username_box = driver.find_element(By.XPATH, xpath_of_username_box)
        username_box.send_keys("Admin")
        username_box.send_keys(Keys.ENTER)
        pwd_box = driver.find_element(By.XPATH, xpath_of_pwd_box)
        pwd_box.send_keys("admin123")
        pwd_box.send_keys(Keys.ENTER)
        time.sleep(3)
        Xpath_Admin_tab = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        driver.find_element(By.XPATH, Xpath_Admin_tab).click()
        time.sleep(3)
        Xpath_Add_tab = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        driver.find_element(By.XPATH, Xpath_Add_tab).click()
        time.sleep(3)

        User_Role = driver.find_element(By.XPATH,
                                        "//label[text()='User Role']/following::div[text()='-- Select --'][1]")
        action = ActionChains(driver)
        action.move_to_element(User_Role).click().perform()
        selecting_role = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Admin']")
        action.move_to_element(selecting_role).click().perform()
        time.sleep(3)
        driver.find_element(By.XPATH,
                            "//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']/input").send_keys(
            "Paul")
        Employee_name = "//span[text()='Paul']"
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Employee_name)))
        driver.find_element(By.XPATH, "//span[text()='Paul Collings']").click()

        status = driver.find_element(By.XPATH, "//label[text()='Status']/following::div[text()='-- Select --'][1]")
        action = ActionChains(driver)
        ActionChains(driver).move_to_element(status).click().perform()
        selecting_status = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Enabled']")
        action.move_to_element(selecting_status).click().perform()
        time.sleep(3)

        Xpath_user_name = "//label[text()='Username']/following::div[1]/input"
        driver.find_element(By.XPATH, Xpath_user_name).send_keys("Ram1234")
        time.sleep(3)

        Xpath_User_Password = "//div/label[text()='Password']/following::div[1]/input"
        driver.find_element(By.XPATH, Xpath_User_Password).send_keys("Admin@123")
        time.sleep(3)

        Xpath_Confirm_Password = "//div/label[text()='Confirm Password']/following::div[1]/input"
        driver.find_element(By.XPATH, Xpath_Confirm_Password).send_keys("Admin@123")
        time.sleep(5)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

go = BrowesrInteractions()
go.test()
