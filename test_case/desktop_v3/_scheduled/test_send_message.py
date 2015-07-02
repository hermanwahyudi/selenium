#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from main.page.desktop_v3.login.pe_login import *
from main.page.desktop_v3.shop.pe_shop import *
from main.activity.desktop_v3.activity_inbox_message import *
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_send_message import *
from utils.function.setup import *
from utils.lib.user_data import *



class TestSendMessage(unittest.TestCase):

	_site = "live"
	_domain_shop = user11['domain']
	count = 1

	

	def setUp(self):
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		
		self.driver = tsetup('firefox')
		self.login = loginActivity()
		self.shop = ShopPage(self.driver)
		self.message = sendMessageActivity(self.driver)
		self.inbox = inboxMessageActivity()
		self.sender = user10
		self.receiver = user11
	#def test_do_fav_shop(self):

	def test_flow_send_message(self):
		new_sent_msg_list=[]
		print('==================================')
		print('TEST #1 : SEND MESSAGE VIA PRODUCT')
		print('==================================')
		print('!SENDER SIDE!')
		self.login.do_login(self.driver, self.sender, self.sender['email'], self.sender['password'], self._site)
		print('++CHECK INBOX SENT BEFORE SEND MESSAGE++')
		old_sent_msg_list, total_old_msg_list = self.inbox.get_list_sent_message(self.driver, self._site)
		print('')
		print('++GO TO TARGET SHOP++')
		self.shop.domain(self._site, self._domain_shop)
		print('')
		print('++SEND MESSAGE++')
		time.sleep(2)
		subject, message_prev = self.message.send_message(self.driver, self.count)
		#self.message.send_message(self.driver, self.count, self._domain_shop, self._site)
		print('')
		print('++CHECK INBOX SENT AFTER SEND MESSAGE++')
		new_sent_msg_list, total_new_msg_list = self.inbox.get_list_sent_message(self.driver, self._site)
		#check is message sent
		stat_sent_msg, total_new_sent_msg, new_sent_msg = self.message.is_message_sent(self.driver, total_old_msg_list, total_new_msg_list, new_sent_msg_list, subject, message_prev)
		print('status sent message : ' + str(stat_sent_msg))
		print('Total New Sent Message : ' + str(total_new_sent_msg))
		print(new_sent_msg)
		self.driver.close()
		print('')
		print('!RECEIVER SIDE!')
		self.driver = tsetup('firefox')
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		self.login.do_login(self.driver, self.receiver, self.receiver['email'], self.receiver['password'], self._site)
		self.inbox.is_message_received(self.driver, self._site, new_sent_msg)
		self.inbox.is_message_contains_blacklisted_links(self.driver, self._site, new_sent_msg, message_prev)

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
