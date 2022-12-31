from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class  OrangeHRM() :

    def tc_pim_01(self):
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
        driver.find_element(By.XPATH, xpath_of_pwd_box).send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        list_of_menuitems = []
        menu_display = driver.find_elements(By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']")
        for i in menu_display:
            list_of_menuitems.append(i.text)
        print(list_of_menuitems)
        search_button = driver.find_element(By.XPATH,"//input[@placeholder='Search']")
        for a in list_of_menuitems:
            search_button.send_keys(a.upper())
            time.sleep(1)
            search_button.send_keys(Keys.CONTROL,'a')
            search_button.send_keys(Keys.BACKSPACE)
        for b in list_of_menuitems:
            search_button.send_keys(b.lower())
            time.sleep(1)
            search_button.send_keys(Keys.CONTROL,'a')
            search_button.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        driver.close()

go = OrangeHRM()
go.tc_pim_01()
