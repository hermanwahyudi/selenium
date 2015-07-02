import os,sys, re
from main.page.base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
import time

class InboxMessagePage(BasePage):
	#url = "https://www.tokopedia.com/inbox-message.pl"
	_pl = "inbox-message.pl"

	#Locators
	_filter_all_loc = (By.CSS_SELECTOR, 'div#message-box div.row-fluid div.span12 span.pull-left small a#filter-all')
	_filter_unread_loc = (By.CSS_SELECTOR, 'div#message-box div.row-fluid div.span12 span.pull-left small a#filter-unread')
	_archive_button_upper_loc = (By.XPATH, '//*[@id="message"]/div/div[1]/a[1]')
	_delete_button_upper_loc = (By.XPATH, '//*[@id="message"]/div/div[1]/a[2]')
	_archive_button_lower_loc = (By.XPATH, '//*[@id="message"]/div/div[2]/a[1]')
	_delete_button_lower_loc = (By.XPATH, '//*[@id="message"]/div/div[2]/a[2]')
	#_next_page_button_loc = (By.XPATH, '//*[@id="message-box"]/div[3]/div[2]/div/ul/li/a')

	_list_of_next_button_loc = (By.CSS_SELECTOR, 'div.row-fluid.clear-b div.span7.text-right div.pagination ul li')
	_next_page_button_loc = (By.CSS_SELECTOR, 'div.row-fluid.clear-b div.span7.text-right div.pagination ul li a')
	_next_page_button_loc_1 = (By.CSS_SELECTOR, 'div.row-fluid.clear-b div.span7.text-right div.pagination ul li:nth-child(1) a')
	_next_page_button_loc_2 = (By.CSS_SELECTOR, 'div.row-fluid.clear-b div.span7.text-right div.pagination ul li:nth-child(2) a')

	#Tab Locators
	_tab_inbox_loc = (By.CSS_SELECTOR, 'div.maincontent-admin ul.horizontal-tab li.active a#tab-nav-inbox')
	_tab_sent_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[2]/a')
	_tab_archive_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[3]/a')
	_tab_trash_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[4]/a')

	#Message Content
	_msg_box = (By.XPATH, "//tr[starts-with(@id, 'msg-id-')]")
	#_msg_list = (By.XPATH, '//*[@id="message"]/div/table/tbody')
	_msg_list = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/div[2]/div/table/tbody/tr')
	#_msg_list = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div[2]/div[2]/div/table/tbody/tr') #for testing in devel

	#Actions

	#Buka site
	def open(self, site, _pl=""):
		self._open(site, self._pl)

	#Pilih tab inbox
	def select_tab_inbox(self):
		tab_inbox_loc = self.find_element(*self._tab_inbox_loc)
		self._click(tab_inbox_loc)

	#Pilih tab sent
	def select_tab_sent(self):
		"""tab_sent_loc = self.find_element(*self._tab_sent_loc)
		self._click(tab_sent_loc)"""
		self.find_element(*self._tab_sent_loc).click()

	def select_tab_archive(self):
		tab_archive_loc = self.find_element(*self._tab_archive_loc)
		self._click(tab_archive_loc)

	def select_tab_trash(self):
		tab_trash_loc = self.find_element(*self._tab_trash_loc)
		self._click(tab_trash_loc)

	#Next button (general)
	def next_button_element(self):
		#case1: first page, only next page button available, or last page
		list_page_button = self.find_elements(*self._list_of_next_button_loc)
		if len(list_page_button) == 1:
			if self.find_element(*self._next_page_button_loc).text == '>':
				print('Next page available')
				return(1)
			else:
				print('Next page not found')
				return(0)
		elif len(list_page_button) == 2: #case2: n-th page, next and previous page button available
			print('Next page available')
			return(1)


	def click_next_button(self):
		list_page_button = self.find_elements(*self._list_of_next_button_loc)
		if len(list_page_button) == 1:
			if self.find_element(*self._next_page_button_loc).text == '>': #next page available in first page
				self.find_element(*self._next_page_button_loc).click()
			else:
				pass
		elif len(list_page_button) == 2:
			self.find_element(*self._next_page_button_loc_2).click()
		else:
			pass

	def select_filter_unread(self):
		filter_unread_loc = self.find_element(*self._filter_unread_loc)
		try:
			WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self._filter_unread_loc))
			print ("JS clickable")
			self.click_on_javascript(filter_unread_loc)
		except:
			print ("JS not found")
		time.sleep(5)


	def check_message_exists(self):
		self.check_visible_element(*self._msg_box)
		message_found = self.find_element(*self._msg_box)
		try:
			if message_found.is_displayed():
				print ("Message found!")
		except NoSuchElementException:
			print ("No Message Found!")

	def get_list_message(self):
		list_message = []
		try:
			list_message = self.find_elements(*self._msg_list)
			return(list_message)
		except NoSuchElementException:
			return(list_message)

	#count message
	def message_counts(self, list_msg):
		total_message = len(list_msg)
		return(total_message)

	#get message subject
	def get_message_subject(self, msg_ID):
		subject_css = '//*[@id="' + msg_ID + '"]/td[3]/a'
		subject_preview = self.driver.find_element(By.XPATH, subject_css).text
		return(subject_preview)

	#get message preview
	def get_message_preview(self, msg_ID):
		prev_css = '//*[@id="' + msg_ID + '"]/td[3]/small'
		content_preview = self.driver.find_element(By.XPATH, prev_css).text
		return(content_preview)

	#message option

	def click_message(self, msg_ID_list, total_msg, msg_ID=""): #msg_ID is optional
		if msg_ID=="":
			i, length = 0, total_msg-1
			rand = randint(i, length)
			css = 'div#message div.span12 table.mt-20 tbody tr#' + str(msg_ID_list[rand]) + ' td.topic.td-inbox-msg a'
			print(css)
			self.find_element(By.CSS_SELECTOR, css).click()
			print('Opening message...')
		else:
			css = 'div#message div.span12 table.mt-20 tbody tr#' + str(msg_ID) + ' td.topic.td-inbox-msg a'
			print(css)
			self.find_element(By.CSS_SELECTOR, css).click()
			print('Opening message...')
