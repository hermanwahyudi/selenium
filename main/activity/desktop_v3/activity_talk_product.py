from main.page.desktop_v3.header import *
from main.page.base import *
from selenium import webdriver
from main.page.desktop_v3.product.pe_talk_product import *
from main.page.desktop_v3.product.pe_product import *
from main.page.desktop_v3.shop.pe_shop import *
from main.activity.desktop_v3.activity_inbox_talk import *
from main.activity.desktop_v3.activity_login import *
from main.page.desktop_v3.login.pe_login import *
from main.page.desktop_v3.login.pe_logout import *
from utils.lib.user_data import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException



class talkProductActivity:
	def __init__(self, driver):
		self.login = LoginPage(driver)
		self.logout = LogoutPage(driver)
		self.shop = ShopPage(driver)
		self.prod = ProductPage(driver)
		self.talk = TalkProductPage(driver)
		self.inbox = inboxTalkActivity()
		self.inbox.setObject(driver)
		

	def set_parameter(self, parameter):
		self.dict = parameter
		self.sender = self.dict['sender']
		self.receiver = self.dict['receiver']

	def test_input_talk(self, driver, site, talk_message):
		self.login.open(site)
		self.login.do_login(self.sender['email'], self.sender['password'])
		if self.dict['end_to_end'] == True:
			print('Sending talk end-to-end\n')
			print("SENDER ACTIVITY")
			self.shop.domain(site, self.receiver['domain'])
			print('Entered Shop' + str(self.receiver['domain']))
			print('Randomly choose product')
			self.shop.choose_product()
			self.prod.go_to_talk() #enter discussion tab
			print('Entered talk tab')
			time.sleep(1)
			total_message_old = self.talk.get_jumlah_message()
			print('Total Talk (old): ' + str(total_message_old))
			self.talk.input_talk(talk_message)
			try:
				total_message_new = self.talk.get_jumlah_message()
				print('Total Talk (new): ' + str(total_message_new))
				end_of_list = total_message_new - total_message_old
				print(end_of_list)
				new_ID_message = self.talk.list_new_message(end_of_list)
			except TimeoutException:
				print ('Loading time too long. Test terminated.')
				new_ID_message = 'none'
			except NoSuchElementException:
				print ('Element Not Found. Test terminated.')
				new_ID_message = 'none'
			self.logout.open(site)
			print('SENDER ACTIVITY DONE')
			print('==========================')
			print('RECEIVER ACTIVITY')
			self.login.open(site)
			self.login.do_login(self.receiver['email'], self.receiver['password'])
			time.sleep(2)
			self.inbox.is_message_received(site, new_ID_message)
		elif self.dict['end_to_end'] == False:
			n = 0
			while n < self.dict['loop']:
				print("Auto Send Talk #" + str(n+1))
				self.shop.domain(site, self.receiver['domain'])
				print('Entered Shop' + str(self.receiver['domain']))
				self.shop.choose_product()
				print('Choose random product')
				self.prod.go_to_talk() #enter discussion tab
				print('Entered talk tab')
				time.sleep(1)
				self.talk.input_talk(talk_message)
				n+=1
				time.sleep(15)
				print("")
