from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class CloseQuit() :
    def test_close(self):
        """
        I want to test the close method of selenium webdriver
        on google.com
        default  :  Closes the current window.
        :return:
        """
        baseUrl = "http://www.google.com"
        driver = webdriver.Chrome()
        #maximize window
        driver.maximize_window()
        driver.get(baseUrl)
        time.sleep(5)
        # close method
        driver.close()
    def test_quit(self):
        """
                I want to test the quit method of selenium webdriver
                on google.com
                Closes the browser and shuts down the ChromiumDriver executable
                :return:
                """
        baseUrl = "http://www.google.com"
        driver = webdriver.Firefox()
        # maximize window
        driver.maximize_window()
        driver.get(baseUrl)
        time.sleep(5)
        # close method
        driver.quit()
ab = CloseQuit()
ab.test_quit()
# ab.test_close()
