#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from page.pe_login import *
from page.pe_shop import *


class TestSendMessage(unittest.TestCase):

	dict_user = {
		"email" : "tkpd.qc+13@gmail.com",
		"password" : "1234asdf"
	}

	def setUp(self):
		self.driver = webdriver.Chrome("C:\driver\chromedriver")
		self.shop = ShopPage(self.driver)
	#def test_do_fav_shop(self):

	def test_send_message(self):
		test_user_login(self.driver, self.dict_user['email'], self.dict_user['password'])
		self.shop.domain("tokoqc14")
		i = 0
		while i < 5:
			self.shop.send_message()
			i += 1

	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.close()

# main
if(__name__ == "__main__"):
	unittest.main()
