from main.activity.activity_login import *
from main.activity.activity_logout import *
from main.activity.activity_myshop_order import *
from main.activity.activity_myshop_order import *
from main.activity.activity_inbox_review import *
from main.lib.user_data import *
from main.function.setup import *
from main.activity.activity_tx_payment_confirmation import *
import unittest

class TestCheckInboxReview(unittest.TestCase):

    _site = "live"

    def setUp(self):
        self.driver = tsetup()


    def test_1_check_counter(self):
        print ("TEST #1 : Check Counter at Inbox Review")
        print ("========================================")
        driver = self.driver
        total_test_user = 0

        for each_user in user:

            email = user[total_test_user]['email']
            pwd = user[total_test_user]['pwd']

            login = loginActivity()
            inbox_review = inboxReviewActivity()
            inbox_review.setObject(driver)
            logout = logoutActivity()

            login.do_login(driver, email, pwd, self._site)
            inbox_review.goto_inbox_review(self._site)
            inbox_review.check_counter_review()
            logout.do_logout(driver, self._site)
            total_test_user +=1

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')