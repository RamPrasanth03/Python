from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
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
        #Admintab
        driver.find_element(By.XPATH,'//a[@href="/web/index.php/admin/viewAdminModule"]').click()
        #driver.find_element(By.XPATH,"//span[text()='Admin']").click()
        time.sleep(5)
        #Add button
        driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
        time.sleep(5)

        xpath_of_employee_box = "//input[@placeholder='Type for hints...']"
        driver.find_element(By.XPATH, xpath_of_employee_box).send_keys("ram123")
        time.sleep(5)
gc = BrowesrInteractions()
gc.test()
