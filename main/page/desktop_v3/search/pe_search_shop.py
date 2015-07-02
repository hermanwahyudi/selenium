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

class SearchShopPage(SearchBasePage):

	# locator result shop div
	_result_loc = (By.XPATH, "//*[@id='content-directory']/div")
	_result_list_shop_loc = (By.XPATH, "//*[@id='content-directory']/ul/li")
	_result_name_shop_loc = (By.CSS_SELECTOR, "a b")

	# locator total of
	_total_shop_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[2]/div/div/div/div/div/div[1]/small/b[2]")

	# locator GM shop mark
	_gm_shop_loc = (By.XPATH, "//*[@id='content-directory']/ul/li[2]/div[2]/a[2]/i")

	# paging locator
	_next_page_loc = (By.XPATH, "//*[@id='content-directory']/div/div/div[2]/div/ul/li[last()]/a/strong")
	_prev_page_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/ul/li[1]/a/strong")

	# searching shop function 
	def searching_shop(self, keyword="", until_page=0, is_gm_shop=False):
		try:
			condition = self.driver.find_element(*self._result_loc).text
			if "Oops... Your search result is not found." in condition or "Oops... hasil pencarian Anda tidak dapat ditemukan." in condition: 
				print("No shop with keyword '" + keyword + "'")
			else:
				page, found = 0, False
				print("There are " + self.total_shop() + " shops")
				time.sleep(1)
				print("Page", (page+1))
				while not found and page <= until_page:
					list_shop_result = self.driver.find_elements(*self._result_list_shop_loc)
					for items in list_shop_result:
						shop_name = items.find_element(*self._result_name_shop_loc).text
						if shop_name == keyword:
							print(shop_name + " is found!")
							items.click()
							break
						else:
							print("Keyword '" + keyword + "' is not same with Shop '" + shop_name + "'")
						if is_gm_shop:
							try:
								self.is_gm_shop()
								print("Shop '" + shop_name + "' is GM \n"  )
							except:
								print("BUG! Shop '" + shop_name + "' is not GM \n")
					page += 1
					if not found and page < until_page:
						print("Next Page", (page+1))
						try:
							self.driver.find_element(*self._next_page_loc).click()
						except:
							break
						time.sleep(5)
		except Exception as inst:
			print("Exception in searching shop!", inst)

	def total_shop(self):
		return self.driver.find_element(*self._total_shop_loc).text 

	def is_gm_shop(self):
		try:
			return self.driver.find_element(*self._gm_shop_loc)
		except Exception as inst:
			print("Exception in isgm_shop function", inst)
