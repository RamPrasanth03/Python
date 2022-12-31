from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class  OrangeHRM() :

    def tc_pim_10(self):
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
        driver.find_element(By.XPATH,"//a[contains( @ href, '/viewJobDetails')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"(//button[@class='oxd-button oxd-button--medium oxd-button--label-danger --termination-button'])").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//input[@placeholder = 'yyyy-mm-dd'])[2]").send_keys('2011-01-01')
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[6]").click()
        driver.find_element(By.XPATH, "//span[text()='Contract Not Renewed']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, ' // *[ @ id = "app"] / div[1] / div[2] / div[2] / div / div / div / div[2] / div[3] / div / div / div / form / \
                              div[4] / button[2]').click()

        time.sleep(10)
        driver.close()


go = OrangeHRM()
go.tc_pim_10()