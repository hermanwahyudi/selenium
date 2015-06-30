import os,sys
from main.page.base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.page.inbox_message.pe_inbox_message import *
from main.page.inbox_message.pe_message_details import *
from random import randint
import time

class inboxMessageActivity():
	def goto_inbox_message(self, driver, site):
		inbox_message = InboxMessagePage(driver)
		inbox_message.open(site)
		print('masuk inbox-message.pl')
		#inbox_message_page.check_message_exists()
		"""inbox_message.select_filter_unread()
		print('masuk filter unread')
		time.sleep(5)
		inbox_message.select_tab_inbox()
		print('masuk tab inbox')
		inbox_message.select_tab_archive()
		print('masuk tab archive')
		inbox_message.select_tab_sent()
		print('masuk tab sent')
		inbox_message.select_tab_trash()
		print('masuk tab trash')"""


	def get_list_sent_message(self, driver, site):
		list_sent_msg_ID = []
		next_list_sent_msg_ID = []
		try:
			inbox_message = InboxMessagePage(driver)
			inbox_message.open(site)
			inbox_message.select_tab_sent()
			#get list of sent message ID in first page
			list_sent_msg = inbox_message.get_list_message()
			for i in list_sent_msg:
				list_sent_msg_ID.append(i.get_attribute('id'))
			#check is next page available
			is_next_page_exists = inbox_message.next_button_element()
			while is_next_page_exists == 1: #if next page available
				inbox_message.click_next_button()
				time.sleep(5)
				next_list_sent_message = inbox_message.get_list_message()
				for i in next_list_sent_message:
					list_sent_msg_ID.append(i.get_attribute('id'))
				is_next_page_exists = inbox_message.next_button_element()
			#endwhile
			print('End of inbox page')
			print('List of sent message ID has been successfully populated ...')
			total = len(list_sent_msg_ID)
			print('Total Sent Messages : ' + str(total))
			return(list_sent_msg_ID, total)
		except NoSuchElementException:
			total = len(list_sent_msg_ID)
			print('Total Sent Message : ' + str(total))
			return(list_sent_msg_ID, total)


	def get_list_unread_message(self, driver, site):
		try:
			inbox_message = InboxMessagePage(driver)
			inbox_message.open(site)
			list_unread_msg_ID = []
			next_list_unread_msg_ID = []
			inbox_message.select_tab_inbox()
			inbox_message.select_filter_unread()
			list_unread_msg = inbox_message.get_list_message()
			for i in list_unread_msg:
				list_unread_msg_ID.append(i.get_attribute('id'))
			#check next page in first page
			next = inbox_message.next_button_element()
			while next == 1:
				inbox_message.click_next_button()
				time.sleep(5)
				next = inbox_message.next_button_element()
				next_list_unread_message = inbox_message.get_list_message()
				for i in next_list_unread_message:
					list_unread_msg_ID.append(i.get_attribute('id'))
			#endwhile
			print('End of inbox page')
			print('List of unread message ID has been successfully populated ...')
			total = len(list_unread_msg_ID)
			print('Total Unread Message : ' + str(total))
			return(list_unread_msg_ID, total)
		except NoSuchElementException:
			total = len(list_unread_msg_ID)
			print('Total Unread Message : ' + str(total))
			return(list_unread_msg_ID, total)


	def is_message_received(self, driver, site, msg_ID):
		inbox_message = InboxMessagePage(driver)
		list_unread_msg_ID, total_list_unread = self.get_list_unread_message(driver, site)
		msg_received = [] #create list of received message
		print('msg_ID : ')
		print(msg_ID)
		for i in msg_ID:
			print(i)
			for j in list_unread_msg_ID:
				print('j: ')
				print(j)
				if i==j:
					msg_received.append(i)
					break
				else:
					pass
		print('msg_received :')
		for i in msg_received:
			print(i)
		total_msg_received = len(msg_received)
		total_msg_ID = len(msg_ID)
		print(str(total_msg_received) + ' out of ' + str(total_msg_ID) + ' message(s) received from previous test flow.')
		if total_msg_received == total_msg_ID and total_msg_received!=0:
			print('All message is successfully received')
		else:
			diff = total_msg_ID - total_msg_received #to count how many message that is not received
			print(str(diff) + ' message(s) is not received')


	#need improvement: Add check all message, archived, and trash
	def check_sent_message_status(self, driver, site):
		inbox_message = InboxMessagePage(driver)
		inbox_message.open(site)
		print('----- Cek Inbox Sent Status -----')
		self.get_list_sent_message(driver, site)
		#print('Total Sent Message = ' + str(total))

	#ongoing
	def check_message_details(self, driver, site):
		flag = 0
		inbox_message = InboxMessagePage(driver)
		message_details = PageMessageDetails(driver)
		inbox_message.open(site)
		inbox_message.select_filter_unread()
		unread_message, total_unread_message = self.get_list_unread_message(driver, site)
		#get index of messages in last page
		last_page_message_list = inbox_message.get_list_message()
		last_page_message_list_ID = []
		for i in last_page_message_list:
			last_page_message_list_ID.append(i.get_attribute('id'))
		total_last_page_message_list = len(last_page_message_list_ID)
		print(last_page_message_list_ID)
		inbox_message.click_message(last_page_message_list_ID, total_last_page_message_list)
		#check elements in message details
		time.sleep(5)
		try:
			message_details.locate_message_header()
			print('Header exists.')
			message_details.locate_current_shop()
			print('[Your Shop Name] exists.')
			message_details.locate_sender_name_header()
			message_details.locate_sender_name_small()
			print('Sender name exists.')
			message_details.locate_textarea()
			print('Textarea exists.')
			message_details.locate_reply_button()
			print('Reply button exists.')
			msg_content = message_details.get_message_content()
			print(msg_content)
			print('----')
			print('All component exists.')
		except Exception as inst:
			print(inst)
		message_details.click_back_button()
		unread_message_new, total_unread_message_new = self.get_list_unread_message(driver, site)
		for i in unread_message_new:
			if i==unread_message:
				flag = 1
				print('CAUTION! ' + str(unread_message) + 'STILL EXISTS IN UNREAD MSG LIST. IT SHOULD HAVE BEEN REMOVED.')
				break
			else:
				pass
		if flag!=1:
			print('Message has been successfully read')

	def is_message_contains_blacklisted_links(self, driver, site, sent_msg_ID, sent_message):
		inbox_message = InboxMessagePage(driver)
		message_details = PageMessageDetails(driver)
		sent_msg_ID = sent_msg_ID[0]
		print(sent_msg_ID)
		inbox_message.open(site)
		inbox_message.select_filter_unread()
		unread_message = inbox_message.get_list_message() #get unread message in first page
		total_unread_message = len(unread_message)
		inbox_message.click_message(unread_message, total_unread_message, sent_msg_ID) #click message with ID = sent_msg_ID
		time.sleep(3)
		#start checking
		sent_message = str.split(sent_message)
		msg_content_small = str.split(message_details.get_message_content_small())
		msg_content_small_count = len(msg_content_small)
		received_message = str.split(message_details.get_message_content())
		received_message = received_message[msg_content_small_count:]
		file_w = open('whitelist.txt','r')
		file_b = open('blacklist.txt', 'r')
		file_whitelist = file_w.read().splitlines()
		file_blacklist = file_b.read().splitlines()
		file_w.close()
		file_b.close()
		print(file_whitelist)
		print(file_blacklist)
		print(sent_message)
		print(received_message)
		if len(sent_message) ==  len(received_message):
			print('test')
			for word in sent_message:
				#for every words in message, first check if it contains link in blacklist
				for link in file_blacklist:
					if link in word: #if the word contains banned link
						idx = sent_message.index(word) #get message index
						uncensored_word = word[len(link):] #get uncensored words
						print ('uncensored word = ' + uncensored_word)
						received_msg = '[LINK]' + uncensored_word
						if sent_message[idx]==word and received_message[idx]==received_msg:
							print('Link tertangkap: ' + sent_message[idx])
							print('message diterima: ' + received_message[idx])
							print('Link is censored\n')
						else:
							print('Link tertangkap: ' + sent_message[idx])
							print('message diterima: ' + received_message[idx])
							print('Salah\n')
						break
					else:
						pass #check next blacklist
				#for every words in message, first check if it contains link in whitelist
				for link in file_whitelist:
					if link in word: #if the word contains white link
						idx = sent_message.index(word)
						if sent_message[idx]==word and received_message[idx]==word:
							print('Link tertangkap: ' + sent_message[idx])
							print('message diterima: ' + received_message[idx])
							print('Link is in whitelist\n')
						else:
							print('Link tertangkap: ' + sent_message[idx])
							print('message diterima: ' + received_message[idx])
							print('Salah\n')
						break
					else:
						pass #check next whitelist
