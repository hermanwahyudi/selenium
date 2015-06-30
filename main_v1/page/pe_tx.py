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

class TxPage(BasePage):

	# instance variable
	_pl_page = "tx.pl"
	_id_deposit = "input-gateway-0"
	_id_trfbank = "input-gateway-1"
	_delete_prod_loc = (By.CSS_SELECTOR, "a.delete-product")
	_checkout_loc = (By.CSS_SELECTOR, "button.go_to_step_1")
	_password_loc = (By.NAME, "password")
	_pay_loc = (By.CSS_SELECTOR, "button.btn-buy")
	_submit_delete_loc = (By.XPATH, "//button[@name='submit']")

	# dictionary url
	dict_url = {
		"url_1" : "https://www.tokopedia.com/",
		"url_2" : "https://test.tokopedia.nginx/",
		"url_3" : "https://www.tokopedia.dev/"
	}

	def go_to_tx(self):
		self.driver.get(self.dict_url['url_1'] + self._pl_page)

	def delete_product(self):
		self.driver.find_element(*self._delete_prod_loc).click()
		time.sleep(1)
		self.driver.find_element(*self._submit_delete_loc).click()

	def choose_payment(self, payment):
		id_payment = ""
		self.payment = payment
		try:
			time.sleep(2)
			if self.payment == "Deposit":
				id_payment = self._id_deposit
				print("Payment with Deposit")
			elif self.payment == "Bank":
				id_payment = self._id_trfbank
				print("Payment with Transfer Bank")
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
			print("Checkout")
		except Exception as inst:
			print(inst)

	def pay(self, password=""):
		try:
			time.sleep(1)
			if self.payment == "Deposit":
				self.driver.find_element(*self._password_loc).send_keys(password)
			elif self.payment == "Bank":
				pass
			self.driver.find_element(*self._pay_loc).submit()
			time.sleep(2)
			print("Payed")
		except Exception as inst:
			print(inst)

	def __str__(self):
		return "Page Tx"

