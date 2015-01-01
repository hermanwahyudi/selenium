from page.pe_login import *
from main.page.pe_inbox_talk import goto_inbox_talk
from main.page.pe_inbox_review import goto_inbox_review
from selenium import webdriver
from lib.user_data import user3
from page.base import *
from page.header import *
from page.pe_index import *
import time
import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        #chromedriver= "D:\Python34\Scripts\chromedriver"
        #self.driver = webdriver.Chrome(chromedriver)    #Set Chromedriver
        self.driver = webdriver.Firefox()                      #Set Firefoxdriver
        self.driver.implicitly_wait(10)

    def test_1_login_success(self):
        print ("TEST #1 : Login Success")
        driver = self.driver

        email = user3['email']
        pwd = user3['pwd']
        h_flag = test_user_login(driver, email, pwd)
        time.sleep(2)
        #goto_inbox_review(driver)
        now_at_index(driver)
        check_header_status(driver,h_flag)
        #now_at_index(driver)
        test_user_logout(driver)

    # def test_2_login_validation_input_empty(self):
    #     print ("TEST #2 : [Validation] Login Empty")
    #
    #     check_validasi_login_input_empty(self.driver)
    #     test_user_logout(self.driver)
    #
    # def test_3_login_validation_input_email(self):
    #     print ("TEST #3 : [Validation] Input Email")
    #
    #     email = user3['email']
    #     check_validasi_input_email(self.driver,email)
    #     test_user_logout(self.driver)
    #
    # def test_4_login_validation_input_password(self):
    #     print ("TEST #4 : [Validation] Input Password")
    #
    #     pwd = user3['pwd']
    #     check_validasi_input_password(self.driver,pwd)
    #     test_user_logout(self.driver)



    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()




