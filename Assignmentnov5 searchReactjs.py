from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class  BrowesrInteractions() :
    def test(self):
        driver = webdriver.Chrome()
        url1 = "https://reactjs.org/"

    # open the webpage
        driver.get(url1)
    # maximize the window
        driver.maximize_window()
        xpath_of_search_box = "//input[@placeholder='Search']"
        driver.find_element(By.XPATH, xpath_of_search_box).send_keys("abc")
        time.sleep(3)
        driver.find_element(By.XPATH,
                                   "//div[@class='algolia-docsearch-suggestion--content']"
                                   "/div[@class='algolia-docsearch-suggestion--subcategory-inline']"
            .get_attribute('innerText'))
gc = BrowesrInteractions()
gc.test()
