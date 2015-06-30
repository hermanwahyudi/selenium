from main.page.inbox_review.pe_inbox_review import *
from main.page.header import *

class inboxReviewActivity():

    def setObject(self, driver):
        self.inbox_review_page = InboxReviewPage(driver)

    def goto_inbox_review(self, site):
        self.inbox_review_page.open(site)
        #inbox_review_page.select_tab_all()
        # inbox_review_page.select_tab_my_product()
        # inbox_review_page.click_next_page()
        # inbox_review_page.select_filter_unread()

    def check_all_review(self):
        self.inbox_review_page.check_review_exists()


    def check_paging(self):
        self.inbox_review_page.check_paging_exists()

    def change_filter_all(self):
        self.inbox_review_page.select_filter_all()

    def change_filter_unread(self):
        self.inbox_review_page.select_filter_unread()

    def check_counter_review(self):
        self.inbox_review_page.check_counter_notification()

    def get_my_product(self):
        x = self.inbox_review_page.get_product_element()
        return x

    def get_my_shop(self):
        y = self.inbox_review_page.get_shop_element()
        return y

    def insert_review(self, product_name="", shop_name=""):
        target_review_product = self.inbox_review_page.get_selected_review(product_name, shop_name)
        self.inbox_review_page.input_review_for_last_transaction(target_review_product)

    def skip_review(self, product_name="", shop_name=""):
        target_review_product = self.inbox_review_page.get_selected_review(product_name,shop_name)

        flag_review = self.inbox_review_page.skip_review_for_latest_transaction(target_review_product)

        if flag_review == 1:
            self.inbox_review_page.close_skip_review_dialog()
            time.sleep(2)
            self.inbox_review_page.skip_review_for_latest_transaction(target_review_product)
            self.inbox_review_page.cancel_skip_review()
            time.sleep(2)
            self.inbox_review_page.skip_review_for_latest_transaction(target_review_product)
            self.inbox_review_page.confirm_skip_review()
            time.sleep(2)
        else:
            print ("Cannot Skip review because there is no Skip Review button! Continue...")
