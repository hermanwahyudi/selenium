#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import os, time, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))

class Transaksi():
	
	# instance variable login
	_link_login_loc = (By.LINK_TEXT, "Masuk")
	_email_login_loc = (By.NAME, "email")
	_password_login_loc = (By.ID, "inputPassword")
	_btn_login_loc = (By.CLASS_NAME, "btn-login-top")

	# instance variable product
	_product_loc = (By.XPATH, "//div[@class='span9']/div[1]")
	_list_product_loc = (By.XPATH, "//div[@itemtype='http://schema.org/ItemList']/div")

	# instance variable
	_pl_page = "tx.pl"
	_id_deposit = "input-gateway-0"
	_id_trfbank = "input-gateway-1"
	_delete_prod_loc = (By.CSS_SELECTOR, "a.delete-product")
	_checkout_loc = (By.CSS_SELECTOR, "button.go_to_step_1")
	_password_loc = (By.NAME, "password")
	_pay_loc = (By.CSS_SELECTOR, "button.btn-buy")
	_submit_delete_loc = (By.XPATH, "//button[@name='submit']")

	# instance variable atc
	_min_order_loc = (By.ID, "min-order")
	_notes_loc = (By.ID, "notes")
	_btn_atc_loc = (By.ID, "btn-atc")
	_list_shipping_agency_loc = (By.XPATH, "//select[@name='shipping_agency']/option")
	_list_service_type_loc = (By.XPATH, "//select[@id='shipping-product']/option")
	_btn_buy_loc = (By.CSS_SELECTOR, "button.btn-buy")

	# list domain toko
	domain_shop = ['tokoqc14', 'tokoqc15', 'tokoqc16']

	#dictionary url
	dict_url = {
		"url_1" : "https://www.tokopedia.com/",
		"url_2" : "https://test.tokopedia.nginx/",
		"url_3" : "https://www.tokopedia.dev/"
	}

	# id_order 
	id_order = ""

	def __init__(self, browser):
		self.driver = browser
	
	def open(self, flag):
		self.url = ""
		try:
			if(flag == "live-site"):
				self.url = self.dict_url['url_1']
			elif(flag == "test-site"):
				self.url = self.dict_url['url_2']
			else:
				self.url = self.dict_url['url_3']
			self.driver.get(self.url)
			time.sleep(2)
		except Exception as inst:
			print(inst)

	def do_login(self, email, password):
		try:
			self.driver.find_element(*self._link_login_loc).click()
			self.driver.find_element(*self._email_login_loc).send_keys(email)
			self.driver.find_element(*self._password_login_loc).send_keys(password)
			self.driver.find_element(*self._btn_login_loc).click()
			self.driver.implicitly_wait(5)
		except Exception as inst:
			print(inst)

	def do_logout(self):
		pl_logout = "logout.pl"
		try:
			time.sleep(5)
			user_tab = self.driver.find_element(By.ID, "user-tab")
			ActionChains(self.driver).move_to_element(user_tab).perform()
			self.driver.get(self.url + pl_logout)
		except Exception as inst:
			print(inst)

	def domain(self, x=0):
		self.domain = ""
		try:
			if x == 0:
				rand = randint(0, len(self.domain_shop)-1)
				self.domain = self.domain_shop[rand]
			else:
				self.domain = x
			self.driver.get(self.url + self.domain)
		except Exception as inst:
			print(inst)

	def choose_product(self):
		try:
			condition_product = self.driver.find_element(*self._product_loc)
			if condition_product.text != "Tidak ada Produk":
				list_product = self.driver.find_elements(*self._list_product_loc)
				i, length = 0, len(list_product)
				rand = randint(i, length-1)
				while i < length:
					if(i == rand):
						list_product[i].click()
						break
					i += 1
			else:
				print("Tidak ada Produk di Toko", self.driver.title)
		except Exception as inst:
			print(inst)
	
	def add_to_cart(self, shipping_agency):
		try:
			time.sleep(4)
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
			time.sleep(1)
			list_service_type = self.driver.find_elements(*self._list_service_type_loc)
			for q in range(len(list_service_type)):
				if q == randint(0, len(list_service_type)-1):
					list_service_type[q].click()
					break
			time.sleep(1)
		except Exception as inst:
			print(inst)

	def choose_payment(self, payment):
		id_payment = ""
		self.payment = payment
		try:
			time.sleep(2)
			if self.payment == "Deposit":
				id_payment = self._id_deposit
			elif self.payment == "Bank":
				id_payment = self._id_trfbank
			element1 = WebDriverWait(self.driver, 10).until(
					EC.presence_of_element_located((By.ID, id_payment))
				)
			element1.click()
		except Exception as inst:
			print(inst)
			
	def checkout(self):
		try:
			element2 = WebDriverWait(self.driver, 10).until(
				EC.visibility_of_element_located((self._checkout_loc))
			)
			time.sleep(3)
			element2.click()
		except Exception as inst:
			print(inst)

	def pay(self, password):
		try:
			time.sleep(1)
			if self.payment == "Deposit":
				self.driver.find_element(*self._password_loc).send_keys(password)
			elif self.payment == "Bank":
				pass
			self.driver.find_element(*self._pay_loc).submit()
		except Exception as inst:
			print(inst)

	def go_to_status_order(self, flag=0):
		pl_status_order = "tx_order_status.pl"
		try:
			if(flag == 0):
				time.sleep(1)
				self.driver.find_element(By.LINK_TEXT, "Status Pembayaran").click()
			else:
				self.driver.get(self.url + pl_status_order)
		except Exception as inst:
			print(inst)

	def confirm_shipping(self, inv):
		pl_confirm_shipping = "myshop_order_process.pl"
		self.driver.get(self.url + pl_confirm_shipping)
		found = False
		try:
			condition_confirm = self.driver.find_element(By.XPATH, "//*[@id='change-template']")
		except Exception as inst:
			print(inst)

	def get_id_order(self):
		last_order = self.driver.find_element(By.XPATH, "//*[@class='list-box-content']/table")
		self.id_order = last_order.find_element(By.TAG_NAME, "tr").get_attribute("id")
		return self.id_order

	def get_invoice(self):
		id_order = self.get_id_order()
		self.inv = self.driver.find_element(By.XPATH, "//*[@id='"+ id_order +"']/td[2]/a/b")
		return self.inv.text

	def receive_order(self, inv):
		pl_new_order = "myshop_order.pl"
		self.driver.get(self.url + pl_new_order)
		found = False
		try:
			condition_order = self.driver.find_element(By.XPATH, "//*[@id='change-template']")
			if("Tidak ada Daftar Pemesanan" in condition_order.text):
				print("Tidak ada Order Baru")
			else:
				print(inv, self.id_order)
				list_order = self.driver.find_elements(By.XPATH, "//div[@class='list-box-content']/table")
				j = 0
				for i in list_order:
					if inv in i.text:
						time.sleep(4)
						print(inv)
						response_order = self.driver.find_element(By.XPATH, "//*[@id='"+self.id_order+"']/td[3]/div[3]/div/form/div[1]/div/div[2]/button")
						response_order.click()
						found = True
						break
					j += 1
				time.sleep(1)
				if(found == True):
					self.driver.find_element(By.XPATH, "//button[text()='Ya']").click()
					time.sleep(2)
					self.driver.find_element(By.XPATH, "//button[text()='Ok']").click()
		except Exception as inst:
			print(inst)

	def __str__(self):
		return "Transaksi"

