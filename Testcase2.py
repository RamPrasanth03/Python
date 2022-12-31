from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class  OrangeHRM() :

    def tc_pim_02(self):
        driver = webdriver.Chrome()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # open the webpage
        driver.get(url)
        xpath_of_username_box = "//input[@name='username']"
        xpath_of_pwd_box = "//input[@name='password']"
        # maximize the window
        driver.maximize_window()
        time.sleep(5)
        username_box = driver.find_element(By.XPATH, xpath_of_username_box)
        username_box.send_keys("Admin")
        username_box.send_keys(Keys.ENTER)
        pwd_box = driver.find_element(By.XPATH, xpath_of_pwd_box)
        pwd_box.send_keys("admin123")
        pwd_box.send_keys(Keys.ENTER)
        time.sleep(3)
        xpath_of_admin = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        driver.find_element(By.XPATH, xpath_of_admin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[text()='User Management ']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//a[@href="#"]').click()
        time.sleep(2)
        User_Role = driver.find_element(By.XPATH,
                                        "//label[text()='User Role']/following::div[text()='-- Select --'][1]")
        action = ActionChains(driver)
        action.move_to_element(User_Role).click().perform()
        selecting_role = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Admin']")
        action.move_to_element(selecting_role).click().perform()
        time.sleep(3)
        # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]").click()
        # driver.find_element(By.XPATH, "//span[text()='Admin']").click()
        # time.sleep(3)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]").click()
        driver.find_element(By.XPATH, "//span[text()='Enabled']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]").click()
        driver.find_element(By.XPATH, "//span[text()='ESS']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]").click()
        driver.find_element(By.XPATH, "//span[text()='Disabled']").click()
        time.sleep(2)
        driver.close()

go = OrangeHRM()
go.tc_pim_02()
