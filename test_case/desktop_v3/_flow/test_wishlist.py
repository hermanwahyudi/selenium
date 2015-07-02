#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from utils.function.setup import *
from main.activity.desktop_v3.activity_wishlist import *


class TestWishlist(unittest.TestCase):

	dict = {
		"site" : "beta",
		"loop" : 1,
		"domain_shop" : "alvin",
		"until_page" : 500,
		"shop_keyword": "Toko",
		"product_keyword" : "jaket",
		"catalog_keyword" : "Nokia",
		"min_price" : 5000,
		"max_price" : 1000000,
		"location" : "Wonosobo",
		"email_buyer": "tkpd.qc+13@gmail.com",
        "password_buyer": "1234asdf"
	}

	# setUp function
	def setUp(self):
		self.driver = tsetup("chrome")
		self.activity = WishlistActivity(self.driver)
		self.activity.set_parameter(self.dict)
	
	def test_1000_do_wishlist(self):
		print("Test 1000 wishlist!")
		self.activity.sequence_click("tutup")

	"""
	def test_case_search_product(self):
		print("Test Case Seacrh product with keyword '" + self.data['product_keyword'] + "'")
		self.activity.do_search(self.data['product_keyword'], "search_product")
	
	def test_case_search_shop(self):
		print("Test Case Search shop with keyword '" + self.data['shop_keyword'] + "'")
		self.activity.do_search(self.data['shop_keyword'], "search_shop")
	
	def test_case_search_catalog(self):
		print("Test Case Search catalog with keyword '" + self.data['catalog_keyword'] + "'")
		self.activity.do_search(self.data['catalog_keyword'], "search_catalog")
	"""
	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.quit()

# main

if (__name__ == "__main__"):
    unittest.main(warnings='ignore')

