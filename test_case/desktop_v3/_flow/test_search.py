#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from utils.function.setup import *
from main.activity.desktop_v3.activity_search import *

class RunTestSearch():

	def __init__(self):
		self.data = data = {
			"site" : "beta",
			"loop" : 1,
			"until_page" : 4,
			"shop_keyword": "Toko",
			"product_keyword" : "jaket",
			"catalog_keyword" : "Nokia",
			"min_price" : 5000,
			"max_price" : 1000000,
			"location" : "Wonosobo",
			"is_search_gm_shop" : False,
			"is_search_all_shop" : False,
			"is_exact_search_keyword" : True,
			"is_search_with_price" : False,
			"is_blacklist_keyword" : False
		}

	def get_data(self):
		return self.data
		
	def run(self):
		# main

		if (__name__ == "__main__"):
		    unittest.main(warnings='ignore')

class TestSearch(unittest.TestCase):

	# setUp function
	def setUp(self):
		self.driver = tsetup("chrome")
		self.activity = SearchActivity(self.driver)
		self.data = RunTestSearch().get_data() 
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

RunTestSearch().run()

