from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class  BrowesrInteractions() :
    def test(self):
        """
        open google and search for a string  : guvi
        :return:
        """
        driver = webdriver.Chrome()
        # meaningful variables and comment code as a habit
        url1 = "https://www.google.com/"
        xpath_of_google_searchbox = "//input[@name='q']"
    # open the webpage
        driver.get(url1)
    # maximize the window
        driver.maximize_window()
        time.sleep(5)
    # write the string to search in the query box
        search_box = driver.find_element(By.XPATH, xpath_of_google_searchbox)
        search_box.send_keys("indian cricket team")
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)
        count = driver.find_elements(By.XPATH, "//a[@href]")
        for i in count:
            print(i.get_attribute("href"))

gc = BrowesrInteractions()
gc.test()

