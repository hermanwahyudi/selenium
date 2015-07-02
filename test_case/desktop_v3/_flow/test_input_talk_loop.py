#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_talk_product import *
from main.page.desktop_v3.shop.pe_shop import *
from main.page.desktop_v3.product.pe_product import *
from main.page.desktop_v3.product.pe_talk_product import *
from utils.function.setup import *
from utils.lib.user_data import *
from random import randint


class TestInputTalk(unittest.TestCase):
	_site = "beta"

	target_shop = user6['domain']
	randomshop = ['testqc29b']
	talk_message = 'asdfghjklmnbvcxzwertyuii #' + ' http://cumiiii1' + str(randint(0,9999)) + '.com'
	cycle = 2


	def setUp(self):
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		self.driver = tsetup('firefox')
		self.login = loginActivity()
		self.talk_product = talkProductActivity()
		self.sender = user5
		
	def test_input_talk_loop(self):
		n = 0
		self.login.do_login(self.driver, self.sender, self.sender['email'], self.sender['password'], self._site)
		self.talk_product.setObject(self.driver)
		while n < self.cycle:
			print('This is test attempt #' + str(n+1))
			#self.target_shop = self.randomshop[randint(0,len(self.randomshop))]
			new_msg_id = self.talk_product.test_input_talk(self.driver, self._site, self.target_shop, self.talk_message)
			time.sleep(15)
			print("")
			n+=1


	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.quit()
		#test

# main
if(__name__ == "__main__"):
	unittest.main()
