#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from main.page.base import *
from main.page.desktop_v3.search.pe_search_base import *
import os, time, sys

class SearchCatalogPage(SearchBasePage):

	# locator result shop div
	_result_loc = (By.XPATH, "//*[@id='content-directory']/div/div")

	# locator total of
	_total_catalog_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[2]/div/div/div/div/div/div[1]/small/b[2]")

	# locator GM shop mark
	_catalog_name_loc = (By.CLASS_NAME, "name")
	_catalog_price_loc = (By.CLASS_NAME, "price")

	# paging locator
	_next_page_loc = (By.XPATH, "//*[@id='content-directory']/div/div/div[2]/div/ul/li[last()]/a/strong")
	_prev_page_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/ul/li[1]/a/strong")

	def get_catalog_name(self, item=None):
		try:
			return item.find_element(*self._catalog_name_loc).text
		except Exception as ins:
			print("Exception in get catalog name!", ins)

	def get_catalog_price(self, item, rp=False):
		try:
			s, price = "", item.find_element(*self._catalog_price_loc).text 
			if rp == False:
				return price
			else:
				for c in price:
					if c.isdigit():
						s += c
						
				return s
		except Exception as ins:
			print("Exception in get price catalog!", ins)

	def check_keyword(self, item, keyword=""):
		try:
			catalog_name = self.get_catalog_name(item)
			if catalog_name != keyword:
				print("Exact keyword '" + keyword + "' is not same with '" + catalog_name + "'")
				return False
			if catalog_name == keyword:
				print("FOUND!")
				item.click()
				found = True
		except Exception as inst:
			print("Exception in check keyword!", inst)

	# searching shop function 
	def searching_catalog(self, keyword="", until_page=0):
		try:
			current_page, found = 0, False
			while not found and current_page < until_page:
				time.sleep(4)
				items = self.driver.find_elements(*self._result_loc)
				i, length = 0, len(items)
				print("Page", (current_page+1))
				while i < length-2:
					found = self.check_keyword(items[i], keyword)
					if found:
						break
					i += 1
				if not found and current_page < until_page:
					current_page = self.next_page(current_page)
		except Exception as inst:
			print("Exception in searching catalog!", inst)

	def next_page(self, current_page):
		try:
			next_page = current_page+1
			print("Next Page", (next_page+1))
			self.driver.find_element(*self._next_page_loc).click()
			return next_page
		except Exception as inst:
			print("Exception in next page search catalog!", inst)

	def prev_page(self, current_page):
		try:
			prev_page = current_page-1
			print("Prev Page", (prev_page-1))
			self.driver.find_element(*self._prev_page_loc).click()
			return prev_page
		except Exception as ins:
			print("Exception in prev page search catalog!", inst)


	

	