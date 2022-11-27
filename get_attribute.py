from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class GetAttributeTrial():
    def  test_1(self) :
        """
        get the text of any element
        :return:
        """
        driver = webdriver.Firefox()
        url_of_webpage = "https://courses.letskodeit.com/practice"
        url_of_amazon = ""
        id_of_bmwradio_button =  "bmwradio"

        # open the webpage
        driver.get(url_of_webpage)
        driver.maximize_window()
        time.sleep(5)

        # save screenshot
        filename_trail = 'C:\\Users\\LENOVO\\Desktop\\Guvi_batch_01_10_2022\\ss.png'
        driver.save_screenshot(filename_trail)

        # find the element
        # bmwradioelement = driver.find_element(By.ID ,id_of_bmwradio_button )

        # # get the text of element identified
        # text_of_bmw_element  = bmwradioelement.text
        # print(f"the text of lement is : " + text_of_bmw_element )
        #  # get attribute of any element
        # attribute_of_element = bmwradioelement.get_attribute('names')
        # print(f"the name of element is : " + attribute_of_element )
        driver.quit()
gc = GetAttributeTrial()
gc.test_1()
