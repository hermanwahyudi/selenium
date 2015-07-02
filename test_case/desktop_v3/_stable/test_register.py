
import unittest, platform, sys, os
import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from main.activity.desktop_v3.activity_register import registerActivity
from main.page.base import *
from main.page.desktop_v3.header import *
from utils.function.setup import *
from utils.function.logger import *

fullname = "Mirehehe Hahaha"
phone = "081394859148"
gender = "Female"
email = "tkpd.qc+29@gmail.com"
passwd = "12345678"
conf_passwd = "12345678"
check_tos = "yes"



class TokopediaRegister(unittest.TestCase):

	dict = {
		"site" : "live",
		"loop" : 5,
		"inc" : 800000,
		"name" : "name",
		"phone" : "085780548872",
		"gender" : "Male",
		"prefix_email" : "tkpd.qc+",
		"password" : "1234asdf",
		"confirm_password" : "1234asdf",
		"check_tos" : "yes"
	}

	def setUp(self):
		#self.driver = webdriver.Firefox()
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		self.driver = tsetup('chrome')
		self.obj = registerActivity(self.driver)
		#sys.stdout = Logger() #function to create log file

	def test_loop_register(self):
		print("Automation register loop!")
		self.obj.set_param(self.dict)
		self.obj.loop_reg(self.dict['loop'])

	"""def test_fill_registration_form(self):
		print('================================')
		print('TEST CASE #1 : REGISTRASI NORMAL')
		print('================================')
		driver = self.driver
		#object activity
		register = registerActivity()
		register.test_do_register(driver, fullname, phone, gender, email, passwd, conf_passwd, check_tos)"""
	"""
	def test_check_error_message_case1(self):
		print('======================================================')
		print('TEST CASE #2 : CHECK ERROR MESSAGE IF ALL FIELD = NULL')
		print('======================================================')
		driver = self.driver
		register = registerActivity(driver)
		register.check_validasi_input_null(driver)"""

	"""def test_link_register_via_fb(self):
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
		register.check_link_register_via_google(driver)"""
	
	

	def tearDown(self):
		print("")
		self.driver.quit()

if __name__ == "__main__":
	unittest.main(warnings='ignore')

	#test