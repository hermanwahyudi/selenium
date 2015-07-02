__author__ = 'QC1'

import unittest
from main.activity.android.andr_activity_login import *
from main.activity.android.andr_activity_logout import *
from main.activity.android.andr_activity_shop import *
from time import sleep
from utils.function.setup import *
from utils.lib.user_data import *

class TestTokopediaAndroidAddProduct(unittest.TestCase):

    def setUp(self):
        self.driver = tsetup_andr()

    def test_1_add_product(self):
        print("Tokopedia Android Add Product #1 : Adding new product to shop")
        sleep(2)

        login_activity = ActivityLogin()
        logout_activity = ActivityLogout()
        shop_activity = ActivityShop()

        login_activity.do_login(self.driver,AndroidSeller["email"], AndroidSeller["password"])
        login_activity.seller_login_validation(self.driver)
        self.driver.keyevent(4)
        sleep(1)
        shop_activity.add_product(self.driver)
        self.driver.keyevent(4)
        logout_activity.do_logout(self.driver)


    def tearDown(self):
        print("Testing done. The test environment will be closed in a few moment. . . .")
        sleep(5)
        self.driver.quit()

#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTokopediaAndroidAddProduct)
    unittest.TextTestRunner(verbosity=2).run(suite)