import time, unittest, os, sys
from selenium import webdriver
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_inbox_talk import *
from main.page.desktop_v3.inbox_talk.pe_inbox_talk import *
from utils.function.setup import *
from utils.function.logger import *
from utils.lib.user_data import *


class TestInboxTalk(unittest.TestCase):

	_site = "live"

	def setUp(self):
		#self.driver = useDriver("firefox")
		#self.driver = webdriver.Chrome("C:\driver\chromedriver\chromedriver.exe")
		self.driver = tsetup("phantomjs")
		#sys.stdout = Logger()
		self.login = loginActivity()
		self.inbox_talk = inboxTalkActivity()
		

	def test_initial_checking(self):
		print('=====================================')
		print('TEST #1 : INITIAL TALK INBOX CHECKING ')
		print('=====================================')
		self.login.do_login(self.driver, user6['user_id'], user6['email'], user6['password'], self._site)
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