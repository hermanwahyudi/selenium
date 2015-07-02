__author__ = 'QC1'

import unittest
from main.activity.android.andr_activity_login import *
from main.activity.android.andr_activity_logout import *
from main.activity.android.andr_activity_transaction import *
from time import sleep
from utils.function.setup import *
from utils.lib.user_data import *
from appium import webdriver

class TestTokopediaAndroidTransaction(unittest.TestCase):

    def setUp(self):
        self.driver = tsetup_andr()


    def test_1_buyer_purchase_product(self):

        print("Tokopedia Transaction Test #1 : Testing for purchase product")
        sleep(2)

        login_activity = ActivityLogin()
        transaction_activity = ActivityTransaction()
        logout_activity = ActivityLogout()

        login_activity.do_login(self.driver,AndroidBuyer["email"], AndroidBuyer["password"])
        login_activity.buyer_login_validation(self.driver)
        self.driver.keyevent(4)
        sleep(2)
        transaction_activity.do_buyer_purchase(self.driver, AndroidBuyer["password"])
        print("purchase test succeeded.")
        logout_activity.do_logout(self.driver)

    def test_2_seller_shipment_process(self):
        print("Tokopedia Transaction Test #2 : Testing for seller order shipment process.")
        sleep(2)

        login_activity = ActivityLogin()
        transaction_activity = ActivityTransaction()
        logout_activity = ActivityLogout()

        login_activity.do_login(self.driver, AndroidSeller["email"], AndroidSeller["password"])
        login_activity.seller_login_validation(self.driver)
        self.driver.keyevent(4)
        sleep(2)
        order_success_text = transaction_activity.do_seller_order_process(self.driver)
        #assert the status of the test
        self.assertEqual(order_success_text, "Order telah diproses")
        print("Seller successfully processed the order. Test suceeded.")
        self.driver.keyevent(4)
        sleep(2)
        logout_activity.do_logout(self.driver)



    def test_3_buyer_confirmation(self):
        print("Tokopedia Transaction Test #3 : Testing buyer confirming product has been received")
        sleep(2)

        login_activity = ActivityLogin()
        transaction_activity = ActivityTransaction()
        logout_activity = ActivityLogout()

        login_activity.do_login(self.driver, AndroidBuyer["email"], AndroidBuyer["password"])
        login_activity.buyer_login_validation(self.driver)
        self.driver.keyevent(4)
        sleep(2)
        transaction_activity.do_buyer_receive_confirm(self.driver)
        print("Buyer confirmation test successful.")
        logout_activity.do_logout(self.driver)

    def tearDown(self):
        print("Testing done. The test environment will be closed in a few moment. . . .")
        sleep(5)
        self.driver.quit()

#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTokopediaAndroidTransaction)
    unittest.TextTestRunner(verbosity=2).run(suite)