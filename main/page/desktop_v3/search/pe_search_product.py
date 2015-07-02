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

class SearchProductPage(SearchBasePage):

	# locators interval price
	_min_price_input_loc = (By.XPATH, "//*[@id='pr-min']")
	_max_price_input_loc = (By.XPATH, "//*[@id='pr-max']") 
	_price_product_loc = (By.CLASS_NAME, "price")

	# locators by location
	_location_name_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/div/div/div[1]/div[1]/a/div/div[2]/div[2]/div[2]/small")
	_location_list_loc = (By.XPATH, "//select[@id='location']/option")

	# locator result product div
	_result_loc = (By.XPATH, "//*[@id='content-directory']/div")
	_result_list_loc = (By.XPATH, "//*[@id='content-directory']/div/div")
	_result_total_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/small/b[2]") 
	_result_name_product_loc = (By.CLASS_NAME, "name")

	# paging locator
	_next_page_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/ul/li[last()]/a/strong")
	_prev_page_loc = (By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/ul/li[1]/a/strong")

	def set_interval_price(self, min_price, max_price):
		try:
			self.min_price, self.max_price = int(min_price), int(max_price)
			self.driver.find_element(*self._min_price_input_loc).send_keys(min_price)
			self.driver.find_element(*self._max_price_input_loc).clear()
			time.sleep(3)
			self.driver.find_element(*self._max_price_input_loc).send_keys(max_price)
			time.sleep(3)
		except Exception as ins:
			print("Exception in interval price!")

	def get_list_product_search(self):
		try:
			return self.driver.find_elements(*self._result_list_loc)
		except Exception as inst:
			print("Exception in get list product serach!", inst)

	def checking_price_product(self, item):
		try:
			p, price = "", item.find_element(*self._price_product_loc).text
			for i in price:
				if i.isdigit():
					p += i
			x = int(p)
			if x >= self.min_price and x <= self.max_price:
				print(price + " is interval " + str(self.min_price) + " and " + str(self.max_price))
			else:
				print(item.text + " is not interval price range.")
		except Exception as ins:
			print("Exception in assertion price product!")

	def choose_location(self, location=""):
		try:
			time.sleep(2)
			self.driver.execute_script("document.getElementById('location').style.display = '';")
			self.driver.execute_script("document.querySelector('html.no-js.svg body div#content-container div.container div.row-fluid div.span10 div#filter-sorting-container.row-fluid.w-977 div.span12.top-filter form.form-inline div.row-fluid div.pull-left div.pull-left a.selectBox.select-styled.select-styled_medium.select-medium.ml-10.selectBox-dropdown').style.display = 'none';")
			location_list = self.driver.find_elements(*self._location_list_loc)
			length_list = len(location_list)
			if location != "":
				for item in location_list:
					loc = item
					if location == loc.text:
						loc.click()
						print(loc.text)
						break
			else:
				location_list[randint(1, length-1)].click()
			time.sleep(2)
		except Exception as ins:
			print(ins)

	def is_exact_keyword(self, keyword, item, is_exact_keyword):
		try:
			if is_exact_keyword == True:
				s = "Exact "
				if keyword == item.lower():
					return True, s
			else:
				s = "Non-Exact "
				if keyword in item.lower():
					return True, s
			print("Keyword '" + keyword + "' is not same with '" + item + "'")
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

	def searching_product(self, until_page=0, is_exact_keyword=False, is_checking_price=False, keyword=""):
		found = False
		try:
			condition = self.driver.find_element(*self._result_loc).text
			if("Oops... Your search result is not found." in condition or "Oops... hasil pencarian Anda tidak dapat ditemukan." in condition):
				print("No product with keyword '" + keyword + "'")
			else:
				time.sleep(5)
				total_result = self.driver.find_element(*self._result_total_loc).text
				print("There are " + total_result + " products")
				i, per_page, s = 0, 30, ""
				print("Page", (i+1))
				while not found and i != -1:
					items = self.driver.find_elements(*self._result_list_loc)
					j, result_per_page = 0, int((len(items)-2)/per_page)
					while j < len(items)-2:
						found, s = self.is_exact_keyword(keyword, items[j].find_element(*self._result_name_product_loc).text, is_exact_keyword)
						if is_checking_price:
							self.checking_price_product(items[j])
						if found:
							print("FOUND! \n" + items[j].text)
							items[j].click()
							print(s + "Keyword '" + keyword + "' is found in page " + str(i+1) + "")
							break
						j = j + 1
					if not found:
						print(s + "Keyword '" + keyword + "' is not found in page " + str(i+1) + "")
						i = self.page_condition(i, until_page, result_per_page)
		except Exception as inst:
			print(inst)

	def next_page(self, i=-1):
		try:
			time.sleep(4)
			print(i)
			if i != -1:
				i = i + 1
				print("Next Page", (i+1))
			self.driver.find_element(*self._next_page_loc).click()
			time.sleep(4)
			return i
		except Exception as inst:
			print("Exception in next page!")
	
	def prev_page(self, i=-1):
		try:
			time.sleep(4)
			if i != -1:
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
