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
        driver = webdriver.Firefox()
        # meaningful variables and comment code as a habit
        url1 = "https://www.google.com/"
        xpath_of_google_searchbox = "//input[@name='q']"
        xpath_of_google_searchbutton = '//input[@aria-label="Google Search"]'
    # open the webpage
        driver.get(url1)
    # maximize the window
        driver.maximize_window()
        time.sleep(5)
    # write the string to search in the query box
        search_box = driver.find_element(By.XPATH, xpath_of_google_searchbox)
        search_box.send_keys("guvi")
    # click the search icon
    #     search_icon_element = driver.find_element(By.XPATH,xpath_of_google_searchbutton)
    #     search_icon_element.click()
    # press the enter keys
        search_box.send_keys(Keys.ENTER)
        time.sleep(10)
     # get the current url of page
        curren_url = driver.current_url
        print(f"The current url of page is : " + curren_url)
    # refreshes the page
        time.sleep(5)
        driver.refresh()
    # refresh the page using second method
        time.sleep(5)
        driver.get(curren_url)
        driver.quit()
gc = BrowesrInteractions()
gc.test()
