#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from main.page.desktop_v3.search.pe_search_base import *
from main.page.desktop_v3.search.pe_search_product import *
from main.page.desktop_v3.search.pe_search_shop import *
from main.page.desktop_v3.search.pe_search_catalog import *

class SearchActivity:

	def __init__(self, driver):
		self.search_base = SearchBasePage(driver)
		self.search_product = SearchProductPage(driver)
		self.search_shop = SearchShopPage(driver)
		self.search_catalog = SearchCatalogPage(driver)

	def set_parameter(self, global_parameter):
		self.data = global_parameter

	def go_to_tab_product(self):
		try:
			print("Click Tab Product")
			self.search_base.tab_product()
		except Exception as inst: 
			print("Exception in go to tab product!", inst)

	def go_to_tab_shop(self):
		try:
			print("Click Tab Shop")
			self.search_base.tab_shop()
		except Exception as inst: 
			print("Exception in go to tab shop!", inst)

	def go_to_tab_catalog(self):
		try:
			print("Click Tab Catalog")
			self.search_base.tab_catalog()
		except Exception as inst: 
			print("Exception in go to tab catalog!", inst)

	def do_search(self, keyword="", type=""):
		self.search_base.open(self.data['site'])
		i = 0
		while i < self.data['loop']:
			if type == "search_product":
				print("Automation search product -", (i+1))
				self.search_base.search(keyword)
				#self.search.choose_location(self.data['location'])
				self.search_base.tab_product()
				self.search_product.set_interval_price(self.data['min_price'], self.data['max_price'])
				self.search_product.searching_product(self.data['until_page'], self.data['is_exact_search_keyword'], self.data['is_search_with_price'], keyword)
			if type == "search_shop":
				print("Automation search shop -", (i+1))
				self.search_base.search(keyword)
				self.search_base.tab_shop()
				if self.data['is_search_gm_shop']:
					self.go_to_gm_shop_tab()
				self.search_shop.searching_shop(keyword, self.data['until_page'], self.data['is_search_gm_shop'])
			if type == "search_catalog":
				print("Automation search catalog -", (i+1))
				self.search_base.search(keyword)
				self.search_base.tab_catalog()
				self.search_catalog.searching_catalog(keyword, self.data['until_page'])
				#self.search_base.searching_catalog()
			time.sleep(1)
			i = i +1

	def do_click_tab(self, tab):
		if tab == "product":
			print("Click Tab Product")
			self.go_to_tab_product()
		if tab == "shop":
			print("Click Tab Shop")
			self.go_to_tab_shop()
		if tab == "catalog":
			print("Click Tab Catalog")
			self.go_to_tab_catalog()
		if tab == "gm_shop":
			print("Click Tab GM Sjop")
			self.go_to_gm_shop_tab()
		if tab == "all_shop":
			print("Click Tab All Shop")
			self.go_to_all_shop_tab()


	def go_to_gm_shop_tab(self):
		try:
			print("Click Tab GM Sjop")
			self.search_base.tab_gm_shop()
		except Exception as inst:
			print("Exception in go to gm sho tab!", inst)

	def go_to_all_shop_tab(self):
		try:
			print("Click Tab All Shop")
			self.search_base.tab_all_shop()
		except Exception as inst:
			print("Exception in go to gm sho tab!", inst)