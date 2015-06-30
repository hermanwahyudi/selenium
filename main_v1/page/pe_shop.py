#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from page.pe_product import *
import os, time, sys

class ShopPage(BasePage):

	# instance variable product
	_product_loc = (By.XPATH, "//div[@class='span9']/div[1]")
	_list_product_loc = (By.XPATH, "//div[@itemtype='http://schema.org/ItemList']/div")

	# instance variable tab
	_tab_product_loc = (By.XPATH, "//*[@id='s_shopmenu']/ul/li[1]")
	_tab_talk_loc = (By.XPATH, "//*[@id='s_shopmenu']/ul/li[2]")
	_tab_review_loc = (By.XPATH, "//*[@id='s_shopmenu']/ul/li[3]")
	_tab_info_loc = (By.XPATH, "//*[@id='s_shopmenu']/ul/li[4]")

	# instance variable message
	_send_msg_loc = (By.ID, "s_send_pm")
	_subj_msg_loc = (By.ID, "message-subject")
	_text_msg_loc = (By.ID, "message")
	_submit_msg_loc = (By.XPATH, '//button[text()="Kirim"]')
	_after_submit_loc = (By.CSS_SELECTOR, "div.dialog-footer button.btn-action")

	# instance variable fav shop
	_btn_fav_shop_loc = (By.XPATH, "//*[@id='fave_this_shop']")
	_total_shop_fav_loc = (By.XPATH, "//*[@id='gold-info-2']/ul/li[5]/a/div[1]/span/b")

	# list domain shop
	domain_shop = ['tokoqc14', 'tokoqc15', 'tokoqc16']

	#dictionary
	dict_url = {
		"url_1" : "https://www.tokopedia.com/",
		"url_2" : "https://test.tokopedia.nginx/",
		"url_3" : "https://www.tokopedia.dev/"
	}

	def domain(self, x=0):
		self.domain, self.url = "", ""
		try:
			if x == 0:
				rand = randint(0, len(self.domain_shop)-1)
				self.domain = self.domain_shop[rand]
			else:
				self.domain = x
			self.url = self.dict_url['url_1']
			self.driver.get(self.url + self.domain)
		except Exception as inst:
			print(inst)

	def go_to_product_tab(self):
		self.driver.find_element(*self._tab_product_loc).click()

	def go_to_talk_product_tab(self):
		self.driver.find_element(*self._tab_talk_loc).click()

	def go_to_review_tab(self):
		self.driver.find_element(*self._tab_review_loc).click()

	def go_to_info_shop_tab(self):
		self.driver.find_element(*self._tab_info_loc).click()

	def do_fav_shop(self):
		total_before = self.driver.find_element(*self._total_shop_fav_loc).text
		total_before = int(total_before)+1
		try:
			element = WebDriverWait(self.driver, 10).until(
				EC.visibility_of_element_located((self._btn_fav_shop_loc))
			)
			time.sleep(10)
			print(element.text)
			bl = element.click()
			time.sleep(1)
			total_after = self.driver.find_element(*self._total_shop_fav_loc).text
			if(total_before == int(total_after)):
				print("Counter OK.")
			print(total_before, total_after, bl)
		except Exception as inst:
			print(inst)

	def send_message(self):
		try:
			s = ""
			for i in range(100):
				s += str(i)
			time.sleep(2)
			self.driver.find_element(*self._send_msg_loc).click()
			time.sleep(2)
			self.driver.find_element(*self._subj_msg_loc).send_keys(randint(100, 1000000))
			self.driver.find_element(*self._text_msg_loc).send_keys(s)
			self.driver.find_element(*self._submit_msg_loc).click()
			time.sleep(1)
			self.driver.find_element(*self._after_submit_loc).click()
		except Exception as inst:
			print(inst)

	def choose_product(self):
		try:
			condition_product = self.driver.find_element(*self._product_loc)
			browser_type = self.driver.capabilities['browserName']
			if condition_product.text != "Tidak ada Produk" or condition_product.text != "No Product":
				list_product = self.driver.find_elements(*self._list_product_loc)
				i, length = 0, len(list_product)
				rand = randint(i, length-1)
				print("Choose product", list_product[rand].text)
				if(browser_type == "chrome"):
					list_product[rand].click()
				else:
					product_name = list_product[rand].find_element(By.TAG_NAME, "b").text
					seq = product_name.split(" ")
					c = "-".join(seq)
					self.driver.get(self.url + self.domain + "/" + c)
			else:
				print("No product in", self.driver.title)
		except Exception as inst:
			print(inst)

	def __str__(self):
		return "Page Toko " + self.driver.title


