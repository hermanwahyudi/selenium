#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from main.page.search.pe_search import *

class SearchActivity:

	def __init__(self, driver):
		self.search = SearchPage(driver)

	def set_parameter(self, global_parameter):
		self.data = global_parameter

	def do_search(self, keyword="", type=""):
		self.search.open(self.data['site'])
		i = 0
		while i < self.data['loop']:
			if type == "search_product":
				print("Automation search product -", (i+1))
				self.search.search(keyword)
				self.search.assertion_search_product(self.data['until_page'], self.data['is_exact_search_keyword'], keyword)
			if type == "search_shop":
				print("Automation search shop -", (i+1))
				self.search.search(keyword)
				print("Click Tab Shop")
				self.search.tab_shop_search()
				if self.data['is_search_gm_shop'] == True:
					print("Click Tab GM Shop")
					self.search.tab_gm_shop()
				if self.data['is_search_all_shop'] == True:
					print("Click Tab All Shop")
					self.search.tab_all_shop()
			if type == "search_catalog":
				print("Automation search catalog -", (i+1))
				self.search.search(keyword)
				print("Click Tab Catalog")
				self.search.tab_catalog_search()
			time.sleep(1)
			i = i +1