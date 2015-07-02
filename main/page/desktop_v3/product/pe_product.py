#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from random import randint
from main.page.base import *
import os, time, sys


class ProductPage(BasePage):

	# instance variable
	_pnav_info_loc = (By.ID, "p-nav-infoprod")
	_pnav_review_loc = (By.ID, "p-nav-review")
	# _pnav_talk_loc = (By.ID, "p-nav-talk")
	_pnav_talk_loc = (By.XPATH, '//*[@id="p-nav-talk"]/a')
	_min_order_loc = (By.ID, "min-order")
	_notes_loc = (By.CSS_SELECTOR, "div.offset1 div.control-group textarea#notes")
	_btn_atc_loc = (By.CSS_SELECTOR, "div.span3 div.mt-70 a#btn-atc i.icon-shopping-cart")
	_list_shipping_agency_loc = (By.XPATH, "//select[@name='shipping_agency']/option")
	_list_service_type_loc = (By.XPATH, "//select[@id='shipping-product']/option")
	_btn_buy_loc = (By.CSS_SELECTOR, "button.btn-buy")

	# instance add new address in add to cart
	_add_addr_loc = (By.XPATH, "//*[@id='new-addr']/small/b")
	_addr_as_loc = (By.XPATH, "//*[@id='sell']/div[3]/div/div[1]/div/p/input")
	_receiver_name_loc = (By.XPATH, "//*[@id='sell']/div[3]/div/div[2]/div[1]/p/input")
	_receiver_telp_loc = (By.XPATH, "//*[@id='sell']/div[3]/div/div[2]/div[2]/p/input")
	_zip_loc = (By.XPATH, "//*[@id='sell']/div[3]/div/div[2]/div[3]/p/input")
	_province_loc = (By.XPATH, "//*[@id='province']/option")
	_regency_loc = (By.XPATH, "//*[@id='city']/option")
	_district_loc = (By.XPATH, "//*[@id='district']/option")
	_addr_loc = (By.XPATH, "//*[@id='address-street']")

	# price alert loc
	_price_alert_link_loc = (By.XPATH, "//*[@id='btn-wishlist']")
	_price_alert_input_loc = (By.XPATH, "//*[@id='wl-price']")
	_price_alert_add_loc = (By.XPATH, "/html/body/div[3]/div[1]/div[2]/div/div/div/form/div[2]/button")
	_price_alert_after_add_loc = (By.XPATH, "//*[@id='rf']/div/button")

	# report product
	_report_product_link_loc = (By.XPATH, "//*[@id='report-it']")
	_list_category_report_loc = (By.XPATH, "//*[@id='r-type']/option")
	_desc_report_loc = (By.XPATH, "//*[@id='r_message']")
	_button_report_loc = (By.XPATH, "//*[@id='d-report']/form/div[3]/button[2]")
	_button_after_report_loc = (By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div/div/button")

	# product edit locator
	_product_edit_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[5]/ul/li[1]/a')
	_product_move_to_warehouse_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[5]/ul/li[2]/a')
	_product_price_input_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/form/div[5]/div[2]/div/input[1]')
	_product_save_change_button_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/form/div[14]/button[1]')

	#Etalase Warehouse Left
	_etalase_loc = (By.CSS_SELECTOR, "div#mCSB_1 div.mCSB_container ul li")
	_etalase_name_loc = (By.CSS_SELECTOR, "div#mCSB_1 div.mCSB_container ul li a")
	_product_loc = (By.CSS_SELECTOR, "div.span9 div.shop-only-product")
	_product_list_loc = (By.CSS_SELECTOR, "div.span9 div.shop-only-product div")

	#move to warehouse
	_move_to_warehouse_button_loc = (By.CSS_SELECTOR, "div.span3 div.well.well-small.text-center.mb-10.mt-10 ul.inline li a#move-to-warehouse")
	_move_to_etalase_button_loc = (By.CSS_SELECTOR, "div.span3 div.well.well-small.text-center.mb-10.mt-10 ul.inline li a#to-etalase")
	_move_to_etalase_submit_button_loc = (By.CSS_SELECTOR, "div#to-etalase form div.dialog-footer button.btn-action")
	_move_to_warehouse_submit_button_loc = (By.CSS_SELECTOR, "div#dialog.jqmWindow.jqm-init div.jqm-inner div#dc.dialog-content div.container-fluid div#rf.row-fluid div#warehouse-dialog form div.dialog-footer button.btn.btn-action")
	_other_product_in_etalase_group_loc = (By.CSS_SELECTOR, "div.row-fluid div#prev-next-etalase-container div.span5")
	_other_product_in_etalase_group_loc = (By.CSS_SELECTOR, "div.row-fluid div#prev-next-etalase-container div.span5")
	_etalase_dropdown_loc = (By.CSS_SELECTOR, "div#to-etalase form div.control-group div.controls select#p-menu-id")
	_etalase_list_loc = (By.CSS_SELECTOR, "div#to-etalase form div.control-group div.controls select#p-menu-id option")

	#promote banner
	_promote_button_loc = (By.CSS_SELECTOR,'div.span3 div.mt-70.mb-10 a#dink-it.btn.btn-action.btn-block.text-center.jqModal')
	_promote_ads_loc = (By.CSS_SELECTOR, 'div.span3 div.mb-10.pull-left.clear-b a img')

	#Talk
	_next_page_loc = (By.CSS_SELECTOR,'div#product-talk-container div div ul li a i.icon-chevron-right')
	_talk_box = (By.CSS_SELECTOR,'div#product-talk-container ul li')

	# wishlist 
	_add_wishlist_loc = (By.XPATH, "//*[@id='btn-wish-add']")
	_after_add_wishlist_loc = (By.XPATH, "/html/body/div[3]/div[1]/div[2]/div/div/div/div/div[3]/div/div/div/button[2]")

	# dictionary shipping agency
	dict_shipping_agency = {
		"JNE": 1,
		"TIKI": 2,
		"RPX": 3,
		"Wahana": 6,
		"Cahaya": 7,
		"Pandu": 8,
		"First": 9
	}

	def domain(self, site, x=""):
		self._open(site, x)
		self.target_domain = x

	def get_name_product(self):
		url = self.driver.current_url
		ar1 = url.split("/")[4]
		ar2 = ar1.split("-")
		self.name_product = ""
		for i in ar2:
			self.name_product = self.name_product + " " + i
		return self.name_product

	def go_to_infoprod(self):
		self.driver.find_element(*self._pnav_info_loc).click()

	def go_to_review(self):
		self.driver.find_element(*self._pnav_review_loc).click()

	def go_to_talk(self):
		self.driver.find_element(*self._pnav_talk_loc).click()

	def click_wishlist(self):
		try:
			try:
				time.sleep(4)
				self.find_element(*self._add_wishlist_loc).click()
				time.sleep(5)
				self.find_element(*self._after_add_wishlist_loc).click()
				print("Wishlist Done!")
			except:
				print("Already in wishlist")
		except Exception as inst:
			print("Exception in wishlist", inst)

	def report_product(self, category="", desc=""):
		try:
			print("sending the reason message : ", desc)
			time.sleep(1)
			self.driver.find_element(*self._report_product_link_loc).click()
			time.sleep(1)
			list_category_report = self.driver.find_elements(*self._list_category_report_loc)
			print(category)
			if category != "":
				for item in list_category_report:
					if item.text == category:
						item.click()
						break
			else:
				rand = randint(0, len(list_category_report) - 1)
				list_category_report[rand].click()
			time.sleep(1)
			self.driver.find_element(*self._desc_report_loc).send_keys(desc)
			self.driver.find_element(*self._button_report_loc).click()
			time.sleep(1)
			b = self.driver.find_element(*self._button_after_report_loc).click()
			print(b)
		except Exception as inst:
			print(inst)

	def price_alert(self, price):
		try:
			time.sleep(4)
			self.driver.find_element(*self._price_alert_link_loc).click()
			time.sleep(1)
			self.driver.find_element(*self._price_alert_input_loc).clear()
			self.driver.find_element(*self._price_alert_input_loc).send_keys(price)
			self.driver.find_element(*self._price_alert_add_loc).click()
			time.sleep(1)
			self.driver.find_element(*self._price_alert_after_add_loc).click()
		except Exception as inst:
			print(inst)

	def add_to_cart(self, shipping_agency, is_add_address):

		# time.sleep(3)
		# element = WebDriverWait(self.driver, 10).until(
		#     EC.presence_of_element_located((self._btn_atc_loc))
		# )
		# element.click()
		print("cari btn buy")
		#self.driver.refresh()
		self.check_visible_element(*self._btn_atc_loc)
		print ("checked visibility")
		coba = self.find_element(*self._btn_atc_loc)
		self.click_on_javascript(coba)

		time.sleep(7)
		notes = ""
		for i in range(10):
			notes += str(i)
		#self.driver.execute_script("document.querySelector('div.jqmWindow').style.display = '';")
		WebDriverWait(self.driver,60 ).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.offset1 div.control-group textarea#notes")))
		#self.check_visible_element(*self._notes_loc)
		self.find_element(*self._notes_loc).send_keys(notes)
		if is_add_address == True:
			self.add_address("addr_as", "receiver_name", "96969696", "12240", "addr")
		self.choose_shipping_agency(shipping_agency)
		time.sleep(1)
		self.driver.find_element(*self._btn_buy_loc).submit()


	def add_address(self, addr_as, receiver_name, receiver_telp, postal_cose, addr):
		try:
			print("Add New Address in Add to Cart")
			self.driver.find_element(*self._add_addr_loc).click()
			time.sleep(1)
			self.driver.find_element(*self._addr_as_loc).send_keys(addr_as)
			self.driver.find_element(*self._receiver_name_loc).send_keys(receiver_name)
			self.driver.find_element(*self._receiver_telp_loc).send_keys(receiver_telp)
			self.driver.find_element(*self._zip_loc).send_keys(postal_cose)
			list_province = self.driver.find_elements(*self._province_loc)
			list_province[randint(1, len(list_province) - 1)].click()
			time.sleep(1)
			list_regency = self.driver.find_elements(*self._regency_loc)
			list_regency[randint(1, len(list_regency) - 1)].click()
			time.sleep(1)
			list_district = self.driver.find_elements(*self._district_loc)
			list_district[randint(1, len(list_district) - 1)].click()
			self.driver.find_element(*self._addr_loc).send_keys(addr)
		except Exception as inst:
			print(inst)

	def choose_shipping_agency(self, x=""):
		try:
			time.sleep(2)
			found = False
			list_shipping_agency = self.driver.find_elements(*self._list_shipping_agency_loc)
			j, k, length = 0, 0, len(list_shipping_agency)
			if (length > 1):
				for i in list_shipping_agency:
					if i.text == x:
						found = True
						j = k
						break
					k += 1
				if (x == "" or found == False):
					j = randint(1, length - 1)
			else:
				j = 0
			time.sleep(1)
			list_shipping_agency[j].click()
			print("Choose shipping agency", list_shipping_agency[j].text)
			time.sleep(1)
			list_service_type = self.driver.find_elements(*self._list_service_type_loc)
			for q in range(len(list_service_type)):
				if q == randint(0, len(list_service_type) - 1):
					print("Choose service type", list_service_type[q].text)
					list_service_type[q].click()
					break
			time.sleep(1)
		except Exception as inst:
			print(inst)

	def edit_price_product(self):
		self.find_element(*self._product_edit_loc).click()
		self.find_element(*self._product_price_input_loc).clear()
		self.find_element(*self._product_price_input_loc).send_keys('5000000')
		time.sleep(2)
		self.find_element(*self._product_save_change_button_loc).click()
		print("Price of the product successfully changed!")

	#warehouse
	def go_to_warehouse(self):
		etalase = self.find_elements(*self._etalase_loc)
		for elmt in etalase:
			#a = self.find_element(*self._etalase_name_loc)
			a = elmt.find_element(By.TAG_NAME,"a")
			print(a.get_attribute("class"))
			if a.get_attribute("class")=="gudang-myshop":
				a.click()
			else:
				pass
	def choose_product_in_warehouse(self):
		self.check_visible_element(*self._product_loc)
		condition_product = self.find_element(*self._product_loc)
		browser_type = self.driver.capabilities['browserName']
		if condition_product.text != "Tidak ada Produk" or condition_product.text != "No Product":
			list_product = self.driver.find_elements(*self._product_loc)
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


	def click_move_to_warehouse_button(self):
		self.check_visible_element(*self._move_to_warehouse_button_loc)
		self.find_element(*self._move_to_warehouse_button_loc).click()

	def click_move_to_warehouse_submit_button(self):
		self.find_element(*self._move_to_warehouse_submit_button_loc).click()

	def get_other_product_in_etalase_group(self):
		self.find_element(*self._other_product_in_etalase_group_loc)

	def get_move_to_etalase_button(self):
		self.find_element(*self._move_to_etalase_button_loc)

	def click_move_to_etalase_button(self):
		self.find_element(*self._move_to_etalase_button_loc).click()

	def click_move_to_etalase_submit_button(self):
		self.find_element(*self._move_to_etalase_submit_button_loc).click()

	def choose_etalase(self):
		self.find_element(*self._etalase_dropdown_loc).click()
		etalase_list = self.find_elements(*self._etalase_list_loc)
		etalase_list[randint(1,len(etalase_list)-2)].click()

	def get_dink_it_button(self):
		self.find_element(*self._promote_button_loc)

	def get_dink_it_ads(self):
		self.find_element(*self._promote_ads_loc)

	def is_other_product_in_etalase_visible(self):
		try:
			self.find_element(*self._other_product_in_etalase_group_loc)
			print('Other product in etalase is visible')
			return(1)
		except NoSuchElementException:
			print('Other product in etalase is not visible')
			return(0)

	def is_dink_it_button_visible(self):
		try:
			self.find_element(*self._promote_button_loc)
			print('Dink it button is visible')
			return(1)
		except NoSuchElementException:
			print('Dink it button is not visible')
			return(0)

	def is_check_dink_it_ads_visible(self):
		try:
			self.find_element(*self._promote_ads_loc)
			print('Dink it ads is visible')
			return(1)
		except NoSuchElementException:
			print('Dink it ads is not visible')
			return(0)

	def is_move_to_warehouse_button_visible(self):
		try:
			self.find_element(*self._move_to_warehouse_button_loc)
			print('Move to Warehouse Button is visible')
			return(1)
		except NoSuchElementException:
			print('Move to Warehouse button is not visible')
			return(0)

	def is_move_to_etalase_button_visible(self):
		try:
			self.find_element(*self._move_to_etalase_button_loc)
			print('Move to Etalase button is visible')
			return(1)
		except NoSuchElementException:
			print('Move to Etalase button is not visible')
			return(0)


	#Talk-related

	def next_page_element(self):
		try:
			self.find_element(*self._next_page_loc)
			#print ('Next page available')
			return (1)
		except NoSuchElementException:
			print ("Next page not found")
			return (0)

	def click_next_page(self):
		#print(str(self.find_element(*self._next_page_loc)) + " next page found")
		NextPage = self.next_page_element()
		if NextPage == 1:
			self.find_element(*self._next_page_loc).click()
			#print('Goto Next Page')
		elif NextPage == 0:
			print("end of page")

	def get_list_talk(self):
		try:
			list_message = self.find_elements(*self._talk_box)
			return(list_message)
		except NoSuchElementException:
			print('Tidak ada pesan')
			list_message = []
			return(list_message)

	def search_talk_ID_in_list(self, talk_ID):
		list_msg = self.get_list_talk()
		list_msg_ID = []
		isNextPageAvailable = self.next_page_element()
		print('Counting message ....')
		for i in list_msg:
			list_msg_ID.append(i.get_attribute('class'))
		if talk_ID in list_msg_ID: #if talk iD is found
			print('[' + talk_ID + '] is found')
			return(1) #true
		else:
			while isNextPageAvailable == 1:
				#search talkID
				self.click_next_page()
				time.sleep(2)
				list_msg = self.get_list_talk()
				for i in list_msg:
					list_msg_ID.append(i.get_attribute('class'))
				if talk_ID in list_msg_ID: #if found in another page
					print('[' + talk_ID + '] is found')
					return(1)
					break
				else: #if not found, check if next page available and check if talk_ID is found in another page
					isNextPageAvailable = self.next_page_element()
			#if talk is not found until the end of talk list:
			print('[' + talk_ID + '] is not found')
			return(0)
		print('end of talk list')

	def __str__(self):
		return "Page product " + self.name_product


