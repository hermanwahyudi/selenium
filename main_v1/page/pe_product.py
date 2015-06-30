#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from page.base import * 
import os, time, sys

class ProductPage(BasePage):

	# instance variable
	_pnav_info_loc = (By.ID, "p-nav-infoprod")
	_pnav_review_loc = (By.ID, "p-nav-review")
	_pnav_talk_loc = (By.ID, "p-nav-talk")
	_min_order_loc = (By.ID, "min-order")
	_notes_loc = (By.ID, "notes")
	_btn_atc_loc = (By.ID, "btn-atc")
	_list_shipping_agency_loc = (By.XPATH, "//select[@name='shipping_agency']/option")
	_list_service_type_loc = (By.XPATH, "//select[@id='shipping-product']/option")
	_btn_buy_loc = (By.CSS_SELECTOR, "button.btn-buy")

	# dictionary url
	dict_url = {
		"url_1" : "https://www.tokopedia.com/",
		"url_2" : "https://test.tokopedia.nginx/",
		"url_3" : "https://www.tokopedia.dev/"
	}

	# dictionary shipping agency
	dict_shipping_agency = {
		"JNE" : 1,
		"TIKI" : 2,
		"RPX" : 3,
		"Wahana" : 6,
		"Cahaya" : 7,
		"Pandu" : 8,
		"First" : 9
	}
	
	def get_name_product(self):
		url = self.driver.current_url
		ar1 = url.split("/")[4]
		ar2 = ar1.split("-")
		self.name_product = ""
		for i in ar2:
			self.name_product = self.name_product + " " + i
		return self.name_product

	def go_to_infoprod(self):
		self.driver.find_element(*self._pnav_infoprod_loc).click()

	def go_to_review(self):
		self.driver.find_element(*self._pnav_review_loc).click()

	def go_to_talk(self):
		self.driver.find_element(*self._pnav_talk_loc).click()

	def add_to_cart(self, shipping_agency):
		try:
			time.sleep(3)
			element = WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((self._btn_atc_loc))
			)
			element.click()
			time.sleep(3)
			self.driver.find_element(*self._min_order_loc).clear()
			self.driver.find_element(*self._min_order_loc).send_keys(randint(1, 2))
			notes = ""
			for i in range(50):
				notes += str(i)
			self.driver.find_element(*self._notes_loc).send_keys(notes)
			self.choose_shipping_agency(shipping_agency)
			time.sleep(1)
			self.driver.find_element(*self._btn_buy_loc).submit()
		except Exception as inst:
			print(inst)
		
	def choose_shipping_agency(self, x=""):
		try:
			time.sleep(2)
			found = False
			list_shipping_agency = self.driver.find_elements(*self._list_shipping_agency_loc)
			j, k, length = 0, 0, len(list_shipping_agency)
			if(length > 1):
				for i in list_shipping_agency:
					if i.text == x:
						found = True
						j = k
						break
					k += 1
				if(x == "" or found == False):
					j = randint(1, length-1)
			else:
				j = 0
			time.sleep(1)
			list_shipping_agency[j].click()
			print("Choose shipping agency", list_shipping_agency[j].text)
			time.sleep(1)
			list_service_type = self.driver.find_elements(*self._list_service_type_loc)
			for q in range(len(list_service_type)):
				if q == randint(0, len(list_service_type)-1):
					print("Choose service type", list_service_type[q].text)
					list_service_type[q].click()
					break
			time.sleep(1)
		except Exception as inst:
			print(inst)

	def __str__(self):
		return "Page product " + self.name_product

class TalkProductPage(ProductPage):

	# instance variable
	_textarea_loc = (By.XPATH, "//textarea[@id='']")
	_submit_loc = (By.XPATH, "//button[text()='Diskusi']")
	
	def input_talk(self):
		try:
			talk = ""
			for i in range(10):
				talk += str(i)
			time.sleep(2)
			self.driver.find_element(*self._textarea_loc).send_keys(talk)
			self.driver.find_element(*self._submit_loc).click()
		except Exception as inst:
			print(inst)

	def __str__(self):
		return "Page Talk"