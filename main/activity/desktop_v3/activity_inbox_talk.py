from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.page.desktop_v3.inbox_talk.pe_inbox_talk import *
from main.page.desktop_v3.index.pe_index import *
from random import randint

import time

class inboxTalkActivity():

	def setObject(self, driver):
		self.inboxtalk = InboxTalkPage(driver)
		self.index = IndexPage(driver)

	def get_receiver_name(self, talk_ID):
		current_user = self.index.check_my_username()
		list_of_replies = self.inboxtalk.get_all_replyID_within_a_talkID(talk_ID)
		print(list_of_replies)
		total_replies = len(list_of_replies)
		if total_replies > 1:
			print('break1')
			index = total_replies - 1
			receiver_name = self.inboxtalk.get_last_reply_sender_name(talk_ID, list_of_replies[index]).text #get the name of last replier
			print('checking...')
			while receiver_name==current_user:
				index-=1
				receiver_name = self.inboxtalk.get_last_reply_sender_name(talk_ID, list_of_replies[index]).text
			#end of while
			print('receiver name = ' + receiver_name)
			return(receiver_name)
		else:
			list_of_replies = []
			receiver_name = self.inboxtalk.get_main_talk_sender(talk_ID).text
			print('receiver name : ' + receiver_name)
			return(receiver_name)


	def is_talk_discussion_exists(self, site):
		self.inboxtalk.open(site)
		#inbox_talk_page.select_filter_all()   #<--masih ngaco nih,perlu di fix (28 Nov 2014)
		self.inboxtalk.select_tab_all()
		self.inboxtalk.select_filter_all()
		self.inboxtalk.check_talk_discussion_exists()
		total = self.inboxtalk.all_message_counts()
		print('Total semua talk message baru yang ada: ' + str(total))
		

	def is_counter_works(self, site):
		self.inboxtalk.open(site)
		print('Masuk Tab Unread')
		counter_value = self.inboxtalk.get_message_counter_value() #nilai di counter pada tab Produk Saya
		actual_number_of_message = self.inboxtalk.unread_message_counts() #jumlah message di tab Produk Saya
		if counter_value == actual_number_of_message:
			print('unread message in counter = ' + str(counter_value))
			print('Actual number = ' + str(actual_number_of_message))
			print('Validation OK')
		else:
			print('unread message in counter = ' + str(counter_value))
			print('Actual number = ' + str(actual_number_of_message))
			print('Validation Not OK')

	def is_message_received(self, site, ID_new_message):
		isMessageReceived = 0
		self.inboxtalk.open(site)
		self.inboxtalk.select_tab_all()
		list_of_unread_msg = self.inboxtalk.list_all_unread_message_ID()
		jml_new_message = len(list_of_unread_msg)
		print(ID_new_message)
		time.sleep(3)
		
		for i in ID_new_message:
			strcompare = i
			for item in list_of_unread_msg: #search ID_new_message in list
				#print(item)
				if item == strcompare:
					isMessageReceived = 1
					unread_flag = self.inboxtalk.get_unread_flag(item)
					break
				else:
					pass
		if (isMessageReceived == 1):
			if unread_flag == 1:
				print('New talk message is successfully received and flagged as unread message')
			else:
				print('New talk message is successfully received but not flagged as unread message')
		else:
			 print('New talk message is not received in receiver inbox')

	def is_reply_shown_after_sent(self, talk_ID): #after reply is sent, check if reply is shown underneath
		self.inboxtalk.select_filter_unread()
		list_reply_ID = self.inboxtalk.get_all_replyID_within_a_talkID(talk_ID)

	#Reply message and check if the reply is immediately shown under main talk
	def reply_message(self, site, talk_ID=""): #talk_ID parameter is optional
		rand = randint(1,9999)
		reply_talk = 'Test balas talk #' + str(rand)
		self.inboxtalk.open(site)
		self.inboxtalk.select_filter_unread()
		list_message = []
		list_replyID = []
		time.sleep(2)
		try:
			list_unread_talk = self.inboxtalk.get_list_message() #get list of unread talk in first page
			end_of_list = len(list_unread_talk)
			index = randint(0,end_of_list-1) #pick an unread message randomly
			if talk_ID=="": #if talk_ID is not passed as parameter
				talk_ID = list_unread_talk[index].get_attribute('class')
				list_reply_before = self.inboxtalk.get_all_replyID_within_a_talkID(talk_ID) #check existing reply ID before sending reply
				total_list_reply_before = len(list_reply_before)
				print('Total reply sebelum send reply: ' + str(total_list_reply_before))
				print(talk_ID)
				print(reply_talk)
				print('List replyID:')
				for i in list_reply_before:
					print(i)
			else: #if talk_ID is passed as parameter in test_reply_talk, then use that specific talk_ID instead of random talk_ID
				print('List replyID:')
				for i in list_reply_before:
					print(i)
				pass
			self.inboxtalk.write_and_send_reply(talk_ID, reply_talk)
			time.sleep(3)
			list_reply_after = self.inboxtalk.get_all_replyID_within_a_talkID(talk_ID) #check existing reply ID after sending reply
			total_list_reply_after = len(list_reply_after)
			print('Total reply setelah send reply: ' + str(total_list_reply_after))
			diff = total_list_reply_after - total_list_reply_before
			reply_ID = list_reply_after[total_list_reply_before:total_list_reply_after] #get new reply ID
			print('New reply ID: ')
			print(reply_ID)
			if diff > 0:
				print('Reply message is shown')
			elif diff == 0:
				print('Reply message is not shown')
			else:
				print('error')
			return(talk_ID, reply_ID)
		except NoSuchElementException:
			talk_ID=[]
			reply_ID=[]
			print('Tidak ada unread talk')
			return(talk_ID, reply_ID)

	def is_reply_received(self, site, talk_ID, ID_new_reply):
		print('Talk ID : ' + talk_ID)
		print(ID_new_reply)
		isTalkReplyReceived = 0
		self.inboxtalk.open(site)
		self.inboxtalk.select_filter_unread()
		time.sleep(4)
		all_reply_ID = self.inboxtalk.get_all_replyID_within_a_talkID(talk_ID)
		unread_flag = self.inboxtalk.get_unread_flag(talk_ID)
		print('unread flag : ' + str(unread_flag))
		for i in ID_new_reply:
			print(i)
			for j in all_reply_ID:
				print(j)
				print('Checking if reply is shown')
				if i == j:
					isTalkReplyReceived = 1
					break
				else:
					pass
		if isTalkReplyReceived == 1:
			if unread_flag==1:
				print('Talk Reply is received and flagged as new message')
			else:
				print('Talk Reply is received but not flagged as new message')
		else:
			isTalkReplyReceived == 0
			print('Talk Reply is not received')

	def delete_random_talk(self, site):
		list_talk_ID = []
		self.inboxtalk.open(site)
		self.inboxtalk.select_tab_all()
		self.inboxtalk.select_filter_unread()
		time.sleep(3)
		list_talk = self.inboxtalk.get_list_message()
		for each in list_talk:
			list_talk_ID.append(each.get_attribute('class'))
			#print(each.get_attribute('class'))
		total_list_talk = len(list_talk)
		if total_list_talk > 0:
			talk_ID = str(list_talk_ID[randint(0,total_list_talk-1)]) #get random talk
			print('Talk ID: ' + talk_ID)
			product_link = self.inboxtalk.get_product_link_of_talk_to_be_deleted(talk_ID)
			self.inboxtalk.delete_talk(talk_ID)
		elif total_list_talk == 0:
			talk_ID='none'
			product_link='none'
			print('There is no unread talk in Inbox Talk')
		return(talk_ID, product_link, total_list_talk)
			
	def is_talk_deleted_from_sender_inbox(self, talk_ID, total_list_talk):
		list_talk_ID = []
		list_talk = self.inboxtalk.get_list_message()
		for each in list_talk:
			list_talk_ID.append(each.get_attribute('class'))
		if total_list_talk > 0:
			if talk_ID in list_talk_ID:
				raise('ERROR: Deleted talk ID [' + talk_ID + '] still exists after deletion')
			else:
				print('Talk ID [' + talk_ID + '] is successfully deleted from sender\'s inbox')
		elif total_list_talk==0:
			print('There is no message in this Page')
