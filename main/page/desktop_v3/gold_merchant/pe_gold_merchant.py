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

class GoldMerchantPage(BasePage):

	_page = "https://gold.tokopedia.com/"

	# locator
	_gm_three_month_loc = (By.XPATH, "/html/body/div[3]/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[4]/button")
	_gm_six_month_loc = (By.XPATH, "/html/body/div[3]/div[1]/div/div/div/div/div/div[2]/form/div[2]/div[4]/button")
	_gm_one_year_loc = (By.XPATH, "/html/body/div[3]/div[1]/div/div/div/div/div/div[2]/form/div[3]/div[4]/button")
	_gm_two_year_loc = (By.XPATH, "/html/body/div[3]/div[1]/div/div/div/div/div/div[2]/form/div[4]/div[4]/button")
	
	def open(self, site=""):
		self._open(site, self._page)

	def choose_three_month_gm(self):
		try:
			self.driver.find_element(*self._gm_three_month_loc).click()
		except Exception as ins:
			print("Exception in choose Three Month GM", inst)

	def choose_six_month_gm(self):
		try:
			self.driver.find_element(*self._gm_six_month_loc).click()
		except Exception as ins:
			print("Exception in choose Six Month GM", inst)

	def choose_one_year_gm(self):
		try:
			self.driver.find_element(*self._gm_one_year_loc).click()
		except Exception as ins:
			print("Exception in choose One Year GM", inst)

	def choose_two_year_gm(self):
		try:
			self.driver.find_element(*self._gm_two_year_loc).click()
		except Exception as ins:
			print("Exception in choose Three Month GM", inst)

	def __str__(self):
		return self.driver.title
