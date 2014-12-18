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
		"email" : "tkpd.qc+14@gmail.com",
		"password" : "1234asdf"
	}

	def setUp(self):
		self.driver = webdriver.Chrome("C:\driver\chromedriver")
		self.obj = Transaksi(self.driver)

	def test_case_with_deposit(self):
		self.obj.open("test-site")
		self.obj.do_login(self.dict_user['email'], self.dict_user['password'])
		self.obj.receive_order()
		
	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.close()

# main

if(__name__ == "__main__"):
	unittest.main()