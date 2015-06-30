from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.page.inbox_talk.pe_inbox_talk import *
from random import randint

import time

class inboxTalkActivity():

    def setObject(self, driver):
        self.inboxtalk = InboxTalkPage(driver)

    def reply_message(self, site, talk_ID=""): #talk_ID parameter is optional
        rand = randint(1,9999)
        reply_talk = 'Test balas talk #' + str(rand)
        self.inboxtalk.open(site)
        self.inboxtalk.select_filter_unread()
        list_message = []
        try:
            list_unread_talk = self.inboxtalk.get_list_message() #get list of unread talk in first page
            end_of_list = len(list_unread_talk)
            index = randint(0,end_of_list-1) #pick an unread message randomly
            if talk_ID=="": #if talk_ID is not passed as parameter
                talk_ID = list_unread_talk[index].get_attribute('class')
                print(talk_ID)
                print(reply_talk)
            else: #if talk_ID is passed as parameter in test_reply_talk, then use that specific talk_ID instead of random talk_ID
                pass
            self.inboxtalk.write_and_send_reply(talk_ID, reply_talk)
            reply_ID = [] #can be multiple reply ID
            return(talk_ID, reply_ID)
        except NoSuchElementException:
            return(talk_ID, reply_ID)

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
        unread_flag = self.inboxtalk.get_unread_flag(ID_new_message)
        jml_new_message = len(list_of_unread_msg)
        print(ID_new_message)
        for i in (ID_new_message):
            strcompare = i
            for item in list_of_unread_msg: #search ID_new_message in list
                #print(item)
                if item == strcompare:
                    isMessageReceived = 1
                    break
                else:
                    continue
        if (isMessageReceived == 1):
            if unread_flag == 1:
                print('New talk message is successfully received and flagged as unread message')
            else:
                print('New talk message is successfully received but not flagged as unread message')
        else:
             print('New talk message is not received in receiver inbox')

    def is_reply_received(self):
        pass