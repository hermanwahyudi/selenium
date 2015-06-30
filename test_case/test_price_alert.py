#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from main.function.setup import *
from main.activity.activity_price_alert import *

class TestPriceAlert(unittest.TestCase):

    dict = {
        "site" : "live",
        "loop" : 2,
        "domain_shop" : "qc13",
        "price" : 4000,
        "email_buyer" : "tkpd.qc+15@gmail.com",
        "password_buyer" : "1234asdf"
    }

    def setUp(self):
        self.driver = tsetup()
        self.activity = PriceAlertActivity(self.driver)
        self.activity.set_parameter(self.dict)

    def test_case_input_price_alert(self):
        print("Price Alert")
        self.activity.set_price_alert(self.dict['price'])

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        time.sleep(5)
        self.driver.quit()

# main
if __name__ == '__main__':
    unittest.main(warnings='ignore')

