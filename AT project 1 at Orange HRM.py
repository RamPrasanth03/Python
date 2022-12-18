from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class  OrangeHRM() :

    def tc_login_01(self):
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
        driver.find_element(By.XPATH, xpath_of_pwd_box).send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("The user is logged in successfully")
        time.sleep(5)
        driver.close()

    def tc_login_02(self):
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
        driver.find_element(By.XPATH, xpath_of_pwd_box).send_keys("Invalid password")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        xpath_of_alert ="//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"
        print(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_of_alert))).text)
        time.sleep(5)
        driver.close()

    def tc_pim_01(self):
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
        time.sleep(5)
        xpath_of_PIM = '//a[@href="/web/index.php/pim/viewPimModule"]'
        driver.find_element(By.XPATH,xpath_of_PIM).click()  # clicking on PIM option in the home page
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@class='oxd-icon-button employee-image-action']").click()
        time.sleep(5)
        xpath_of_firstname = "//input[@name='firstName']"
        driver.find_element(By.XPATH,xpath_of_firstname).send_keys('Ram')
        time.sleep(3)
        xpath_of_middlename = "//input[@name='middleName']"
        driver.find_element(By.XPATH, xpath_of_middlename).send_keys('Prasanth')
        time.sleep(3)
        xpath_of_lastname = "//input[@name='lastName']"
        driver.find_element(By.XPATH, xpath_of_lastname).send_keys('K')
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
        time.sleep(3)
        Xpath_user_name = "//label[text()='Username']/following::div[1]/input"
        driver.find_element(By.XPATH, Xpath_user_name).send_keys("HRMram123")
        time.sleep(3)
        driver.find_element(By.XPATH,"//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']").click()
        time.sleep(3)
        Xpath_User_Password = "//div/label[text()='Password']/following::div[1]/input"
        driver.find_element(By.XPATH, Xpath_User_Password).send_keys("Admin@123")
        time.sleep(3)
        Xpath_Confirm_Password = "//div/label[text()='Confirm Password']/following::div[1]/input"
        driver.find_element(By.XPATH, Xpath_Confirm_Password).send_keys("Admin@123")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        print("Successfully Added Employee details")
        driver.close()

    def tc_pim_02(self):
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
        time.sleep(5)
        xpath_of_PIM = '//a[@href="/web/index.php/pim/viewPimModule"]'
        driver.find_element(By.XPATH, xpath_of_PIM).click()  # clicking on PIM option in the home page
        time.sleep(5)
        driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//div/label[text()='Other Id']/following::div[1]/input").send_keys('1111')
        time.sleep(3)
        driver.find_element(By.XPATH,'// *[ @ id = "app"] / div[1] / div[2] / div[2] / div / div / div / div[2] / div[1] / form / div[2] / div[2] / \
                              div[1] / div / div[2] / input').send_keys(123456)
        driver.find_element(By.XPATH,
                            "//div/label[text()='SSN Number']/following::div[1]/input").send_keys('1111')
        time.sleep(3)
        driver.find_element(By.XPATH,
                            "//div/label[text()='SIN Number']/following::div[1]/input").send_keys('1111')
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        driver.close()

    def tc_pim_03(self):
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
        time.sleep(5)
        xpath_of_PIM = '//a[@href="/web/index.php/pim/viewPimModule"]'
        driver.find_element(By.XPATH, xpath_of_PIM).click()  # clicking on PIM option in the home page
        time.sleep(5)
        driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-trash']").click();
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']").click()
        time.sleep(5)
        driver.close()

go = OrangeHRM()
driver = webdriver.Chrome()
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
go.tc_login_01()
#go.tc_login_02()
#go.tc_pim_01()
#go.tc_pim_02()
#go.tc_pim_03()
