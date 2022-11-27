from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

"""
 wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID,
                                                         "stopFilter_stops-0")))
"""

class ExplicitExample():
    def test(self):
        driver = webdriver.Chrome()

        # Defing url
        url_omayo4 = "http://omayo.blogspot.com/"
        url_letskodeit = "https://courses.letskodeit.com/practice"

        # open the webpage
        driver.get(url_letskodeit)

        # maximize the window
        driver.maximize_window()
        #clicking on the courses page
        course_page_link = "//a[@href='/courses']"
        courses_page_element = driver.find_element(By.XPATH,course_page_link)
        courses_page_element.click()

        # search course
        search_bar_id = "search"
        search_bar_element = driver.find_element(By.ID,search_bar_id)
        string_to_pass = "Javascript"
        search_bar_element.click()
        # search_bar_element.send_keys(string_to_pass)
        # time.sleep(5)

        #javascript
        javscript_xpath = "//h4[1]"

        """
            wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])"""

        wait_for_element1 = WebDriverWait(driver,10,1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException,
                                                 ElementNotInteractableException,
                                                 TimeoutException])


        """
        element = wait.until(EC.element_to_be_clickable((By.ID,
                                                         "stopFilter_stops-0")))
        """
        # waiting until the javascript element is clickable


        javscript_element = wait_for_element1.until(EC.element_to_be_clickable((By.XPATH,javscript_xpath)))

        javscript_element.click()

        print("The title of page is "+ driver.title)

        time.sleep(4)

        driver.quit()

go = ExplicitExample()
go.test()