import time, unittest, os, sys
from selenium import webdriver
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_talk_product import *
from main.page.desktop_v3.shop.pe_shop import *
from main.page.desktop_v3.product.pe_product import *
from main.page.desktop_v3.product.pe_talk_product import *
from main.page.desktop_v3.login.pe_login import *
from main.activity.desktop_v3.activity_inbox_message import *
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_send_message import *
from utils.function.setup import *
from utils.lib.user_data import *

class TestDebug(unittest.TestCase):
	_site = "live"

	dict_user = {
		"Napoleon Bonaparte" : "user7",
		"Tony Stark" : "user5",
		"Test Man" : "user6"
	}

	def setUp(self):
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		self.driver = tsetup('firefox')
		self.login = loginActivity()
		self.talk_product = talkProductActivity(self.driver)
		self.inbox_talk = inboxTalkActivity()
		self.shop = ShopPage(self.driver)
		self.message = sendMessageActivity(self.driver)
		self.inbox = inboxMessageActivity()
		#userinfo
		self.sender = user7

	def test_reply_talk(self):
		print('Test Reply')
		print('*SELLER*')
		self.login.do_login(self.driver, self.sender, self.sender['email'], self.sender['password'], self._site)
		self.inbox_talk.setObject(self.driver)
		talk_ID, reply_ID = self.inbox_talk.reply_message(self._site)
		receiver = self.inbox_talk.get_receiver_name(talk_ID)
		self.driver.close()
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		self.driver = tsetup('firefox')
		print('*RECEIVER')
		#Choose Receiver Account
		if receiver=="Napoleon Bonaparte":
			self.receiver = user7
		elif receiver=="Tony Stark":
			self.receiver = user5
		elif receiver=="Test Man":
			self.receiver = user6
		self.login.do_login(self.driver, self.receiver, self.receiver['email'], self.receiver['password'], self._site)
		self.inbox_talk.setObject(self.driver)		
		self.inbox_talk.is_reply_received(self._site, talk_ID, reply_ID)
		

	def tearDown(self):
		print("Testing akan selesai dalam beberapa saat..")
		time.sleep(5)
		self.driver.quit()

# main
if(__name__ == "__main__"):
	unittest.main()