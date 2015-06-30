#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from main.function.setup import *
from main.activity.activity_report_product import *

class TestReportProduct(unittest.TestCase):

	dict = {
		"site" : "live",
		"loop" : 2,
		"domain_shop" : "qc13",
		"price" : 4000,
		"category" : "",
		"desc" : "Apapun",
		"email_buyer" : "tkpd.qc+15@gmail.com",
		"password_buyer" : "1234asdf"
	}
	
	def setUp(self):
		self.driver = tsetup("firefox")
		self.activity = ReportProductActivity(self.driver)
		self.activity.set_parameter(self.dict)

	def test_case_report_product(self):
		print("Report Product")
		self.activity.set_report_product(self.dict['category'], self.dict['desc'])

	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.close()

# main

if(__name__ == "__main__"):
	unittest.main()

