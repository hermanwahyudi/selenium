from main.activity.activity_forgot_password import *
from main.page.forgot_password.pe_forgot_password import *
from main.lib.user_data import *
from selenium import webdriver
import time
import unittest

#locator path
input_email = "tkpd.qc+10@gmail.com"

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.fp = ForgotPasswordActivity()

    def test_forgot_password(self):
        driver = self.driver
        self.fp.goto_fpsw_page(driver, input_email)

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        time.sleep(5)
        #self.driver.close()

if __name__ == '__main__':
    unittest.main()