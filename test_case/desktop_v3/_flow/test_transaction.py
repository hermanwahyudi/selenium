#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from utils.function.setup import *
from main.activity.desktop_v3.activity_transaction import *


class TestTransaction(unittest.TestCase):
    # global parameter
    dict = {
        "site": "live",
        "loop": 5,
        "domain_shop": "tokoqc15",
        "shipping_agency": "JNE",
        "partial_deposit": 1000,
        "destination_bank": "MANDIRI",
        "payment_method": "Transfer ATM",
        "is_confirm_payment": True,
        "is_dropshipper": False,
        "is_until_finish": True,
        "is_add_address": False,
        "dropshipper_name": "PT. Maju Mundur",
        "dropshipper_telp": "09878787855",
        "email_buyer": "tkpd.qc+13@gmail.com",
        "password_buyer": "1234asdf",
        "email_seller": "tkpd.qc+15@gmail.com",
        "password_seller": "1234asdf"  
    }

    # setUp function
    def setUp(self):
        self.driver = tsetup("chrome")
        self.activity = TransactionActivity(self.driver)
        self.activity.set_parameter(self.dict)

    def test_case_deposit(self):
        print("Transaction with Saldo Tokopedia in", self.dict['site'])
        self.activity.transaction_with("Deposit")
    
    def test_case_transfer_bank(self):
        print("Transaction with Bank in", self.dict['site'])
        self.activity.transaction_with("Bank")

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        time.sleep(5)
        self.driver.close()

# main

if (__name__ == "__main__"):
    unittest.main()
