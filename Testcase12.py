from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class  OrangeHRM() :

    def tc_pim_12(self):
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
        driver.find_element(By.XPATH,"//a[contains( @ href, '/viewSalaryList')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--text']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='Salary Component']/following::div[1]/input").send_keys('457')
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]").click()
        driver.find_element(By.XPATH, "//span[text()='Grade 2']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]").click()
        driver.find_element(By.XPATH, "//span[text()='Monthly']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[3]").click()
        driver.find_element(By.XPATH, "//span[text()='United States Dollar']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='Amount']/following::div[1]/input").send_keys('45657')
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='Comments']/following::div[1]/textarea").send_keys('yyyy')
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,
                            "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//div/label[text()='Account Number']/following::div[1]/input").send_keys('75464')
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[4]").click()
        driver.find_element(By.XPATH, "//span[text()='Checking']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/label[text()='Routing Number']/following::div[1]/input").send_keys('7974')
        time.sleep(2)
        driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[5]").send_keys('123567')
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--text']").click()
        time.sleep(5)
        driver.close()


go = OrangeHRM()
go.tc_pim_12()