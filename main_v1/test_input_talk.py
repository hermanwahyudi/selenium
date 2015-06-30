#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from page.pe_login import *
from page.pe_shop import *
from page.pe_product import *


class TestInputTalk(unittest.TestCase):

	dict_user = {
		"email" : "tkpd.qc+13@gmail.com",
		"password" : "1234asdf"
	}

	def setUp(self):
		self.driver = webdriver.Chrome("C:\driver\chromedriver")
		self.shop = ShopPage(self.driver)
		self.prod = ProductPage(self.driver)
		self.talk = TalkProductPage(self.driver)
	
	def test_input_talk(self):
		test_user_login(self.driver, self.dict_user['email'], self.dict_user['password'])
		self.shop.domain("tokoqc14")
		self.shop.choose_product()
		self.prod.go_to_talk()
		i = 0
		while i < 5:
			time.sleep(1)
			self.talk.input_talk()
			self.driver.refresh()
			i += 1

	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.close()

# main
if(__name__ == "__main__"):
	unittest.main()
