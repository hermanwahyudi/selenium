from main.page.pe_login import test_user_login
from main.page.pe_createshop import goto_createshop_page
from main.lib.user_data import *
from selenium import webdriver
import time
import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def test_createshop(self):
        driver = self.driver
        email = user7['email']
        pwd = user7['pwd']
        test_user_login(driver,email,pwd)
        goto_createshop_page(driver)
        time.sleep(5)
        #test_user_logout(driver)



    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        time.sleep(5)
        #self.driver.close()

if __name__ == '__main__':
    unittest.main()