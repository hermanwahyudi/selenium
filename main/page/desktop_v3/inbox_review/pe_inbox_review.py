from main.page.base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InboxReviewPage(BasePage):
    _pl = "inbox-review.pl"

    #Locators
    _filter_all_loc = (By.CSS_SELECTOR, 'div.review-box div.row-fluid div.span12 span.pull-left small a.filter-all')
    _filter_unread_loc = (By.CSS_SELECTOR, 'div.review-box div.row-fluid div.span12 span.pull-left small a.filter-unread')
    _next_page_loc = (By.CSS_SELECTOR, 'div.row-fluid div.text-right div.pagination ul li a i.icon-chevron-right')
    _prev_page_loc = (By.CSS_SELECTOR, 'div.row-fluid div.text-right div.pagination ul li a i.icon-chevron-left')

    #Tab Locators
    _tab_all_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[1]/a')
    _counter_tab_all_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/ul/li[1]/a/span/span')
    _tab_my_product_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[2]/a')
    _counter_tab_my_product_loc = (By.XPATH, 'fill_in_here')
    _tab_my_review_loc = (By.XPATH, '//*[@id="tab-navigation"]/li[3]/a')
    _counter_tab_my_review_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/ul/li[3]/a/span/span')

    _list_review = {
        'review_box_loc' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div'),
        'product_name_loc' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[1]/div[2]/a/b'),
        'shop_name_loc' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[1]/div[2]/small/a'),
        'text_area_loc' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[2]/div/div/textarea[2]'),
        'btn_submit_loc' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[2]/div/div/button[1]'),
        'btn_skip_loc' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[2]/div/div/button[2]'),
        'unread_notification_loc' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[2]/div/div/span'),
        'quality_rating_1' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[3]/span[1]/div/img[1]'),
        'quality_rating_2' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[3]/span[1]/div/img[2]'),
        'accuracy_rating_1' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[3]/span[2]/div/img[1]'),
        'accuracy_rating_2' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[3]/span[2]/div/img[2]'),
        'speed_rating_1' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[3]/span[3]/div/img[1]'),
        'speed_rating_2' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[3]/span[3]/div/img[2]'),
        'service_rating_1' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[3]/span[4]/div/img[1]'),
        'service_rating_2' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li/div/div[2]/div/div/div[3]/span[4]/div/img[2]'),
        'test_p1' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li[1]/div/div[1]/div[2]/a/b'),
        'test_s1' : (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li[1]/div/div[1]/div[2]/small/a')

    }

    _confirm_skip_loc = (By.CSS_SELECTOR,'div.dialog-content div.container-fluid div#rf div form div.dialog-footer button.btn-action')
    _cancel_skip_loc = (By.CSS_SELECTOR,'div.dialog-content div.container-fluid div#rf div form div.dialog-footer button.btn')
    _close_skip_dialog_loc = (By.CSS_SELECTOR, 'div.dialog-header a.dialog-close i.icon-remove')

    #Actions
    def open(self, site=""):
        self._open(site, self._pl)

    def next_page_element(self):
        try:
            self.find_element(*self._next_page_loc)
            return 1
        except NoSuchElementException:
            print ("Next Page not found")
            return 0

    def check_paging_exists(self):
        try:
            if self.find_element(*self._next_page_loc) == True:
                print ("Next Page Button Found!")
            elif self.find_element(*self._prev_page_loc) == True:
                print ("Previous Page Button Found!")

        except:
            print ("Next / Previous Page button not found")
            return

    def click_next_page(self):
        # try:
        #     print(str(self.find_element(*self._next_page_loc)) + " next page found!")
        #     next_page_loc = self.find_element(*self._next_page_loc)
        #     self._click(next_page_loc)
        # except NoSuchElementException:
        #     print ("Next page not found!")
        NextPage = self.next_page_element()
        if NextPage == 1:
            self.find_element(*self._next_page_loc).click()
            print ("Go to Next Page")
        elif NextPage == 0:
            print ("End of Page")
        else:
            print ("error at finding page")


    def click_previous_page(self):

        try:
            print (str(self.find_element(*self._prev_page_loc)) + " previous page found!")
            prev_page_loc = self.find_element(*self._prev_page_loc)
            self._click(prev_page_loc)
        except NoSuchElementException:
            print ("Previous page not found!")

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

    def select_filter_all(self):
        self.check_visible_element(*self._filter_all_loc)
        filter_all_loc = self.find_element(*self._filter_all_loc)
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self._filter_all_loc))
            self.click_on_javascript(filter_all_loc)
            print ("Moved to Filter : All")
        except NoSuchElementException:
            print ("JS not Found")
        time.sleep(4)


    def select_filter_unread(self):
        self.check_visible_element(*self._filter_unread_loc)
        filter_unread_loc = self.find_element(*self._filter_unread_loc)
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self._filter_unread_loc))
            self.click_on_javascript(filter_unread_loc)
            print ("Moved to Filter : Unread")
        except NoSuchElementException:
            print ("JS not found")
        #self._click(filter_unread_loc)
        time.sleep(5)

    def check_review_exists(self):
        global total_review
        total_review = 0
        try:

            self.find_element(*self._list_review['review_box'])
            for each_review in self.find_elements(*self._list_review['review_box']):
                total_review +=1
            print ("Total Review di halaman saat ini: %s" %(total_review))

        except:
            print ("There is no review at this page")


    def check_counter_notification(self):
        unread_counter = 0
        total_page = 0

        print("Now Checking Counter Notification at Inbox Review...")
        time.sleep(2)
        try:
            print (self.find_element(*self._counter_tab_all_loc).text)
            current_counter = self.find_element(*self._counter_tab_all_loc).text
            current_counter = int(current_counter)

            self.select_filter_unread()
            # for each_unread_counter in self.find_elements(*self._list_review['unread_notification_loc']):
            #     unread_counter +=1
            # print ("Total Unread Review : %s" %(unread_counter))
            isNextPageAvailable = self.next_page_element()

            if isNextPageAvailable == 0:
                for each_unread_counter in self.find_elements(*self._list_review['unread_notification_loc']):
                    #print ("list unread counter %s: " %(each_unread_counter))
                    unread_counter +=1
                total_page +=1

            elif isNextPageAvailable == 1:
                while isNextPageAvailable == 1:
                    for each_unread_counter in self.find_elements(*self._list_review['unread_notification_loc']):
                        #print ("list unread counter %s: " %(each_unread_counter))
                        unread_counter +=1
                    total_page += 1
                    self.click_next_page()
                    time.sleep(2)

                    isNextPageAvailable = self.next_page_element()
                    if isNextPageAvailable == 0:
                        for each_unread_counter in self.find_elements(*self._list_review['unread_notification_loc']):
                            #print ("list unread counter %s: " %(each_unread_counter))
                            unread_counter +=1



            print ("Total Unread Review : %s" %(unread_counter))
            print ("Total Page : %s"%(total_page))


            if current_counter == unread_counter:
                print ("Current Counter : %s and Total Unread Review : %s (MATCHED)" %(current_counter,unread_counter))
            else:
                print ("Current Counter : %s and Total Unread Review : %s (NOT MATCHED)" %(current_counter,unread_counter))
                print ("Something is wrong with total counter!")
        except:
            print ("There is no Unread Review!")

    def get_product_element(self):

        self.check_visible_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li[3]/div/div[1]/div[2]/a/b')
        a = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li[3]/div/div[1]/div[2]/a/b')
        return a

    def get_shop_element(self):
        self.check_visible_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li[3]/div/div[1]/div[2]/small/a')
        b = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[1]/div[2]/div/ul/li[3]/div/div[1]/div[2]/small/a')
        return b

    def get_selected_review(self, product_name="", shop_name=""):
        list_product_name = []
        list_shop_name = []

        target_filter = 0
        order_index = None
        #each_text_box = None

        #cond 1
        for each_product in self.find_elements(*self._list_review['product_name_loc']):
            list_product_name.append(each_product)

        for each_shop in self.find_elements(*self._list_review['shop_name_loc']):
            list_shop_name.append(each_shop)

        print ("Searching for target order")
        for each_product_listed in range(len(list_product_name)):

            if list_product_name[target_filter].text == product_name and list_shop_name[target_filter].text == shop_name:
                print(list_product_name[target_filter].text + " dan " + list_shop_name[target_filter].text + " pada index " + str(target_filter))
                order_index= target_filter+1
                break
            target_filter +=1

        print ("target review found at order {0}".format(order_index))
        return target_filter

    def input_review_for_last_transaction(self, target_filter):
        list_text_area = []

        # for each_text_box in self.find_elements(*self._list_review['text_area_loc']):
        #     list_text_area.append(each_text_box)

        [(lambda find_text_area: list_text_area.append(each_text_box))(each_text_box) for each_text_box in self.find_elements(*self._list_review['text_area_loc'])]
        list_text_area[target_filter].send_keys("holeelleellele")
        print("sent keys")
        time.sleep(5)

    def skip_review_for_latest_transaction(self, target_filter):
        list_skip_btn = []

        try:
            [(lambda find_skip_btn: list_skip_btn.append(each_skip_btn))(each_skip_btn) for each_skip_btn in self.find_elements(*self._list_review['btn_skip_loc'])]

            print (list_skip_btn[target_filter])
            self._click(list_skip_btn[target_filter])
            print ("success skip")
        except:
            print ("Button Skip for this review product not found! Buyer has never been gave a review before!")
            flag = 2
            return flag
        time.sleep(2)

    def confirm_skip_review(self):
        self.check_visible_element(*self._confirm_skip_loc)
        do_skip = self.find_element(*self._confirm_skip_loc)
        self._click(do_skip)
        return

    def cancel_skip_review(self):
        self.check_visible_element(*self._cancel_skip_loc)
        cancel_skip = self.find_element(*self._cancel_skip_loc)
        self._click(cancel_skip)
        return

    def close_skip_review_dialog(self):
        self.check_visible_element(*self._close_skip_dialog_loc)
        close_dialog = self.find_element(*self._close_skip_dialog_loc)
        self._click(close_dialog)
        return

