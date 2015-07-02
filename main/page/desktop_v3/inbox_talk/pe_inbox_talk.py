from main.page.base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InboxTalkPage(BasePage):
	_pl = "inbox-talk.pl"
	#url = "https://www.tokopedia.com/inbox-talk.pl"

	#Locators
	#_filter_all_loc = (By.CSS_SELECTOR, 'div#talk-box div.row-fluid div.span12 span.pull-left small a.filter-all')
	_filter_all_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div/span/small/a[1]')
	_filter_unread_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div/span/small/a[2]')
	_next_page_loc = (By.CSS_SELECTOR, 'div.row-fluid div.text-right div.pagination ul li a i.icon-chevron-right')

	#Tab Locators
	_tab_all_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[1]/a')
	_tab_my_product_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[2]/a')
	_tab_following_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[3]/a')
	_total_message_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[2]/a/span/span') #angka di counter di tab my product

	#Talk Content
	_talk_box = (By.XPATH, '//*[@id="talk-list-container"]')
	_list_of_message_loc = (By.XPATH, '//*[@id="talk-box"]/div[2]/div/ul')
	#_unread_flag_loc_1 = '//*[@id=\"talk-list-container" and @class=\"'
	#_unread_flag_loc_2 = '\"]/div/div[2]/div[1]/a'
	_unread_flag_loc = ' div.list-box-content div.list-box-detail div.first-talk span.unread-box'
	_see_all_comment_link_loc = (By.CSS_SELECTOR, 'div.list-box-detail a.list-box-viewalltalk small span') #only appeared if there are more than 3 replies
	

	_talkID_loc = 'div.span12 ul li.'
	_reply_textarea_loc = ' div.list-box-replyholder div.row-fluid.talk-comment-input div div div div textarea:nth-child(2)'
	#_reply_button_loc = (By.CSS_SELECTOR, 'div.list-box-textarea div.pull-left button#submit-talk-comment') #only visible if textarea is filled
	#_reply_button_loc = (' div.list-box-content div.list-box-detail div.list-box-replyholder div.row-fluid.talk-comment-input div.list-box-replyholder.talk-response-input div.list-box-replycomment div.list-box-textarea div.pull-left button#submit-talk-comment')
	_reply_button_loc = (' div.list-box-replyholder div.row-fluid.talk-comment-input div div div div button#submit-talk-comment')
	_reply_list_loc = ' div.list-box-replyholder div#talk-comment-container div.talk-comment-list'
	_sender_loc = ' div.list-box-content div.list-box-detail div.first-talk div.list-box-replybuyer div.list-box-sellerreplyinfo a small b'
	_replier_name_loc_1 = ' div.list-box-content div.list-box-detail div.list-box-replyholder div#talk-comment-container div#'
	_replier_name_loc_2 = ' div.list-box-replycomment div.list-box-replybuyer div.list-box-sellerreplyinfo span.pull-left b small a'
	_delete_button_loc = ' div.list-box-content div.list-box-detail div.first-talk a span#delete-talk-button'
	_single_talk_body_loc = ' div div.list-box-detail div.first-talk div.list-box-replybuyer div.list-box-sellerreplyinfo'
	_delete_button_at_popup_loc = (By.CSS_SELECTOR, 'div.container-fluid div.row-fluid div form div.dialog-footer button#del-talk-button')
	_product_name_loc = ' div.list-box-content div.list-box-product div.list-box-top a b'
	_product_link_loc = ' div.list-box-content div.list-box-product div.list-box-top a'


	#Actions
	def open(self, site, _pl=""):
		self._open(site, self._pl)

	def next_page_element(self):
		try:
			self.find_element(*self._next_page_loc)
			#print ('Next page available')
			return (1)
		except NoSuchElementException:
			print ("Next page not found")
			return (0)


	def click_next_page(self):
		#print(str(self.find_element(*self._next_page_loc)) + " next page found")
		NextPage = self.next_page_element()
		if NextPage == 1:
			self.find_element(*self._next_page_loc).click()
			print('Goto Next Page')
		elif NextPage == 0:
			print("end of page")
			

	def select_tab_all(self):
		tab_all = self.find_element(*self._tab_all_loc)    #Tampung lokasi elemen ke dalam variabel
		self._click(tab_all)                                  #Gunakan fungsi Click kepunyaan Framework variable

	def select_tab_my_product(self):
		tab_my_product = self.find_element(*self._tab_my_product_loc)
		self._click(tab_my_product)

	def select_filter_unread(self):
		self.check_visible_element(*self._filter_unread_loc)
		filter_unread_loc = self.find_element(*self._filter_unread_loc)
		try:
			WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self._filter_unread_loc))
			print ("JS clickable ni")
			self.click_on_javascript(filter_unread_loc)
		except NoSuchElementException:
			print ("JS not found")
		self._click(filter_unread_loc)


	def select_filter_all(self):
		self.check_visible_element(*self._filter_all_loc)
		filter_all_loc = self.find_element(*self._filter_all_loc)
		try:
			WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self._filter_all_loc))
			print ("JS clickable ni")
			self.click_on_javascript(filter_all_loc)
		except NoSuchElementException:
			print ("JS not found")
		#self._click(filter_unread_loc)


	def check_talk_discussion_exists(self):
		self.check_visible_element(*self._talk_box)
		talk_found = self.find_element(*self._talk_box)
		try:
			if talk_found.is_displayed():
				print("Talk Found")
		except NoSuchElementException:
			print ("No Talk Found")

	def get_message_counter_value(self):
		try:
			jumlah_message = self.find_element(*self._total_message_loc).text
			jumlah_message = int(jumlah_message)
			return (jumlah_message)
		except NoSuchElementException:
			print('There is no message here')
			return(0)

	def get_list_message(self):
		try:
			list_message = self.find_elements(*self._talk_box)
			return(list_message)
		except NoSuchElementException:
			print('Tidak ada pesan')
			list_message = []
			return(list_message)

	def list_all_message_ID(self):
		list_msg = self.get_list_message()
		list_msg_ID = []
		print('Counting message ....')
		for i in list_msg:
			#print(i.get_attribute('class'))
			list_msg_ID.append(i.get_attribute('class'))
		isNextPageAvailable = self.next_page_element()
		while isNextPageAvailable == 1:
			self.click_next_page()
			time.sleep(5)
			next_list_messages = self.get_list_message()
			for i in next_list_messages:
				#print(i.get_attribute('class'))
				list_msg_ID.append(i.get_attribute('class'))
			list_msg.extend(next_list_messages)
			isNextPageAvailable = self.next_page_element()
		print('end of inbox page')
		print('List ID message dalam inbox:')
		jml_msg = len(list_msg)
		for i in list_msg_ID:
			print(i)
		print('List of message has been successfully populated...')
		return(list_msg_ID)

	def all_message_counts(self):
		self.select_filter_all()
		all_msg = len(self.list_all_message_ID())
		return(all_msg)

	#UNREAD TALKS#
	def get_unread_flag(self, new_message_id):
		#unread_sign = self._unread_flag_loc_1 + str(new_message_id) + self._unread_flag_loc_2
		unread_sign = self._talkID_loc + str(new_message_id) + self._unread_flag_loc
		try:
			#unread_sign = self._talkID_loc + str(new_message_id) + self._unread_flag_loc
			self.check_visible_element(By.CSS_SELECTOR, unread_sign)
			print(unread_sign)
			#self.find_element(By.CSS_SELECTOR, unread_sign)
			return(1)
		except:
			print(unread_sign)
			print('Unread flag not displayed')
			return(0)

	def list_all_unread_message_ID(self):
		self.select_tab_my_product()
		self.select_filter_unread()
		print('Masuk Tab Unread')
		unread_msg = self.get_list_message()
		unread_msg_ID = []
		for i in unread_msg:
			unread_msg_ID.append(i.get_attribute('class'))
		isNextPageAvailable = self.next_page_element()
		while isNextPageAvailable == 1:
			self.click_next_page()
			time.sleep(5)
			next_list_messages = self.get_list_message()
			for i in next_list_messages:
				unread_msg_ID.append(i.get_attribute('class'))
			unread_msg.extend(next_list_messages)
			isNextPageAvailable = self.next_page_element()
		print('end of inbox page')
		print('List unread ID message dalam inbox:')
		for i in unread_msg_ID:
			print(i)
		print('List of message has been successfully populated...')
		return(unread_msg_ID)

	#actual number of all messages
	def unread_message_counts(self):
		self.select_filter_unread()
		all_unread_msg = len(self.list_all_unread_message_ID())
		return(all_unread_msg)



	#REPLY#
	def write_and_send_reply(self, talk_ID, reply_talk):
		textarea = self._talkID_loc + talk_ID + self._reply_textarea_loc
		reply_btn = self._talkID_loc + talk_ID + self._reply_button_loc
		_reply_btn = (By.CSS_SELECTOR, reply_btn)
		try:
			self.find_element(By.CSS_SELECTOR, textarea).click()
			time.sleep(1)
			self.find_element(By.CSS_SELECTOR, textarea).send_keys(reply_talk)
			print('berhasil tulis reply')
			time.sleep(2)
			#WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(_reply_btn))
			#self.check_visible_element(_reply_btn)
			#print('replybtn found')
			self.find_element(By.CSS_SELECTOR, reply_btn).click() #should be visible after send_keys is performed
			#self.find_element(By.CSS_SELECTOR, reply_btn).click()
			#self.click_on_javascript(self.find_element(_reply_btn))
			print('reply sent')
		except Exception as inst:
			print(inst)

	def get_all_replyID_within_a_talkID(self, talk_ID):
		replyID_list = []
		reply = self._talkID_loc + talk_ID + self._reply_list_loc
		try:
			reply_list = self.find_elements(By.CSS_SELECTOR, reply)
			print(reply_list)
			for i in reply_list:
				replyID_list.append(i.get_attribute('id'))
				print(i.get_attribute('id'))
			return(replyID_list)
		except NoSuchElementException:
			print('There is no reply within this talk_ID')
			return(replyID_list)

	def get_main_talk_sender(self, talk_ID): #get the username of talk creator
		sender = self._talkID_loc + talk_ID + self._sender_loc
		sender_name = self.find_element(By.CSS_SELECTOR, sender)
		return(sender_name)

	def get_last_reply_sender_name(self, talk_ID, reply_ID): #get the username of reply senders
		name_location = self._talkID_loc + talk_ID + self._replier_name_loc_1 + reply_ID + self._replier_name_loc_2
		reply_sender_name = self.find_element(By.CSS_SELECTOR, name_location)
		return(reply_sender_name)

	#DELETE TALK

	def delete_talk(self, talk_ID):
		selected_talk = self._talkID_loc + talk_ID + self._single_talk_body_loc
		delete_button = self._talkID_loc + talk_ID + self._delete_button_loc

		self.mouse_hover_to(By.CSS_SELECTOR, selected_talk)
		print('Hovering to talk')
		#self.mouse_hover_to(By.CSS_SELECTOR, delete_button)
		time.sleep(2)
		self.find_element(By.CSS_SELECTOR, delete_button)
		self.mouse_hover_to(By.CSS_SELECTOR, delete_button).click()
		self.find_element(*self._delete_button_at_popup_loc).click()
		print('Delete button clicked')

	def delete_at_popup(self):
		try:
			self.find_element(*self._delete_button_at_popup_loc).click()
		except:
			raise('Pop up delete button does not exist')

	def get_product_name_of_talk_to_be_deleted(self, talk_ID):
		product = self._talkID_loc + talk_ID + self._product_name_loc
		product_name = self.find_element(By.CSS_SELECTOR, product).text
		return(product_name)

	def get_product_link_of_talk_to_be_deleted(self, talk_ID):
		link = self._talkID_loc + talk_ID + self._product_link_loc
		product_link = self.find_element(By.CSS_SELECTOR, link).get_attribute('href')
		return(product_link)

	

