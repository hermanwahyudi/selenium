#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from main.page.product.pe_product import *
from main.function.general import *
import os, time, sys, json, requests
import urllib.parse
import urllib.request




class ShopPage(BasePage):

	payload = {
	'action' : 'show_dialog_new_message',
	'friend_id' : '295701',
	'shop' : '1',
	'v' : '',
	'bypass_qc' : '1'
	}


	# instance variable product
	#_product_loc = (By.XPATH, "//div[@class='span9']/div[1]")
	_product_loc = (By.XPATH, "/html/body/div[1]/section/div[4]/div[2]/div[1]/div")
	_list_product_loc = (By.XPATH, "//div[@itemtype='http://schema.org/ItemList']/div")

	# instance variable tab
	_tab_product_loc = (By.XPATH, "//*[@id='s_shopmenu']/ul/li[1]")
	_tab_talk_loc = (By.XPATH, "//*[@id='s_shopmenu']/ul/li[2]")
	_tab_review_loc = (By.XPATH, "//*[@id='s_shopmenu']/ul/li[3]")
	_tab_info_loc = (By.XPATH, "//*[@id='s_shopmenu']/ul/li[4]")

	# instance variable message
	_send_msg_loc = (By.CSS_SELECTOR, "div#send-pm button.send-pm.button")
	_subj_msg_loc = (By.ID, "message-subject")
	_text_msg_loc = (By.ID, "message")
	_submit_msg_loc = (By.XPATH, "//*[@id='new-message']/div[5]/button[2]")
	_after_submit_loc = (By.XPATH, "//*[@id='rf']/div/button")
	# instance variable fav shop
	_btn_fav_shop_loc = (By.XPATH, "//*[@id='fave_this_shop']")
	_total_shop_fav_loc = (By.XPATH, "//*[@id='gold-info-2']/ul/li[5]/a/div[1]/span/b")

	# list domain shop
	domain_shop = ['tokoqc14', 'tokoqc15', 'tokoqc16']
	target_domain = ""

	#Security
	_captcha_loc = (By.CSS_SELECTOR, 'div#recaptcha_widget div.mb-10 div input.recaptcha_response_field')

	def domain(self, site, x=""):
		self._open(site, x)
		self.target_domain = x

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
		total_before = int(total_before) + 1
		try:
			element = WebDriverWait(self.driver, 10).until(
				EC.visibility_of_element_located((self._btn_fav_shop_loc))
			)
			time.sleep(10)
			print(element.text)
			bl = element.click()
			time.sleep(1)
			total_after = self.driver.find_element(*self._total_shop_fav_loc).text
			if (total_before == int(total_after)):
				print("Counter OK.")
			print(total_before, total_after, bl)
		except Exception as inst:
			print(inst)

	# klik button send message (sebelum tulis pesan)
	def click_send_message_button(self):
		try:
			time.sleep(2)
			self.driver.find_element(*self._send_msg_loc).click()
		except Exception as inst:
			print(inst)


	#klik button send message (setelah tulis pesan)
	def click_send_message(self, driver, subject, message):
		print('masuk method click send message')
		try:
			time.sleep(10)
			self.driver.find_element(*self._send_msg_loc).click()
			time.sleep(10)
			print('Sent message button clicked')
			time.sleep(2)
			self.find_element(*self._subj_msg_loc).send_keys(subject)
			print('Enter subject succeed')
			self.find_element(*self._text_msg_loc).send_keys(message)
			print('Write message succeed')
			self.find_element(*self._submit_msg_loc).click()
			print('Submit message')
			time.sleep(3)
			self.find_element(*self._after_submit_loc).click()
			print('Confirmation done')
		except NoSuchElementException:
			print('No such element')

	def choose_product(self):

		self.check_visible_element(*self._product_loc)
		condition_product = self.find_element(*self._product_loc)
		browser_type = self.driver.capabilities['browserName']
		if condition_product.text != "Tidak ada Produk" or condition_product.text != "No Product":
			list_product = self.driver.find_elements(*self._list_product_loc)
			i, length = 0, len(list_product)
			rand = randint(i, length - 1)
			print("Choose product", list_product[rand].text)
			if (browser_type == "chrome"):
				#list_product[rand].click()
				self._click(list_product[rand])
				time.sleep(4)

			else:
				product_name = list_product[rand].find_element(By.TAG_NAME, "b").text
				seq = product_name.split(" ")
				c = "-".join(seq)
				self.driver.get(self.url + self.target_domain + "/" + c)
		else:
			print("No product in", self.driver.title)



	#====================FOR UNIT TESTING PURPOSE, DO NOT DELETE====================#		
	#bypass captcha
	def bypass_send_message(self, people_ID):
		self.payload['friend_id'] = people_ID
		print(self.payload['friend_id'])
		requests.get("https://www.tokopedia.com/ajax/people-4.pl", data=self.payload)

		#print (pos.text)
		self.payload['friend_id'] = request.get.get('v')
		data = urllib.parse.urlencode(self.payload)
		data = data.encode('utf-8') # data should be bytes
		req = urllib.request.Request("https://www.tokopedia.com/ajax/people-4.pl", self.payload)
		response = urllib.request.urlopen("https://www.tokopedia.com/ajax/people-4.pl")
		the_page = response.read()

	def check_is_captcha_available(self):
		self.check_visible_element(self._captcha_loc[0], self._captcha_loc[1])
		print('captcha appeared')
	#==================FOR UNIT TESTING PURPOSE, DO NOT DELETE=======================#


	def __str__(self):
		return "Page Toko " + self.driver.title


