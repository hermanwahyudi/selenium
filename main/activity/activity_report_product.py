#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from main.page.login.pe_login import *
from main.page.login.pe_logout import *
from main.page.shop.pe_shop import *
from main.page.product.pe_product import *

class ReportProductActivity:

	def __init__(self, driver):
		self.login = LoginPage(driver)
		self.logout = LogoutPage(driver)
		self.shop = ShopPage(driver)
		self.prod = ProductPage(driver)

	def set_parameter(self, param):
		self.dict = param

	def set_report_product(self, category, desc):
		self.login.open(self.dict['site'])
		self.login.do_login(self.dict['email_buyer'], self.dict['password_buyer'])
		self.shop.domain(self.dict['site'], self.dict['domain_shop'])
		self.shop.choose_product()
		i = 0
		while i < self.dict['loop']:
			print("Report product", self.dict['category'], (i+1))
			self.prod.report_product(category, desc)
			i += 1