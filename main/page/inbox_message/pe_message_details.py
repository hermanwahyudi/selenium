import os, sys
from main.page.inbox_message.pe_inbox_message import *
from selenium.webdriver.common.by import By

class PageMessageDetails(InboxMessagePage):

	#locators
	_msg_header_loc = (By.CSS_SELECTOR, 'div.row-fluid div.span12 h3')
	_current_shop_loc = (By.CSS_SELECTOR, 'div.row-fluid div.span12 a:nth-of-type(1)')
	_sender_name_h2_loc = (By.CSS_SELECTOR, 'div.row-fluid div.span12 a:nth-of-type(2)')
	_sender_name_small_loc = (By.CSS_SELECTOR,'div.message-holder p span small a')
	#_msg_content_loc = (By.CSS_SELECTOR, 'div.message-holder p.span10 span')
	_msg_content_loc = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div/div/p/span')
	_msg_content_small_loc = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div/div/p/span/small')
	_textarea_loc = (By.CSS_SELECTOR, 'div.inbox-message-subthread div.row-fluid div.span12 textarea:nth-of-type(2)')
	_reply_btn_loc = (By.CSS_SELECTOR, 'div.inbox-message-subthread div.row-fluid div.span12 button')
	_back_btn_loc = (By.CSS_SELECTOR, 'div.maincontent-admin a.pull-left.mb-20')

	#locating message header element #will be used for element asserts
	def locate_message_header(self):
		self.find_element(*self._msg_header_loc)

	#get the value of message header
	def get_message_header(self):
		header = self.locate_message_header.text
		return(header)

	def locate_current_shop(self):
		self.find_element(*self._current_shop_loc)

	#current shop name
	def get_current_shop(self):
		current_shop = self.locate_current_shop().text
		return(current_shop)

	#sender name (small)
	def locate_sender_name_header(self):
		self.find_element(*self._sender_name_h2_loc)

	def locate_sender_name_small(self):
		self.find_element(*self._sender_name_small_loc)

	def get_sender_name_small(self):
		sender_name_s = self.locate_current_shop.text
		return(sender_name_s)

	def locate_message_content(self):
		elmt = self.find_element(*self._msg_content_loc)
		return(elmt)
	
	def get_message_content_small(self):
		text = self.find_element(*self._msg_content_small_loc).text
		return(text)

	def get_message_content(self):
		#text = self.locate_message_content().text
		text = self.find_element(*self._msg_content_loc).text
		return(text)

	def locate_textarea(self):
		self.find_element(*self._textarea_loc)

	def locate_reply_button(self):
		self.find_element(*self._reply_btn_loc)

	def click_reply_button(self):
		self.locate_reply_button().click

	def click_back_button(self):
		self.find_element(*self._back_btn_loc).click()




