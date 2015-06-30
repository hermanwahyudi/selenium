from main.activity.activity_login import *
from main.activity.activity_myshop_order import *
from main.activity.activity_logout import *
from main.function.setup import *
from main.lib.user_data import *
import unittest


class TestRejectOrder(unittest.TestCase):

    #Instance
    _site = "live"

    def setUp(self):
        self.driver = tsetup()

    def test_1_reject_order(self):
        print ("TEST #1 : Reject Order")
        print ("======================")
        driver = self.driver

        email = user2['email']
        pwd = user2['pwd']

        #Object Activity
        loginValidate = loginActivity()
        myshopOrder = myshopOrderActivity()
        logoutValidate = logoutActivity()


        #Action
        loginValidate.do_login(driver, email, pwd, self._site)
        myshopOrder.goto_myshop_order_process(driver, self._site)
        myshopOrder.reject_order(driver)
        logoutValidate.do_logout(driver, self._site)

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')