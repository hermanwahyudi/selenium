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

class GoldCartPage(BasePage):

	_page = "gold-cart.pl"
	
	def open(self, site=""):
		self._open(site, self._page)