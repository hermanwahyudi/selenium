import time, unittest, os, sys
from selenium import webdriver
from main.activity.activity_inbox_message import *
from main.activity.activity_login import *
from main.function.setup import *

class testInboxMessage(unittest.TestCase):
	_site='live'

	dict_user = {
		"email" : "tkpd.qc+29b@gmail.com",
		"password" : "cumicumi"
	}

	def setUp(self):
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		self.driver = tsetup('phantomjs')
		self.login = loginActivity()
		self.message = inboxMessageActivity()

	#check message status
	def test_1_check_inbox_status(self):
		print('===================================')
		print('TEST #1 : CHECK INBOX - STATUS')
		print('===================================')
		self.login.do_login(self.driver, self.dict_user['email'], self.dict_user['password'], self._site)
		self.message.check_sent_message_status(self.driver, self._site)
		print('Test #1 done.')
		print('')

	#read message
	def test_2_read_message(self):
		print('===================================')
		print('TEST #2 : READ MESSAGE')
		print('===================================')
		self.login.do_login(self.driver, self.dict_user['email'], self.dict_user['password'], self._site)
		self.message.check_message_details(self.driver, self._site)
		print('Test #2 done.')
		print('')

	def tearDown(self):
		print('Testing akan selesai dalam beberapa saat...')
		self.driver.quit()

#main
if __name__ == "__main__":
	unittest.main()