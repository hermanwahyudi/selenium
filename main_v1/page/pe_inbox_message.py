import os,sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InboxMessagePage(BasePage):
    url = "https://www.tokopedia.com/inbox-message.pl"

    #Locators
    _filter_all_loc = (By.CSS_SELECTOR, 'div#message-box div.row-fluid div.span12 span.pull-left small a#filter-all')
    _filter_unread_loc = (By.CSS_SELECTOR, 'div#message-box div.row-fluid div.span12 span.pull-left small a#filter-unread')
    _archive_button_upper_loc = (By.XPATH, '//*[@id="message"]/div/div[1]/a[1]')
    _delete_button_upper_loc = (By.XPATH, '//*[@id="message"]/div/div[1]/a[2]')
    _archive_button_lower_loc = (By.XPATH, '//*[@id="message"]/div/div[2]/a[1]')
    _delete_button_lower_loc = (By.XPATH, '//*[@id="message"]/div/div[2]/a[2]')
    _next_page_button_loc = (By.XPATH, '//*[@id="message-box"]/div[3]/div[2]/div/ul/li/a')

    #Tab Locators
    _tab_inbox_loc = (By.CSS_SELECTOR, 'div.maincontent-admin ul.horizontal-tab li.active a#tab-nav-inbox')
    _tab_sent_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[2]/a')
    _tab_archive_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[3]/a')
    _tab_trash_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[4]/a')

    #Message Content
    _msg_box = (By.XPATH, "//tr[starts-with(@id, 'msg-id-')]")

    #Actions
    def open(self):
        self._open(self.url)

    def select_tab_inbox(self):
        tab_inbox_loc = self.find_element(*self._tab_inbox_loc)
        self._click(tab_inbox_loc)

    def select_tab_sent(self):
        tab_sent_loc = self.find_element(*self._tab_sent_loc)
        self._click(tab_sent_loc)

    def select_tab_archive(self):
        tab_archive_loc = self.find_element(*self._tab_archive_loc)
        self._click(tab_archive_loc)

    def select_tab_trash(self):
        tab_trash_loc = self.find_element(*self._tab_trash_loc)
        self._click(tab_trash_loc)

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


def goto_inbox_message(driver):
    inbox_message_page = InboxMessagePage(driver)

    inbox_message_page.open()
    inbox_message_page.check_message_exists()
    inbox_message_page.select_filter_unread()
    time.sleep(10)
    inbox_message_page.select_tab_inbox()
    inbox_message_page.select_tab_archive()
    inbox_message_page.select_tab_sent()
    inbox_message_page.select_tab_trash()















