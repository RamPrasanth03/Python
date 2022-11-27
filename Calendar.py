from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class CalendarSelection():

    def select_dates_on_caledar(self):
        """
    1. open Expedia.com - done
    2. switch to flight tab - done
    3. switch to one-way tab - done
    4. open calendar - done
    5. click on a specific date - done

            """

    driver = webdriver.Firefox()

    baseurl = "https://www.expedia.com/"

    # open the website
    driver.get(baseurl)

    # maximize the window
    driver.maximize_window()
    time.sleep(4)
    # switch to flights tab
    xpath_to_flight_tab = "//a[@href='?pwaLob=wizard-flight-pwa']"
    flight_tab_element = driver.find_element(By.XPATH, xpath_to_flight_tab)
    flight_tab_element.click()

    time.sleep(4)
    # switch to one tab on flights
    xpath_to_onewaay_tab = "//a[@href='?flightType=oneway']"
    one_way_tab_element = driver.find_element(By.XPATH, xpath_to_onewaay_tab)
    one_way_tab_element.click()

    time.sleep(4)
    # switching to select a date on the tab for this calendar
    xpath_to_departing_tab = "//button[@id='d1-btn']"
    departing_cal_button = driver.find_element(By.ID, 'd1-btn')
    departing_cal_button.click()

    time.sleep(4)
    # switching to select current day ,date
    calMonth = driver.find_element(By.XPATH, "(//div[@class='uitk-date-picker-month'])[1]")  # the month october
    xpath_to_oct_8 = "//button[@data-day='8']"
    current_date_button = calMonth.find_element(By.XPATH, xpath_to_oct_8)
    current_date_button.click()

    # practice
    # to find the list of dates that are disabled in the current month and print it
    # this will utilise get_attribute method and concept of lists
    # expected output --- [1,2,3,4,5,6,7]

    time.sleep(10)

    driver.quit()


ab = CalendarSelection()
ab.select_dates_on_caledar()
