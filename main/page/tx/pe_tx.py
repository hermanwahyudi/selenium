#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from main.page.base import * 
import os, time, sys

class TxPage(BasePage):

	# instance variable
	_pl = "tx.pl"
	_id_deposit = "input-gateway-0"
	_id_trfbank = "input-gateway-1"
	_delete_prod_loc = (By.CSS_SELECTOR, "a.delete-product")
	_checkout_loc = (By.CSS_SELECTOR, "button.go_to_step_1")
	_password_loc = (By.NAME, "password")
	_pay_loc = (By.CSS_SELECTOR, "button.btn-buy")
	_submit_delete_loc = (By.XPATH, "//button[@name='submit']")
	_partial_deposit_check_loc = (By.XPATH, "//*[@id='use-deposit']")
	_partial_deposit_amount_loc = (By.XPATH, "//*[@id='deposit-amt']")
	_dropshipper_checked_loc = (By.XPATH, ".//*[@class='dropship_flag']")
	_dropshipper_name_loc = (By.XPATH, "//*[@class='dropship_dtl']/input[1]")
	_dropshipper_telp_loc = (By.XPATH, "//*[@class='dropship_dtl']/input[2]")

	def open(self, site=""):
		self._open(site, self._pl)

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
			elif self.payment == "Partial Deposit":
				id_payment = self._id_trfbank
				print("Payment with Partial Deposit")
			element1 = WebDriverWait(self.driver, 10).until(
					EC.presence_of_element_located((By.ID, id_payment))
				)
			element1.click()
		except Exception as inst:
			print(inst)
	
	def choose_partial_deposit(self, number):
		try:			
			time.sleep(3)
			self.driver.find_element(*self._partial_deposit_check_loc).click()
			print("Partial deposit", number)
			time.sleep(1)
			self.driver.find_element(*self._partial_deposit_amount_loc).send_keys(number)
		except Exception as inst:
			print(inst)

	def dropshipper(self, name, telp):
		try:
			time.sleep(2)
			self.driver.find_element(*self._dropshipper_checked_loc).click()
			time.sleep(1)
			print("Dropshipper name " + name +  ", telp " + telp)
			self.driver.find_element(*self._dropshipper_name_loc).send_keys(name)
			self.driver.find_element(*self._dropshipper_telp_loc).send_keys(telp)
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
			if self.payment == "Deposit" or self.payment == "Partial Deposit":
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

