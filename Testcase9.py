from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class  OrangeHRM() :

    def tc_pim_09(self):
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
        driver.find_element(By.XPATH, "(//input[@placeholder = 'yyyy-mm-dd'])[1]").send_keys('2011-01-01')
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]").click()
        driver.find_element(By.XPATH, "//span[text()='Chief Financial Officer']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]").click()
        driver.find_element(By.XPATH, "//span[text()='Craft Workers']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[3]").click()
        driver.find_element(By.XPATH, "//span[text()='Quality Assurance']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[4]").click()
        driver.find_element(By.XPATH, "//span[text()='Canadian Regional HQ']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[5]").click()
        driver.find_element(By.XPATH, "//span[text()='Freelance']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//input[@placeholder = 'yyyy-mm-dd'])[2]").send_keys('2011-01-01')
        time.sleep(2)
        driver.find_element(By.XPATH, "(//input[@placeholder = 'yyyy-mm-dd'])[3]").send_keys('2015-01-01')
        time.sleep(2)
        upload_file = driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-upload oxd-file-input-icon']")
        upload_file.click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(10)
        driver.close()


go = OrangeHRM()
go.tc_pim_09()