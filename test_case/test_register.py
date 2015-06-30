
import unittest, platform
import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from main.activity.activity_register import registerActivity
from main.page.base import *
from main.page.header import *
from main.function.setup import *

fullname = "Mirehehe Hahaha"
phone = "081394859148"
gender = "Female"
email = "tkpd.qc+29@gmail.com"
passwd = "12345678"
conf_passwd = "12345678"
check_tos = "yes"



class TokopediaRegister(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
        self.driver = tsetup()

    def test_fill_registration_form(self):
        print('================================')
        print('TEST CASE #1 : REGISTRASI NORMAL')
        print('================================')
        driver = self.driver
        #object activity
        register = registerActivity()
        register.test_do_register(driver, fullname, phone, gender, email, passwd, conf_passwd, check_tos)

    def test_check_error_message_case1(self):
        print('======================================================')
        print('TEST CASE #2 : CHECK ERROR MESSAGE IF ALL FIELD = NULL')
        print('======================================================')
        driver = self.driver
        register = registerActivity()
        register.check_validasi_input_null(driver)

    def test_link_register_via_fb(self):
        print('======================================')
        print('TEST CASE #3 : REGISTRASI VIA FACEBOOK')
        print('======================================')
        driver = self.driver
        register = registerActivity()
        register.check_link_register_via_fb(driver)

    def test_link_register_via_google(self):
        print('======================================')
        print('TEST CASE #4 : REGISTRASI VIA GOOGLE+')
        print('======================================')
        driver = self.driver
        register = registerActivity()
        register.check_link_register_via_google(driver)
    
	

    def tearDown(self):
    	self.driver.quit()

if __name__ == "__main__":
	unittest.main(warnings='ignore')

    #test