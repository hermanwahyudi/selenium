#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from main.page.login.pe_login import *
from main.page.shop.pe_shop import *
from main.activity.activity_inbox_message import *
from main.activity.activity_login import *
from main.activity.activity_send_message import *
from main.function.setup import *



class TestSendMessage(unittest.TestCase):

	_site = "live"
	_domain_shop = "testqc29b"
	count = 1

	dict_user = {
		"email" : "tkpd.qc+29a@gmail.com",
		"password" : "cumicumi"
	}

	dict_receiver = {
		"email" : "tkpd.qc+29b@gmail.com",
		"password" : "cumicumi"
	}

	def setUp(self):
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		
		self.driver = tsetup('phantomjs')
		self.login = loginActivity()
		self.shop = ShopPage(self.driver)
		self.message = sendMessageActivity()
		self.inbox = inboxMessageActivity()
	#def test_do_fav_shop(self):

	def test_flow_send_message(self):
		new_sent_msg_list=[]
		print('==================================')
		print('TEST #1 : SEND MESSAGE VIA PRODUCT')
		print('==================================')
		print('!SENDER SIDE!')
		self.login.do_login(self.driver, self.dict_user['email'], self.dict_user['password'], self._site)
		print('++CHECK INBOX SENT BEFORE SEND MESSAGE++')
		old_sent_msg_list, total_old_msg_list = self.inbox.get_list_sent_message(self.driver, self._site)
		print('')
		print('++GO TO TARGET SHOP++')
		self.shop.domain(self._site, self._domain_shop)
		print('')
		print('++SEND MESSAGE++')
		subject, message_prev = self.message.send_message(self.driver, self.count)
		#self.message.send_message(self.driver, self.count, self._domain_shop, self._site)
		time.sleep(10)
		print('')
		print('++CHECK INBOX SENT AFTER SEND MESSAGE++')
		new_sent_msg_list, total_new_msg_list = self.inbox.get_list_sent_message(self.driver, self._site)
		#check is message sent
		stat_sent_msg, total_new_sent_msg, new_sent_msg = self.message.is_message_sent(self.driver, total_old_msg_list, total_new_msg_list, new_sent_msg_list, subject, message_prev)
		print('status sent message : ' + str(stat_sent_msg))
		print('Total New Sent Message : ' + str(total_new_sent_msg))
		print(new_sent_msg)
		self.driver.close()
		time.sleep(10)
		print('')
		print('!RECEIVER SIDE!')
		self.driver = tsetup('phantomjs')
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		self.login.do_login(self.driver, self.dict_receiver['email'], self.dict_receiver['password'], self._site)
		self.inbox.is_message_received(self.driver, self._site, new_sent_msg)

	"""def test_bypass_captcha(self):
		new_sent_msg_list=[]
		print('==================================')
		print('TEST #1 : SEND MESSAGE VIA PRODUCT')
		print('==================================')
		print('!SENDER SIDE!')
		self.login.do_login(self.driver, self.dict_user['email'], self.dict_user['password'], self._site)
		print('++CHECK INBOX SENT BEFORE SEND MESSAGE++')
		old_sent_msg_list, total_old_msg_list = self.inbox.get_list_sent_message(self.driver, self._site)
		print('')
		print('++GO TO TARGET SHOP++')
		self.shop.domain(self._site, self._domain_shop)
		print('')
		print('++SEND MESSAGE++')
		subject, message_prev = self.message.send_message(self.driver, self.count)
		#self.message.send_message(self.driver, self.count, self._domain_shop, self._site)
		time.sleep(5)
		print('++CHECK INBOX SENT AFTER SEND MESSAGE++')
		new_sent_msg_list, total_new_msg_list = self.inbox.get_list_sent_message(self.driver, self._site)
		#check is message sent
		stat_sent_msg, total_new_sent_msg, new_sent_msg = self.message.is_message_sent(self.driver, total_old_msg_list, total_new_msg_list, new_sent_msg_list, subject, message_prev)
		self.driver.close()
		time.sleep(5)"""

	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.quit()

# main
if(__name__ == "__main__"):
	unittest.main()
