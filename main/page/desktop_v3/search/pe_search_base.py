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

class SearchBasePage(BasePage):

	# page locator
	_page = "index.pl"

	# locators in header search
	_input_search_loc = (By.XPATH, "//*[@id='search-keyword']")
	_btn_search_loc = (By.CSS_SELECTOR, "button.btn-search")

	# locators tab search
	_tab_product_loc = (By.XPATH, "/html/body/div[1]/div[4]/div/div[1]/ul/li[1]/a")
	_tab_catalog_loc = (By.XPATH, "//*[@id='tab-catalog']")
	_tab_shop_loc = (By.XPATH, "//*[@id='tab-shop']")
	_tab_all_shop_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[1]/div/form/div/div[2]/div/div/a[1]")
	_tab_gm_shop_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[1]/div/form/div/div[2]/div/div/a[2]")

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

	def tab_product(self):
		try:
			self.driver.find_element(*self._tab_product_loc).click()
		except Exception as ins:
			print("Exception in tab product", ins)

	def tab_shop(self):
		try:
			self.driver.find_element(*self._tab_shop_loc).click()
		except Exception as ins:
			print("Exception in tab shop!", ins)

	def tab_catalog(self):
		try:
			self.driver.find_element(*self._tab_catalog_loc).click()
		except Exception as ins:
			print("Exception in tab catalog!", ins)

	def tab_all_shop(self):
		try:
			self.driver.find_element(*self._tab_all_shop_loc).click()
		except Exception as ins:
			print("Exception in tab all shop!", ins)

	def tab_gm_shop(self):
		try:
			self.driver.find_element(*self._tab_gm_shop_loc).click()
		except Exception as inst:
			print("Exception in tab GM shop!", ins)

	def __str__(self):
		return self.driver.title
	