from page.pe_login import *
from page.pe_add_product import *
from selenium import webdriver
from lib.user_data import user3
import time
import unittest

class TestAddProduct(unittest.TestCase):
    def setUp(self):
        #chromedriver= "D:\Python34\Scripts\chromedriver"
        #self.driver = webdriver.Chromedriver(chromedriver)    #Set Chromedriver
        self.driver = webdriver.Firefox() 
        self.addProduct = addProduct(self.driver)                     #Set Firefoxdriver
        self.driver.implicitly_wait(10)


    # def test_1_add_product_validation_input_empty(self):
    #     print ("TEST #1 : [Validation] Add Product Empty")
    #     driver = self.driver
    #     email = "tkpd.qc+18@gmail.com"
    #     pwd = "imtokopedia91"
    #     test_user_login(driver,email,pwd)
    #     check_validasi_add_product_empty(self.driver)
    #     time.sleep(5)
    #     test_user_logout(self.driver)

    def test_2_add_product(self):
        print ("TEST #2 : Add Product")
        driver = self.driver
        email = "tkpd.qc+18@gmail.com"
        pwd = "imtokopedia91"
        test_user_login(driver,email,pwd)
        self.addProduct.go_to_add_product()
        self.addProduct.add_to_product()
   

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()