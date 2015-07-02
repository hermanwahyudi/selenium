from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_myshop_order import *
from main.activity.desktop_v3.activity_logout import *
from utils.function.setup import *
from utils.lib.user_data import *
import unittest


class TestRejectOrder(unittest.TestCase):

    #Instance
    _site = "live"

    def setUp(self):
        self.driver = tsetup("phantomjs")
        self.user = user2

    def test_1_reject_order(self):
        print ("TEST #1 : Reject Order")
        print ("======================")
        driver = self.driver



        email= self.user['email']
        pwd = self.user['pwd']

        #Object Activity
        loginValidate = loginActivity()
        myshopOrder = myshopOrderActivity()
        logoutValidate = logoutActivity()


        #Action
        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        myshopOrder.goto_myshop_order_process(driver, self._site)
        myshopOrder.reject_order(driver)
        logoutValidate.do_logout(driver, self._site)

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')