from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class  OrangeHRM() :

    def tc_pim_03(self):
        driver = webdriver.Chrome()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # open the webpage
        driver.get(url)
        xpath_of_username_box = "//input[@name='username']"
        xpath_of_pwd_box = "//input[@name='password']"
        # maximize the window
        driver.maximize_window()
        time.sleep(2)
        username_box = driver.find_element(By.XPATH, xpath_of_username_box)
        username_box.send_keys("Admin")
        username_box.send_keys(Keys.ENTER)
        pwd_box = driver.find_element(By.XPATH, xpath_of_pwd_box)
        pwd_box.send_keys("admin123")
        pwd_box.send_keys(Keys.ENTER)
        time.sleep(5)
        xpath_of_PIM = '//a[@href="/web/index.php/pim/viewPimModule"]'
        driver.find_element(By.XPATH, xpath_of_PIM).click()  # clicking on PIM option in the home page
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
        time.sleep(2)
        xpath_of_firstname = "//input[@name='firstName']"
        driver.find_element(By.XPATH, xpath_of_firstname).send_keys('Ram')
        time.sleep(2)
        xpath_of_middlename = "//input[@name='middleName']"
        driver.find_element(By.XPATH, xpath_of_middlename).send_keys('Prasanth')
        time.sleep(2)
        xpath_of_lastname = "//input[@name='lastName']"
        driver.find_element(By.XPATH, xpath_of_lastname).send_keys('K')
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
        time.sleep(2)
        Xpath_user_name = "//label[text()='Username']/following::div[1]/input"
        driver.find_element(By.XPATH, Xpath_user_name).send_keys("HRM02")
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']").click()
        time.sleep(2)
        Xpath_User_Password = "//div/label[text()='Password']/following::div[1]/input"
        driver.find_element(By.XPATH, Xpath_User_Password).send_keys("Admin@123")
        time.sleep(2)
        Xpath_Confirm_Password = "//div/label[text()='Confirm Password']/following::div[1]/input"
        driver.find_element(By.XPATH, Xpath_Confirm_Password).send_keys("Admin@123")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        xpath_of_EmployeeList = '//a[@href="#"]'
        driver.find_element(By.XPATH, xpath_of_EmployeeList).click()
        time.sleep(5)
        print("Successfully Added Employee details")
        driver.close()

go = OrangeHRM()
go.tc_pim_03()