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
	
	# list domain toko
	domain_shop = ['tokoqc14', 'tokoqc15', 'tokoqc16']
	
	# dictionary
	dict = {
		"index_url" : "https://test.tokopedia.nginx/", #"http://new.tkpdevel-pg.steph/", #
		"email" : "tkpd.qc+13@gmail.com", #"stephanus.tedy@gmail.com", #
		"password" : "1234asdf"
	}

	def __init__(self, browser):
		self.browser = browser
	
	def open(self, url):
		self.browser.get(url)
		time.sleep(2)

	def do_login(self, email, password):
		try:
			self.browser.find_element_by_link_text("Masuk").click()
			self.browser.find_element_by_name("email").send_keys(email)
			self.browser.find_element_by_name("pwd").send_keys(password)
			self.browser.find_element_by_class_name("btn-login-top").click()
			self.browser.implicitly_wait(5)
		except Exception as inst:
			print(inst)

	def go_to_shop(self):
		length_shop = len(self.domain_shop)
		rand = randint(0, length_shop-1)
		self.open(self.dict['index_url'] + self.domain_shop[rand])

	def choose_product(self):
		self.go_to_shop()
		condition_product = self.browser.find_element(By.XPATH, "//div[@class='span9']/div[1]")
		if condition_product.text != "Tidak ada Produk":
			list_product = self.browser.find_elements(By.XPATH, "//div[@itemtype='http://schema.org/ItemList']/div")
			i, length = 0, len(list_product)
			rand = randint(i, length-1)
			print(length, list_product[0].text)
			while i < length:
				if(i == rand):
					list_product[i].click()
					break
				i += 1
			self.add_to_cart()
		else:
			print("Tidak ada Produk di Toko", self.browser.title)
			time.sleep(3)
			self.choose_product()
	
	def add_to_cart(self):
		try:
			time.sleep(2)
			element = WebDriverWait(self.browser, 10).until(
				EC.presence_of_element_located((By.ID, "btn-atc"))
			)
			element.click()
			time.sleep(5)
			self.browser.find_element(By.ID, "min-order").clear()
			self.browser.find_element(By.ID, "min-order").send_keys(randint(1, 2))
			self.browser.find_element(By.ID, "notes").send_keys(randint(1000000000, 10000000000))
			self.choose_kurir()
			time.sleep(1)
			self.browser.find_element(By.CSS_SELECTOR, "button.btn-buy").submit()
		except Exception as inst:
			print(inst)
		
	def choose_kurir(self):
		try:
			time.sleep(3)
			list_shipping_agency = self.browser.find_elements(By.XPATH, "//select[@name='shipping_agency']/option")
			i = 1
			while i < len(list_shipping_agency):
				if i == randint(1, len(list_shipping_agency)):
					list_shipping_agency[i].click()
					break
				i += 1
			time.sleep(1)
			list_service_type = self.browser.find_elements(By.XPATH, "//select[@name='shipping_product']/option")
			for j in range(len(list_service_type)):
				if j == randint(1, len(list_service_type)):
					list_service_type[j].click()
					break
			time.sleep(1)
		except Exception as inst:
			print(inst)

	def choose_payment(self, choose):
		id_payment = ""
		try:
			time.sleep(2)
			if choose == "Deposit":
				id_payment = "input-gateway-0"
			elif choose == "Bank":
				id_payment = "input-gateway-1"
			element1 = WebDriverWait(self.browser, 10).until(
					EC.presence_of_element_located((By.ID, id_payment))
				)
			element1.click()
		except Exception as inst:
			print(inst)
	def checkout(self):
		try:
			element2 = WebDriverWait(self.browser, 10).until(
				EC.visibility_of_element_located((By.CSS_SELECTOR, "button.go_to_step_1"))
			)
			time.sleep(3)
			element2.click()
		except Exception as inst:
			print(inst)

	def pay(self, choose):
		try:
			time.sleep(1)
			if choose == "Deposit":
				self.browser.find_element_by_name("password").send_keys(self.dict['password'])
			elif choose == "Bank":
				pass
			self.browser.find_element(By.CSS_SELECTOR, "button.btn-buy").submit()
		except Exception as inst:
			print(inst)

