import time, os, sys, unittest
from selenium import webdriver
from main.activity.activity_deposit import *
from main.activity.activity_login import *
from main.function.setup import *


class testDeposit(unittest.TestCase):
	_site = 'live'

	dict_user = {
		"email" : "tkpd.qc+29a@gmail.com",
		"password" : "cumicumi"
	}

	def setUp(self):
		self.driver = tsetup('phantomjs')
		self.login = loginActivity()
		self.deposit = depositActivity()

	def test_1_status_deposit(self):
		print('===================================')
		print('TEST #1 : CHECK STATUS DEPOSIT')
		print('===================================')
		self.login.do_login(self.driver, self.dict_user['email'], self.dict_user['password'], self._site)
		self.deposit.check_deposit_details(self.driver, self._site)
		print('Test Selesai')


	def tearDown(self):
		print('Testing akan selesai dalam beberapa saat...')
		self.driver.quit()

#main
if __name__ == "__main__":
	unittest.main()