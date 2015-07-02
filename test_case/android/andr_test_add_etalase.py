__author__ = 'QC1'

import unittest, string
from main.activity.android.andr_activity_login import *
from main.activity.android.andr_activity_logout import *
from main.activity.android.andr_activity_shop import *
from main.activity.android.andr_activity_transaction import *
from time import sleep
from utils.function.setup import *
from utils.lib.user_data import *


def random_etal_name(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class TestTokopediaAndroidEtalase(unittest.TestCase):

    def setUp(self):
        self.driver = tsetup_andr()

    def test_1_add_etalase(self):
        print("Tokopedia Android Etalase Test #1 : Login as a seller and add several new etalase for the shop")
        sleep(2)

        login_activity = ActivityLogin()
        logout_activity = ActivityLogout()
        shop_activity = ActivityShop()


        login_activity.do_login(self.driver, AndroidSeller["email"], AndroidSeller["password"])
        login_activity.seller_login_validation(self.driver)
        self.driver.keyevent(4)
        sleep(1)
        shop_activity.add_etalase(self.driver)
        self.driver.keyevent(4)
        sleep(1)
        logout_activity.do_logout(self.driver)

    def test_2_delete_etalase(self):
        print("Tokopedia Android Etalase Test #2 : Login as a seller and delete several etalase from the shop")
        sleep(2)

        login_activity = ActivityLogin()
        logout_activity = ActivityLogout()
        shop_activity = ActivityShop()

        login_activity.do_login(self.driver, AndroidSeller["email"], AndroidSeller["password"])
        login_activity.seller_login_validation(self.driver)
        self.driver.keyevent(4)
        sleep(1)
        shop_activity.delete_etalase(self.driver)
        self.driver.keyevent(4)
        sleep(1)
        logout_activity.do_logout(self.driver)


    def tearDown(self):
        print("Testing done. The test environment will be closed in a few moment. . . .")
        sleep(5)
        self.driver.quit()

#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTokopediaAndroidEtalase)
    unittest.TextTestRunner(verbosity=2).run(suite)




