import os,sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InboxTalkPage(BasePage):
    url = "https://www.tokopedia.com/inbox-talk.pl"

    #Locators
    _filter_all_loc = (By.CSS_SELECTOR, 'div#talk-box div.row-fluid div.span12 span.pull-left small a.filter-all')
    _filter_unread_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div/span/small/a[2]')
    _next_page_loc = (By.CSS_SELECTOR, 'div.row-fluid div.text-right div.pagination ul li a i.icon-chevron-right')

    #Tab Locators
    _tab_all_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[1]/a')
    _tab_my_product_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[2]/a')
    _tab_following_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[3]/a')

    #Talk Content
    _talk_box = (By.XPATH, '//*[@id="talk-list-container"]')


    #Actions
    def open(self):
        self._open(self.url)

    def click_next_page(self):
        print(str(self.find_element(*self._next_page_loc)) + " next page found")

        try:
            next_page_loc = self.find_element(*self._next_page_loc)
            self._click(next_page_loc)
        except NoSuchElementException:
            print ("Next page not found")


    def select_tab_all(self):
        tab_my_product = self.find_element(*self._tab_my_product_loc)    #Tampung lokasi elemen ke dalam variabel
        self._click(tab_my_product)                                      #Gunakan fungsi Click kepunyaan Framework variable

    def select_filter_unread(self):
        self.check_visible_element(*self._filter_unread_loc)
        filter_unread_loc = self.find_element(*self._filter_unread_loc)
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self._filter_unread_loc))
            print ("JS clickable ni")
            self.click_on_javascript(filter_unread_loc)
        except NoSuchElementException:
            print ("JS not found")
        #self._click(filter_unread_loc)
        time.sleep(5)

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
        time.sleep(5)

    def check_talk_discussion_exists(self):
        self.check_visible_element(*self._talk_box)
        talk_found = self.find_element(*self._talk_box)
        try:
            if talk_found.is_displayed():
                print("Talk Found")
        except NoSuchElementException:
            print ("No Talk Found")




def goto_inbox_talk(driver):
    inbox_talk_page = InboxTalkPage(driver)

    inbox_talk_page.open()
    #inbox_talk_page.select_filter_all()   #<--masih ngaco nih,perlu di fix (28 Nov 2014)
    inbox_talk_page.select_tab_all()
    inbox_talk_page.check_talk_discussion_exists()

    time.sleep(5)

    #inbox_talk_page.click_next_page()



