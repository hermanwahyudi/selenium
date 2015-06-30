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
    _unread_flag_loc_1 = '//*[@id=\"talk-list-container" and @class=\"'
    _unread_flag_loc_2 = '\"]/div/div[2]/div[1]/a'
    _see_all_comment_link_loc = (By.CSS_SELECTOR, 'div.list-box-detail a.list-box-viewalltalk small span') #only appeared if there are more than 3 replies

    _talkID_loc = 'div.span12 ul li.'
    _reply_textarea_loc = ' div.list-box-replyholder div.row-fluid.talk-comment-input div div div div textarea:nth-child(2)'
    _reply_button_loc = (By.CSS_SELECTOR, 'div.list-box-textarea button#submit-talk-comment') #only visible if textarea is filled
    _reply_list_loc = 'div.list-box-replyholder div#talk-comment-container div'


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
        try:
            self.check_visible_element(By.XPATH, (self._unread_flag_loc_1 + str(new_message_id) + self._unread_flag_loc_2))
            return(1)
        except NoSuchElementException:
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
        try:
            self.find_element(By.CSS_SELECTOR, textarea).click()
            time.sleep(1)
            self.find_element(By.CSS_SELECTOR, textarea).send_keys(reply_talk)
            print('berhasil tulis reply')
            time.sleep(1)
            self.find_element(*self._reply_button_loc).click() #should be visible after send_keys is performed
            print('reply sent')
        except:
            print('reply button not found')


    def get_all_replyID_within_a_talkID(self, talk_ID):
        replyID_list = []
        try:
            replyID_list = self.find_elements(*loc) #<---- last modified
            return(replyID_list)
        except NoSuchElementException:
            print('There is no reply within this talk_ID')
            return(replyID_list)

