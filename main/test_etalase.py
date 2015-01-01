#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from page.pe_login import *
from page.pe_myshop_etalase import *

class TestMyshopEtalse(unittest.TestCase):

	dict_user = {
		"email" : "tkpd.qc+14@gmail.com",
		"password" : "1234asdf"
	}

	def setUp(self):
		self.driver = webdriver.Chrome("C:\driver\chromedriver")
		self.etalse = MyshopEtalasePage(self.driver)
	
	def test_do_validasi(self):
		test_user_login(self.driver, self.dict_user['email'], self.dict_user['password'])
		self.etalse.go()
		self.etalse.do_validation()

	def test_act_n_times(self):
		test_user_login(self.driver, self.dict_user['email'], self.dict_user['password'])
		self.etalse.go()
		self.etalse.act_n_times("edit", 500)

	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.close()

# main

if(__name__ == "__main__"):
	unittest.main()
