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

	talk_message = 'asdfghjklmnbvcxzwertyuii #' + ' http://cumiiii1' + str(randint(0,9999)) + '.com'

	dict = {
		"site" : "live",
		"end_to_end" : True, #True: the default to test Talk with end-to-end process, False: For sending multiple talk 
		"loop" : 3, #Only used for multiple talk
		"sender" : user5,
		"receiver" : user6
	}

	def setUp(self):
		self.driver = tsetup('phantomjs')
		self.talk = talkProductActivity(self.driver)
		self.talk.set_parameter(self.dict)


	def test_input_talk(self):
		print('==========================')
		print('TEST: SEND TALK')
		print('==========================')
		self.talk.set_parameter(self.dict) #initialization
		self.talk.test_input_talk(self.driver, self.dict['site'], self.talk_message)


	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.quit()
		#test

# main
if(__name__ == "__main__"):
	unittest.main()
