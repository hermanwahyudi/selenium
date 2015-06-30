#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from main.page.base import *
import os, time, sys

class SearchPage(BasePage):

	# page locator
	_page = "index.pl"

	# locators in header search
	_input_search_loc = (By.XPATH, "//*[@id='search-keyword']")
	_btn_search_loc = (By.CSS_SELECTOR, "button.btn-search")

	# locators tab search
	_tab_product_loc = (By.XPATH, "//*[@id='tab_product']")
	_tab_catalog_loc = (By.XPATH, "//*[@id='tab-catalog']")
	_tab_shop_loc = (By.XPATH, "//*[@id='tab-shop']")
	_tab_all_shop_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[1]/div/form/div/div[2]/div/div/a[1]")
	_tab_gm_shop_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[1]/div/form/div/div[2]/div/div/a[2]")

	#locator interval price
	_min_price_input_loc = (By.XPATH, "//*[@id='pr-min']")
	_max_price_input_loc = (By.XPATH, "//*[@id='pr-max']") 
	_price_product_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/div/div/div[1]/div[1]/a/div/div[2]/div[2]/div[1]/span")

	# locator result product div
	_result_loc = (By.XPATH, "//*[@id='content-directory']/div")
	_result_list_loc = (By.XPATH, "//*[@id='content-directory']/div/div")
	_result_total_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/small/b[2]") 

	# paging locator
	_next_page_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/ul/li[last()]/a/strong")
	_prev_page_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/ul/li[1]/a/strong")

	def open(self, site=""):
		self._open(site, self._page)

	def search(self, keyword=""):
		try:
			self.driver.find_element(*self._input_search_loc).clear()
			self.driver.find_element(*self._input_search_loc).send_keys(keyword)
			time.sleep(1)
			self.driver.find_element(*self._btn_search_loc).click()
		except Exception as inst:
			print(inst)

	def tab_product_search(self):
		try:
			self.driver.find_element(*self._tab_product_loc).click()
		except Exception as ins:
			print("Exception in tab product")

	def tab_shop_search(self):
		try:
			self.driver.find_element(*self._tab_shop_loc).click()
		except Exception as ins:
			print("Exception in tab shop!")

	def tab_catalog_search(self):
		try:
			self.driver.find_element(*self._tab_catalog_loc).click()
		except Exception as ins:
			print("Exception in tab catalog!")

	def tab_all_shop(self):
		try:
			self.driver.find_element(*self._tab_all_shop_loc).click()
		except Exception as ins:
			print("Exception in tab all shop!")

	def tab_gm_shop(self):
		try:
			self.driver.find_element(*self._tab_gm_shop_loc).click()
		except Exception as inst:
			print("Exception in tab GM shop!")

	def set_interval_price(self, min_price, max_price):
		try:
			self.driver.find_element(*self._min_price_input_loc).send_keys(min_price)
			time.sleep(3)
			self.driver.find_element(*self._max_price_input_loc).send_keys(max_price)
			time.sleep(3)
		except Exception as ins:
			print("Exception in interval price!")

	def assertion_price_product(self, item):
		try:
			print("")
		except Exception as ins:
			print("Exception in assertion price product!")

	def exact_keyword(self, keyword, item, is_exact_keyword):
		try:
			if is_exact_keyword == True:
				s = "Exact "
				if keyword == item.lower():
					return True, s
			else:
				s = "Non-Exact "
				if keyword in item.lower():
					return True, s
			return False, s
		except:
			print("Exception in exact keyword function!")

	def page_condition(self, i, until_page, result_per_page):
		try:
			if result_per_page == 0:
				return -1
			if i == until_page-1:
				return -1
			if result_per_page > 0:
				i = self.next_page(i)
				return i
		except:
			print("Exception in page condition function!")

	def assertion_search_product(self, until_page=0, is_exact_keyword=False, keyword=""):
		found = False
		try:
			condition = self.driver.find_element(*self._result_loc).text
			if("Oops... Your search result is not found." in condition or "Oops... hasil pencarian Anda tidak dapat ditemukan." in condition):
				print("No Product!")
			else:
				time.sleep(5)
				total_result = self.driver.find_element(*self._result_total_loc).text
				print("There are " + total_result + " product/shop")
				i, per_page, s = 0, 30, ""
				print("Page", (i+1))
				while not found and i != -1:
					result_list = self.driver.find_elements(*self._result_list_loc)
					result_per_page = int((len(result_list)-2)/per_page)
					for item in result_list:
						found, s = self.exact_keyword(keyword, item.text, is_exact_keyword)
						if found:
							print(s + "Keyword '" + keyword + "' is found in page", (i+1))
							print(item.text)
							item.click()
							break
					if not found:
						print(s + "Keyword '" + keyword + "' is not found in page " + str(i+1) + "")
						i = self.page_condition(i, until_page, result_per_page)
		except Exception as inst:
			print(inst)

	def next_page(self, i):
		try:
			time.sleep(4)
			i = i + 1
			print("Next Page", (i+1))
			self.driver.find_element(*self._next_page_loc).click()
			time.sleep(4)
			return i
		except Exception as inst:
			print("Exception in next page!")
	
	def prev_page(self, i):
		try:
			time.sleep(4)
			i = i - 1
			print("Prev Page", (i-1))
			self.driver.find_element(*self._prev_page_loc).click()
			time.sleep(4)
			return i
		except Exception as inst:
			print("Exception in prev page!")
	
	def sort_by(self, param=""):
		return 0

	def filter_by_location(self, location):
		return 0
