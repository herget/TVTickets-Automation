import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

names = [   ["First",   "Last",     "phone",   "email@gmail.com"] ,
            ["First2",  "Last2",    "phone2",   "email@gmail.com"] ]

url = "https://www.tvtickets.com/fmi/tickets/addrecord.php"
showSelectLocator = "/html//select[@id='ShowDateTime']"
formElement= "/html//form[@id='ticketForm']"

class BigBangSearch(unittest.TestCase):

    def setUp(self):
        # define the path of your chromedriver
        self.driver = webdriver.Chrome(executable_path="/Users/YOUR/PATH/chromedriver")

    def test_fill_form(self):
        driver = self.driver
        driver.get(url)
        driver.implicitly_wait(10)        
        
        # refresh the page every 3 secs until 'Bang' found in dropdown
        while True:
            showSelect = Select(driver.find_element_by_xpath(showSelectLocator))
            all_options = showSelect.options
            bigBangFound = False
            for option in all_options:
                if "Dr." in option.text and "STANDBY" not in option.text:
                    bigBangFound = True
                    bigBangWebelementValue = option.get_attribute("value")
                    break

            if bigBangFound is False:
                time.sleep(3)
                driver.refresh()
            else:
                break
            
    
        # fill in forms
        for name in names:
            if driver.current_url != url:
                driver.get(url)

            driver.find_element_by_xpath(showSelectLocator + "/option[@value='" + bigBangWebelementValue + "']").click()
            
            # Number
            numberInput = driver.find_element_by_xpath(formElement + "//input[@name='Number']")
            numberInput.send_keys("1")

            # Firstname
            firstInput = driver.find_element_by_xpath(formElement + "//input[@name='First']")
            print(name[0])
            firstInput.send_keys(name[0])

            # Lastname
            lastInput = driver.find_element_by_xpath(formElement + "//input[@name='Last']")
            lastInput.send_keys(name[1])

            # Phone
            phoneInput = driver.find_element_by_xpath(formElement + "//input[@name='Phone']")
            phoneInput.send_keys(name[2])

            # Email
            emailInput = driver.find_element_by_xpath(formElement + "//input[@name='Email']")
            emailInput.send_keys(name[3])

            # HOW DID YOU FIND US?
            findUsInput = driver.find_element_by_xpath(formElement + "//input[@name='FindUs']")
            findUsInput.send_keys("Internet")

            # Submit
            driver.find_element_by_xpath(formElement + "//input[@id='ticketsubmit']").click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()