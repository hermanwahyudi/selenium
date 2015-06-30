from page.pe_login import *
from page.pe_people import *
from selenium import webdriver
from lib.user_data import user3
import time
import unittest

class TestEditPeople(unittest.TestCase):
    def setUp(self):
        #chromedriver= "D:\Python34\Scripts\chromedriver"
        #self.driver = webdriver.Chromedriver(chromedriver)    #Set Chromedriver
        self.driver = webdriver.Firefox() 
        self.peoplePage = peoplePage(self.driver)                     #Set Firefoxdriver
        self.driver.implicitly_wait(10)


    def test_1_edit_tab_1_personal_profile(self):
        print ("TEST #1 : Tab 1 Personal Profile")
        driver = self.driver
        email = "tkpd.qc+18@gmail.com"
        pwd = "imtokopedia91"
        test_user_login(driver,email,pwd)
        self.peoplePage.go_to_people_page()
        self.peoplePage.go_to_edit_people_page()
        # self.peoplePage.edit_personal_profile()
        # self.peoplePage.edit_password()
        # self.peoplePage.search_address()
        self.peoplePage.add_new_address()
        time.sleep(5)

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()