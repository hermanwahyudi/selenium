#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from main.page.base import *
from main.page.desktop_v3.login.pe_login import *
from main.page.desktop_v3.search.pe_search_base import *
from main.page.desktop_v3.search.pe_search_product import *
from main.page.desktop_v3.product.pe_product import *
from main.page.desktop_v3.shop.pe_shop import *

class WishlistActivity:

	def __init__(self, driver):
		self.base = BasePage(driver)
		self.search_base = SearchBasePage(driver)
		self.login = LoginPage(driver)
		self.product = ProductPage(driver)
		self.shop = ShopPage(driver)
		self.search_product = SearchProductPage(driver)

	def set_parameter(self, global_parameter):
		self.dict = global_parameter

	def do_wishlist(self):
		try:
			self.product.click_wishlist()
		except Exception as inst:
			print("Exception in do wishlist", inst)

	def sequence_click(self, keyword=""):
		try:
			print("Keyword: " + keyword)
			self.login.open(self.dict['site'])
			self.login.do_login(self.dict['email_buyer'], self.dict['password_buyer'])
			page, N = 0, 32
			while page < self.dict['until_page']: 
				print("Page", (page+1))
				i = 0
				while i < N-2:
					if page == 0:
						self.base._open(self.dict['site'], "search?st=product&q="+keyword+"&sc=0")
					time.sleep(2)
					if page != 0:
						self.base._open(self.dict['site'], "search?sc=&page="+str(page+1)+"&q="+keyword+"&st=product")
					time.sleep(2)
					list_per_page = self.search_product.get_list_product_search()
					print("Wishlist", (i+1))
					N = len(list_per_page)
					list_per_page[i].click()
					self.do_wishlist()
					time.sleep(2)
					i = i + 1
				page = page + 1
				#page = self.search_product.next_page(page)
		except Exception as inst:
			print("Exception squence click search", inst)

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