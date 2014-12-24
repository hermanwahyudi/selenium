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
		"email_buyer" : "tkpd.qc+14@gmail.com",
		"password_buyer" : "1234asdf",
		"email_seller" : "tkpd.qc+15@gmail.com",
		"password_seller" : "1234asdf"
	}

	def setUp(self):
		self.driver = webdriver.Chrome("C:\driver\chromedriver")
		self.obj = Transaksi(self.driver)

	def test_case_with_deposit(self):
		self.obj.open("live-site")
		self.obj.do_login(self.dict_user['email_buyer'], self.dict_user['password_buyer'])
		self.obj.domain("tokoqc15")
		self.obj.choose_product()
		self.obj.add_to_cart(self._choose_shipping)
		self.obj.choose_payment(self._choose_payment)
		self.obj.checkout()
		self.obj.pay(self.dict_user['password_buyer'])
		self.obj.go_to_status_order()
		inv = self.obj.get_last_inv()
		print(inv)
		self.obj.do_logout()
		self.obj.do_login(self.dict_user['email_seller'], self.dict_user['password_seller'])
		self.obj.receive_order(inv)
		self.obj.confirm_shipping(inv)
		self.obj.do_logout()
		self.obj.do_login(self.dict_user['email_buyer'], self.dict_user['password_buyer'])
		self.obj.finish_order(inv)


	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.close()

# main

if(__name__ == "__main__"):
	unittest.main()