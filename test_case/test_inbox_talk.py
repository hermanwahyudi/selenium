import time, unittest, os, sys
from selenium import webdriver
from main.activity.activity_login import *
from main.activity.activity_inbox_talk import *
from main.page.inbox_talk.pe_inbox_talk import *
from main.function.driver import *


class TestInboxTalk(unittest.TestCase):

	_site = "live"

	dict_user = {
		"email" : "tkpd.qc+29b@gmail.com",
		"password" : "cumicumi"
	}

	def setUp(self):
		#self.driver = useDriver("firefox")
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		self.driver = useDriver("phantomjs")
		self.login = loginActivity()
		self.inbox_talk = inboxTalkActivity()

	def test_initial_checking(self):
		print('=====================================')
		print('TEST #1 : INITIAL TALK INBOX CHECKING ')
		print('=====================================')
		self.login.do_login(self.driver, self.dict_user['email'], self.dict_user['password'], self._site)
		self.inbox_talk.setObject(self.driver)
		print('')
		print('--Menguji apakah ada pesan diskusi dalam inbox (is Talk exist)--')
		self.inbox_talk.is_talk_discussion_exists(self._site)
		print('')
		print('--Periksa nilai counter talk dengan jumlah unread message sesungguhnya--')
		self.inbox_talk.is_counter_works(self._site)
		print('========================================================================')

	#TEST #2 Reply talk (3 cycle)
	#TEST #3 Delete talk
	#TEST #4 Unfollow Talk

	def tearDown(self):
		print("Test akan berakhir dalam beberapa saat...")
		time.sleep(5)
		self.driver.quit()

# main
if(__name__ == "__main__"):
	unittest.main()