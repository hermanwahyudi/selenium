#!/usr/bin/env python

import time, unittest, os, sys
#sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from selenium import webdriver
from transaksi import Transaksi


class TestTransaction(unittest.TestCase):

	# instance variable
	_domain_shop = "tokoqc14"
	_choose_shipping = "JNE"

	# dictionary user
	dict_user = {
		"email_buyer" : "tkpd.qc+13@gmail.com", #syntic.mail@tokopedia.com ", #"laras.deninda+600@tokopedia.com",
		"password_buyer" : "1234asdf",
		"email_seller" : "tkpd.qc+14@gmail.com",
		"password_seller" : "1234asdf"
	}

	def setUp(self):
		self.driver = webdriver.Chrome("chromedriver")
		self.obj = Transaksi(self.driver)

	def test_case_with_saldo(self):
		print("Transaction with Saldo Tokopedia")
		self.driver.get("https://beta.tokopedia.com/")
		i = 1
		while i <= 15:
			print("Automated Transaction - " + str(i))
			self.obj.do_login(self.dict_user['email_buyer'], self.dict_user['password_buyer'])
			self.driver.get("http://new.tkpdevel-pg.api/kambingshop")
			self.obj.choose_product()
			self.obj.add_to_cart(self._choose_shipping)
			self.obj.choose_payment("Deposit")
			self.obj.dropshipper("PT Maju Mundur", "086868686868")
			self.obj.checkout()
			self.obj.pay(self.dict_user['password_buyer'])
			"""self.obj.go_to_status_order()
			inv = self.obj.get_last_inv()
			print(inv)
			self.obj.do_logout()
			self.obj.do_login(self.dict_user['email_seller'], self.dict_user['password_seller'])
			self.obj.receive_order(inv)
			self.obj.do_logout()"""
			i = i + 1
	"""
	def test_case_with_tbank(self):
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
			self.obj.go_to_transaction_list()
			inv = self.obj.get_last_inv()
			print(inv)
			self.obj.go_to_confirm_payment()
			self.obj.confirm_payment(inv, "Transfer ATM", self.dict_user['password_buyer'])
			time.sleep(1)
			i = i + 1 """

	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.close()

# main

if(__name__ == "__main__"):
	unittest.main()