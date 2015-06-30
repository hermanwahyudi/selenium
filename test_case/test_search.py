#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from main.function.setup import *
from main.activity.activity_search import *


class TestSearch(unittest.TestCase):

	data = {
		"site" : "live",
		"loop" : 1,
		"until_page" : 5,
		"shop_keyword": "Toko",
		"product_keyword" : "jaket",
		"catalog_keyword" : "Nokia",
		"is_search_gm_shop" : True,
		"is_search_all_shop" : True,
		"is_exact_search_keyword" : True,
		"is_blacklist_keyword" : False
	}

	# setUp function
	def setUp(self):
		self.driver = tsetup("firefox")
		self.activity = SearchActivity(self.driver)
		self.activity.set_parameter(self.data)

	def test_case_search_product(self):
		print("Test Case Seacrh product with keyword '" + self.data['product_keyword'] + "'")
		self.activity.do_search(self.data['product_keyword'], "search_product")
	
	def test_case_search_shop(self):
		print("Test Case Search shop with keyword '" + self.data['shop_keyword'] + "'")
		self.activity.do_search(self.data['shop_keyword'], "search_shop")

	def test_case_search_catalog(self):
		print("Test Case Search catalog with keyword '" + self.data['catalog_keyword'] + "'")
		self.activity.do_search(self.data['catalog_keyword'], "search_catalog")

	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.quit()

# main

if (__name__ == "__main__"):
    unittest.main(warnings='ignore')

