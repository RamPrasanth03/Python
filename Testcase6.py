from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class  OrangeHRM() :

    def tc_pim_06(self):
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
        time.sleep(2)
        xpath_of_PIM = '//a[@href="/web/index.php/pim/viewPimModule"]'
        driver.find_element(By.XPATH, xpath_of_PIM).click()  # clicking on PIM option in the home page
        time.sleep(2)
        driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[contains( @ href, '/contactDetail')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='Street 1']/following::div[1]/input").send_keys('xxxx')
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='Street 2']/following::div[1]/input").send_keys('yyyy')
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='City']/following::div[1]/input").send_keys('yyyy')
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='State/Province']/following::div[1]/input").send_keys('yyyy')
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='Zip/Postal Code']/following::div[1]/input").send_keys('123456')
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]").click()
        driver.find_element(By.XPATH, "//span[text()='Algeria']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='Home']/following::div[1]/input").send_keys(
            '123456')
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='Mobile']/following::div[1]/input").send_keys(
            '123456')
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='Work']/following::div[1]/input").send_keys(
            '123456')
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='Work Email']/following::div[1]/input").send_keys(
            'test1@abc.com')
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='Other Email']/following::div[1]/input").send_keys(
            'test2@abc.com')
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        driver.close()


go = OrangeHRM()
go.tc_pim_06()