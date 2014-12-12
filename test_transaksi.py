#!/usr/bin/env python

import time, unittest, os, sys
#sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from selenium import webdriver
from random import randint
from p_transaksi import Transaksi


class TestTransaksi(unittest.TestCase):

	# list domain toko
	domain_shop = ['tokoqc14', 'tokoqc15', 'tokoqc16', 'claire']
	
	# dictionary
	dict = {
		"index_url" : "http://new.tkpdevel-pg.steph/", #
		"email" : "stephanus.tedy@gmail.com", #
		"password" : "123123"
	}

	def setUp(self):
		self.driver = webdriver.Chrome("chromedriver")
		self.obj = Transaksi(self.driver)
		self.obj.open(self.dict['index_url'])
		self.obj.do_login(self.dict['email'], self.dict['password'])

	def test_checkout_with_deposit(self):
		i = 0
		while i < 20:
			rand = randint(0, len(self.domain_shop)-1)
			print(rand, len(self.domain_shop)-1)
			self.obj.go_to_shop(self.dict['index_url'], self.domain_shop[3])
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
