#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from utils.function.setup import *
from main.activity.desktop_v3.activity_report_product import *

class TestReportProduct(unittest.TestCase):

    dict = {
        "site" : "live",
        "loop" : 2,
        "domain_shop" : "qc13",
        "backend_link" : "admin/product/report-abuse-product.pl",
        "price" : 4000,
        "category" : "",
        "desc" : "Testing untuk keperluan QC",
        "email_buyer" : "tkpd.qc+44@gmail.com",
        "password_buyer" : "tkpdyo",
        "seller_name" : "herman wahyudi"
    }

    def setUp(self):
        self.driver = tsetup("firefox")
        self.activity = ReportProductActivity(self.driver)
        self.activity.set_parameter(self.dict)
        print("Test Case Report Product: testing the report product function and ensure that the report is available on Tokopedia backend.")
        print("===========================================================================================================================")
        time.sleep(2)

    def test_case_1_report_product(self):
        print("Test #1 : Report a product using the 'report' feature.")
        print("======================================================")
        self.activity.set_report_product(self.dict['category'], self.dict['desc'])

    def test_case_2_report_product_backend(self):
        print("Test #2 : After reporting a product, check the backend to see if the reported product is logged and ready to be processed.")
        print("==========================================================================================================================")
        reasonMessage = self.activity.check_product_report(self.dict['seller_name'], self.dict['desc'])
        print("Comparing the reason message with the description entered....")
        time.sleep(2)
        self.assertEqual(self.dict['desc'], reasonMessage)
        print("The compared text matched! Report product backend test passed.")
        time.sleep(2)


    def tearDown(self):
        print("Report abuse product has been successfully checked! Test Case completed!")
        print("Test environment will be closed in a few moment. . .")
        time.sleep(5)
        self.driver.quit()

# main

if(__name__ == "__main__"):
    unittest.main()

