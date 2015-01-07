#!/usr/bin/env python

import time, unittest, os, sys
#sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from selenium import webdriver
from transaksi import Transaksi


class TestTransaction(unittest.TestCase):

	# instance variable
	_domain_shop = "toserba"
	_choose_shipping = "JNE"

	# dictionary user
	dict_user = {
		"email_buyer" : "laras.deninda+600@tokopedia.com",
		"password_buyer" : "asdasd",
		"email_seller" : "tkpd.qc+14@gmail.com",
		"password_seller" : "1234asdf"
	}

	def setUp(self):
		self.driver = webdriver.Chrome("C:\driver\chromedriver")
		self.obj = Transaksi(self.driver)

	def test_case_with_bank(self):
		print("Transaction with Bank")
		self.obj.open("dev-site")
		self.obj.do_login(self.dict_user['email_buyer'], self.dict_user['password_buyer'])
		i = 1
		while i <= 100:
			print("Automated Transaction - " + str(i))
			self.obj.domain(self._domain_shop)
			self.obj.choose_product()
			self.obj.add_to_cart(self._choose_shipping)
			self.obj.choose_payment("Bank")
			self.obj.checkout()
			self.obj.pay()
			i = i + 1

	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.close()

# main

if(__name__ == "__main__"):
	unittest.main()