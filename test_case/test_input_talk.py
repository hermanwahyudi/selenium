#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from main.activity.activity_login import *
from main.activity.activity_talk_product import *
from main.page.shop.pe_shop import *
from main.page.product.pe_product import *
from main.page.product.pe_talk_product import *
from main.function.setup import *


class TestInputTalk(unittest.TestCase):
	_site = "live"

	dict_sender = {
		"email" : "tkpd.qc+29@gmail.com",
		"password" : "cumicumi"
	}

	dict_receiver = {
		"email" : "tkpd.qc+29a@gmail.com",
		"password" : "cumicumi"
	}

	target_shop = 'testqc29a'

	#Buka file output yang menyimpan nomor last attempt
	file_count = open('test_input_talk_counter.txt','r+')
	counter_old = file_count.read()
	file_count.close()
	counter = int(counter_old)


	def setUp(self):
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		self.driver = tsetup('phantomjs')
		self.login = loginActivity()
		self.talk_product = talkProductActivity()
		

	#Test buyer memulai diskusi
	def test_start_discussion(self):
		self.counter = self.counter+1 #increment test attempt number
		self.counter = str(self.counter)
		print('==========================')
		print('TEST #1: SEND TALK MESSAGE')
		print('==========================')
		print('SENDER SIDE')
		print('This is test attempt #' + self.counter)
		self.login.do_login(self.driver, self.dict_sender['email'], self.dict_sender['password'], self._site)
		self.talk_product.setObject(self.driver)
		new_msg_id = self.talk_product.test_input_talk(self.driver, self._site, self.target_shop, self.counter) #return 'none' kalo ga ada isinya, return list of message ID kalo ada
		self.driver.close()
		print('SENDER ACTIVITY DONE')
		print('==========================')
		print('RECEIVER ACTIVITY')
		self.driver = tsetup('phantomjs')
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		self.talk_product.setObject(self.driver)
		self.login.do_login(self.driver, self.dict_receiver['email'], self.dict_receiver['password'], self._site)
		self.talk_product.test_if_message_received(self.driver, self._site, new_msg_id)
		#save last attempt number to output file
		counter_new = str(self.counter)
		file_output = open('test_input_talk_counter.txt','w')
		file_output.write(counter_new)
		file_output.close()


	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.quit()
		#test

# main
if(__name__ == "__main__"):
	unittest.main()
