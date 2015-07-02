__author__ = 'QC1-Yonathan'
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_logout import *
from main.activity.desktop_v3.activity_header import *
from main.activity.desktop_v3.activity_inbox_price_alert import *
from main.activity.desktop_v3.activity_product import *
from main.activity.desktop_v3.activity_index import *
from utils.lib.user_data import *
from utils.function.setup import *
import unittest, string, random, time

class TestPriceAlert(unittest.TestCase):
    _site = "live"

    def setUp(self):
        self.driver=tsetup("firefox")
        self.flag = 0

    def test_1_notification_price_input_confirmation(self):
        print("TEST #1: Input Price Notification and check its appearance at inbox - price alert")
        print("=================================================================================")

        driver = self.driver

        # change this in accordance with buyer and seller email and pwd
        email = user6['email']
        pwd = user6['pwd']

        loginValidate = loginActivity()
        checkIndex = indexActivity()
        checkHeader = headerActivity()
        inputPriceAlert = PriceAlertActivity()
        logoutValidate = logoutActivity()

        h_flag = loginValidate.do_login(driver, email, pwd, self._site)
        checkIndex.index_no_shop(driver)
        checkHeader.check_header_status(driver,h_flag)
        inputPriceAlert.update_price_alert(driver, self._site, "qc44")
        inputPriceAlert.check_inbox_price_alert(driver)
        logoutValidate.do_logout(driver, self._site)

    def test_2_target_notification_price_found(self):
        print("TEST #2: Seller update a product price and check its appearance at inbox - price alert for buyers")
        print("=================================================================================================")

        driver = self.driver

        # make this the same as the test case 1 user and pwd
        email = user5['email']
        pwd = user5['pwd']

        loginValidate = loginActivity()
        checkIndex = indexActivity()
        checkHeader = headerActivity()
        productPrice = ProductActivity()
        logoutValidate = logoutActivity()
        priceAlert = PriceAlertActivity()

        h_flag = loginValidate.do_login(driver, email, pwd, self._site)
        checkIndex.now_at_index(driver)
        checkHeader.check_header_status(driver,h_flag)
        productPrice.edit_product_price(driver, self._site, "qc44")
        logoutValidate.do_logout(driver, self._site)

        # change this in accordance with buyer and seller email and pwd
        email_buyer = user6['email']
        pwd_buyer = user6['pwd']

        h_flag = loginValidate.do_login(driver, email_buyer, pwd_buyer, self._site)
        checkIndex.index_no_shop(driver)
        checkHeader.check_header_status(driver,h_flag)
        priceAlert.search_price_alert(driver)
        logoutValidate.do_logout(driver, self._site)

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        self.driver.quit()
        #print ("waktu test : %.3f" %(t))

if __name__ == '__main__':
    unittest.main(warnings='ignore')