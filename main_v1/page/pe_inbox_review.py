import os,sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InboxReviewPage(BasePage):
    url = "https://www.tokopedia.com/inbox-review.pl"

    #Locators
    _filter_all_loc = (By.CSS_SELECTOR, 'div.review-box div.row-fluid div.span12 span.pull-left small a.filter-all')
    _filter_unread_loc = (By.CSS_SELECTOR, 'div.review-box div.row-fluid div.span12 span.pull-left small a.filter-unread')
    _next_page_loc = (By.CSS_SELECTOR, 'div.row-fluid div.text-right div.pagination ul li a i.icon-chevron-right')

    #Tab Locators
    _tab_all_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[1]/a')
    _tab_my_product_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[2]/a')
    _tab_my_review_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[3]/a')

    #Review Content
    _review_box = (By.XPATH, '//*[@id="review-list-container"]')


    #Actions
    def open(self):
        self._open(self.url)

    def click_next_page(self):

        try:
            print(str(self.find_element(*self._next_page_loc)) + " next page found")
            next_page_loc = self.find_element(*self._next_page_loc)
            self._click(next_page_loc)
        except NoSuchElementException:
            print ("Next page not found")

    def select_tab_all(self):
        self.check_visible_element(*self._tab_all_loc)
        tab_all = self.find_element(*self._tab_all_loc)
        self._click(tab_all)

    def select_tab_my_product(self):
        tab_my_product = self.find_element(*self._tab_my_product_loc)
        self._click(tab_my_product)

    def select_tab_my_review(self):
        tab_my_review = self.find_element(*self._tab_my_review_loc)
        self._click(tab_my_review)

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

    def check_review_exists(self):
        self.check_visible_element()

def goto_inbox_review(driver):
    inbox_review_page = InboxReviewPage(driver)

    inbox_review_page.open()
    inbox_review_page.select_tab_all()
    inbox_review_page.select_tab_my_product()
    inbox_review_page.click_next_page()
    time.sleep(5)
    inbox_review_page.select_filter_unread()
    time.sleep(10)
