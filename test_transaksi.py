#!/usr/bin/env python

import time, unittest, os, sys
#sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from selenium import webdriver
from transaksi import Transaksi


class TestTransaction(unittest.TestCase):

	# instance variable
	_domain_shop = "tokoqc14"
	_choose_shipping = "JNE"
	_choose_payment = "Deposit"

	# dictionary user
	dict_user = {
		"email" : "tkpd.qc+13@gmail.com",
		"password" : "1234asdf"
	}

	def setUp(self):
		self.driver = webdriver.Chrome("C:\driver\chromedriver")
		self.obj = Transaksi(self.driver)

	def test_case_with_deposit(self):
		self.obj.open("test-site")
		self.obj.do_login(self.dict_user['email'], self.dict_user['password'])
		i = 0
		while i < 5:
			self.obj.domain(self._domain_shop)
			self.obj.choose_product()
			self.obj.add_to_cart(self._choose_shipping)
			self.obj.choose_payment(self._choose_payment)
			self.obj.checkout()
			self.obj.pay(self.dict_user['password'])
			i += 1

	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.close()

# main

if(__name__ == "__main__"):
	unittest.main()