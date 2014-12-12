#!/usr/bin/env python

import time, unittest, os, sys
#sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from selenium import webdriver
from p_transaksi import Transaksi


class TestTransaksi(unittest.TestCase):

	dict = {
		"index_url" : "https://test.tokopedia.nginx/", #"http://new.tkpdevel-pg.steph/", #
		"email" : "tkpd.qc+13@gmail.com", #"stephanus.tedy@gmail.com", #
		"password" : "1234asdf"
	}

	def setUp(self):
		self.driver = webdriver.Chrome("chromedriver")
		self.obj = Transaksi(self.driver)
		self.obj.open(self.dict['index_url'])
		self.obj.do_login(self.dict['email'], self.dict['password'])

	def test_case_with_deposit(self):
		i = 0
		while i < 20:
			self.obj.choose_product()
			self.obj.choose_payment("Deposit")
			self.obj.checkout()
			self.obj.pay("Deposit")
			i += 1

	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.close()

# main

if(__name__ == "__main__"):
	unittest.main()
