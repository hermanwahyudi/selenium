import time, unittest, os, sys
from selenium import webdriver
from main.page.desktop_v3.login.pe_login import *
from main.page.desktop_v3.product.pe_product import *
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_product import *
from utils.function.setup import *
from utils.lib.user_data import *

class TestDebug(unittest.TestCase):
	_site = "live"

	def setUp(self):
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		self.driver = webdriver.Firefox()
		#self.driver = tsetup('phantomjs')
		self.login = loginActivity()
		self.product = ProductActivity()
		self.user = user5

	def test_1_move_to_warehouse(self):
		print('==================================')
		print('TEST : MOVE PRODUCT TO WAREHOUSE')
		print('==================================')
		self.login.do_login(self.driver, self.user, self.user['email'], self.user['password'], self._site)
		self.product.setObject(self.driver)
		self.product.move_product_to_warehouse(self._site, self.user['domain'])

	def test_2_move_to_etalase(self):
		print('==================================')
		print('TEST : MOVE PRODUCT TO ETALASE')
		print('==================================')
		self.login.do_login(self.driver, self.user, self.user['email'], self.user['password'], self._site)
		self.product.setObject(self.driver)
		self.product.move_product_to_etalase(self._site, self.user['domain'])


	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.quit()

# main
if(__name__ == "__main__"):
	unittest.main(warnings="ignore")
