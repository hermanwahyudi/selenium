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
			time.sleep(1)
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
			browser_type = self.driver.capabilities['browserName']
			condition_product = self.driver.find_element(*self._product_loc)
			if condition_product.text != "Tidak ada Produk":
				list_product = self.driver.find_elements(*self._list_product_loc)
				i, length = 0, len(list_product)
				rand = randint(i, length-1)
				if(browser_type == "chrome"):
					list_product[rand].click()
				else:
					product_name = list_product[rand].find_element(By.TAG_NAME, "b").text
					seq = product_name.split(" ")
					j = "-".join(seq)
					self.driver.get(self.url + self.domain + "/" + j)
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

	def go_to_confirm_payment(self):
		pl_confirm_payment = "tx_payment_confirm.pl"
		try:
			self.driver.get(self.url + pl_confirm_payment)
		except Exception as inst:
			print(inst)

	def show_all_confirm(self):
		time.sleep(2)
		self.driver.find_element(By.XPATH, "//a[@id='collapse_show_all']").click()

	def confirm_payment(self, inv="INV/20141229/XIV/XII/7987989"):
		found = False
		try:
			condition_confirm = self.driver.find_element(By.XPATH, "//div[@id='change-template']")
			if("No Payment Confirmation" in condition_confirm.text or "Tidak ada Data Konfirmasi"  in condition_confirm.text):
				print("No Payment Confirmation")
			else:
				self.show_all_confirm()
				time.sleep(3)
				list_confirm = self.driver.find_elements(By.XPATH, "//div[@id='change-template']/div")
				for x in list_confirm:
					if(inv in x.text):
						id_confirmation = self.driver.find_element(By.TAG_NAME, "tr").get_attribute("id")
						self.driver.find_element(By.XPATH, "//*[@id='"+id_confirmation+"']/td[1]/input").click()
						time.sleep(2)
						self.driver.find_element(By.XPATH, "//*[@id='change-template']/div/div/div[2]/button[1]/b").click()

		except Exception as inst:
			print(inst)

	def finish_order(self, inv):
		self.go_to_status_order(1)
		print(inv)
		found = False
		try:
			list_order = self.driver.find_elements(By.XPATH, "//*[@class='list-box-content']/table")
			for i in list_order:
				if inv in i.text:
					print(inv)
					found = True
					time.sleep(3)
					id_order = i.find_element(By.TAG_NAME, "tr").get_attribute("id")
					self.driver.find_element(By.XPATH, "//*[@id='"+id_order+"']/td[2]/div[2]/div[2]/button").click()
					break
			time.sleep(1)
			if(found):
				self.driver.find_element(By.XPATH, "//*[@id='frm_delivery_action']/div[2]/button[2]").click()
				time.sleep(2)
				self.driver.find_element(By.XPATH, "//button[text()='Ok']").click()
		except Exception as inst:
			print(inst)

	def confirm_shipping(self, inv):
		pl_confirm_shipping = "myshop_order_process.pl"
		self.driver.get(self.url + pl_confirm_shipping)
		found = False
		rand_ref = randint(10000000000, 100000000000)
		try:
			condition_confirm = self.driver.find_element(By.XPATH, "//*[@id='change-template']")
			if("Tidak ada Daftar Pemesanan" in condition_confirm.text):
				print("Tidak ada Daftar Pemesanan")
			else:
				list_confirm_shipping = self.driver.find_elements(By.XPATH, "//*[@id='change-template']/div[2]/div/div/table/tbody/tr")
				for x in list_confirm_shipping:
					if(inv in x.text):
						print(inv)
						time.sleep(4)
						id_order = x.get_attribute("id")
						self.driver.find_element(By.XPATH, "//*[@id='"+id_order+"']/td[4]/div[2]/input").send_keys(rand_ref)
						time.sleep(1)
						self.driver.find_element(By.XPATH, "//*[@id='"+id_order+"']/td[5]/p[1]/a").click()
						found = True
						break
				time.sleep(2)
				if(found):
					self.driver.find_element(By.XPATH, "//button[text()='Ya']").click()
					time.sleep(2)
					self.driver.find_element(By.XPATH, "//button[text()='Ok']").click()
		except Exception as inst:
			print(inst)

	def get_last_inv(self):
		last_order = self.driver.find_element(By.XPATH, "//*[@class='list-box-content']/table")
		id_order = last_order.find_element(By.TAG_NAME, "tr").get_attribute("id")
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
				list_order = self.driver.find_elements(By.XPATH, "//div[@class='list-box-content']/table")
				j = 0
				for i in list_order:
					if inv in i.text:
						time.sleep(2)
						id_order = i.find_element(By.TAG_NAME, "tr").get_attribute("id")
						time.sleep(2)
						response_order = self.driver.find_element(By.XPATH, "//*[@id='"+id_order+"']/td[3]/div[3]/div/form/div[1]/div/div[2]/button")
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

