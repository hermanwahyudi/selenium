#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from page.pe_login import *
from page.pe_shop import *
from page.pe_product import *
from page.pe_tx import *  
from page.pe_myshop_order import *
from page.pe_tx_payment import *

class TestTransaction(unittest.TestCase):

	# instance variable
	_domain_shop = "tokoqc15"
	_choose_shipping = "JNE"

	# dictionary user
	dict_user = {
		"email_buyer" : "tkpd.qc+1000@gmail.com",
		"password_buyer" : "1234asdf",
		"email_seller" : "tkpd.qc+15@gmail.com",
		"password_seller" : "1234asdf"
	}

	def setUp(self):
		self.driver = webdriver.Chrome("C:\driver\chromedriver")
		self.shop = ShopPage(self.driver)
		self.prod = ProductPage(self.driver)
		self.tx = TxPage(self.driver)
		self.o_status = OrderStatusPage(self.driver)
		self.m_order = MyshopOrderPage(self.driver)
		self.process_order = MyshopOrderProcessPage(self.driver)
		self.confirm_payment = PaymentConfirmationPage(self.driver)
		self.list_transact = TransactionListPage(self.driver)

	def test_case_with_bank(self):
		print("Transaction with Bank")
		test_user_login(self.driver, self.dict_user['email_buyer'], self.dict_user['password_buyer'])
		self.shop.domain("tokoqc15")
		self.shop.choose_product()
		self.prod.add_to_cart(self._choose_shipping)
		self.tx.choose_payment("Bank")
		self.tx.checkout()
		self.tx.pay()
		self.list_transact.open()
		inv = self.list_transact.get_last_inv()
		print(inv)
		self.confirm_payment.open()
		self.confirm_payment.confirm_payment(inv, "Saldo Tokopedia", self.dict_user['password_buyer'])

	def test_case_with_deposit_until_finish(self):
		print("Transaction with Deposit")
		test_user_login(self.driver, self.dict_user['email_buyer'], self.dict_user['password_buyer'])
		self.shop.domain(self._domain_shop)
		self.shop.choose_product()
		self.prod.add_to_cart(self._choose_shipping)
		self.tx.choose_payment("Deposit")
		self.tx.checkout()
		self.tx.pay(self.dict_user['password_buyer'])
		self.o_status.open()
		inv = self.o_status.get_last_inv()
		print(inv)
		test_user_logout(self.driver)
		test_user_login(self.driver, self.dict_user['email_seller'], self.dict_user['password_seller'])
		self.m_order.open()
		self.m_order.response_order(inv) 
		self.process_order.open()
		self.process_order.confirm_shipping(inv)
		test_user_logout(self.driver)
		test_user_login(self.driver, self.dict_user['email_buyer'], self.dict_user['password_buyer'])
		self.o_status.open()
		self.o_status.finish_order(inv)

	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.close()

# main

if(__name__ == "__main__"):
	unittest.main()
