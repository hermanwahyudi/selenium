from main.activity.activity_login import *
from main.page.add_product.pe_add_product import *
from selenium import webdriver
import time
import unittest

class TestAddProduct(unittest.TestCase):

    _site = "live"

    # dictionary user
    dict_user = {
        "email_buyer" : "tkpd.qc+35@gmail.com",
        "password_buyer" : "123456789",
        "email_seller" : "tkpd.qc+36@gmail.com",
        "password_seller" : "123456789"
    }

    def setUp(self):
        self.driver = webdriver.Firefox() 
        self.addProduct = addProduct(self.driver)
        self.driver.implicitly_wait(10)
        self.login = LoginPage(self.driver)

    def test_1_add_product(self):
        print ("TEST #1 : Add Product")
        driver = self.driver
        self.login.open(self._site)
        self.login.do_login(self.dict_user['email_buyer'], self.dict_user['password_buyer'])
        self.addProduct.open(self._site)

        ####### comment dan uncomment untuk mengganti-ganti test case di bawah ini #######
        self.addProduct.action_add_product(2, self._site)
        #self.addProduct.action_add_product_catalog(2, self._site)

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()