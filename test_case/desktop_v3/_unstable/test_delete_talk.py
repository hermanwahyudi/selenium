import time, unittest, os, sys
from selenium import webdriver
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_inbox_talk import *
from main.activity.desktop_v3.activity_product import *
from main.page.desktop_v3.inbox_talk.pe_inbox_talk import *
from utils.function.setup import *
from utils.lib.user_data import *


class TestDeletetalk(unittest.TestCase):

	_site = "live"

	def setUp(self):
		self.driver = tsetup("firefox")
		self.user = user7
		self.login = loginActivity()
		self.inbox_talk = inboxTalkActivity()
		self.product = ProductActivity()

	def test_delete_talk(self):
		print('============================================')
		print('TEST Talk/004 : DELETE TALK FROM INBOX TALK ')
		print('============================================')
		self.login.do_login(self.driver, self.user, self.user['email'], self.user['password'], self._site)
		self.inbox_talk.setObject(self.driver)
		deleted_talk_ID, product_link, total_list_talk = self.inbox_talk.delete_random_talk(self._site)
		time.sleep(2)
		self.inbox_talk.is_talk_deleted_from_sender_inbox(deleted_talk_ID, total_list_talk)
		self.driver.close()
		print('***Check if the talk is deleted from product***')
		self.driver = tsetup("firefox")
		self.driver.get(product_link)
		self.product.setObject(self.driver)
		self.product.is_talk_deleted_from_product(deleted_talk_ID)
		print('')
		print('=============================================')

	def tearDown(self):
		print("Test will be terminated in a second...")
		time.sleep(5)
		self.driver.quit()


# main
if(__name__ == "__main__"):
	unittest.main()