#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from main.page.desktop_v3.login.pe_login import *
from main.page.desktop_v3.login.pe_logout import *
from main.page.desktop_v3.shop.pe_shop import *
from main.page.desktop_v3.product.pe_product import *
from main.page.desktop_v3.tx.pe_tx import *
from main.page.desktop_v3.sales.pe_myshop_order_status import *
from main.page.desktop_v3.sales.pe_myshop_order import *
from main.page.desktop_v3.sales.pe_myshop_order_process import *
from main.page.desktop_v3.purchase.pe_tx_payment_base import *
from main.page.desktop_v3.purchase.pe_tx_order_status import *
from main.page.desktop_v3.purchase.pe_tx_payment_confirmation import *
from main.page.desktop_v3.purchase.pe_tx_transaction_list import *
from main.activity.desktop_v3.activity_inbox_review import *


class TransactionActivity:

    # constructor of TransactionActivity
    def __init__(self, driver):
        self.login = LoginPage(driver)
        self.logout = LogoutPage(driver)
        self.shop = ShopPage(driver)
        self.prod = ProductPage(driver)
        self.tx = TxPage(driver)
        self.order_status = OrderStatusPage(driver)
        self.myshop_order = MyshopOrderPage(driver)
        self.process_order = MyshopOrderProcessPage(driver)
        self.confirm_payment = PaymentConfirmationPage(driver)
        self.list_transact = TransactionListPage(driver)
        self.inbox_review = inboxReviewActivity()
        self.inbox_review.setObject(driver)

    def set_parameter(self, global_parameter):
        self.dict = global_parameter

    def transaction_with(self, payment):
        order_product_name = None
        order_shop_name = None
        self.login.open(self.dict['site'])
        self.login.do_login(self.dict['email_buyer'], self.dict['password_buyer'])
        i = 0
        while i < self.dict['loop']:
            print("Automated Transaction -", (i + 1))
            self.shop.domain(self.dict['site'], self.dict['domain_shop'])
            self.shop.choose_product()
            self.prod.add_to_cart(self.dict['shipping_agency'], self.dict['is_add_address'])
            self.tx.choose_payment(payment)
            if payment == "Partial Deposit":
                self.tx.choose_partial_deposit(self.dict['partial_deposit'])
            if self.dict["is_dropshipper"] == True:
                self.tx.dropshipper(self.dict['dropshipper_name'], self.dict['dropshipper_telp'])
            self.tx.checkout()
            self.tx.pay(self.dict['password_buyer'])
            if self.dict["is_confirm_payment"] == True and payment == "Bank":
                self.list_transact.open(self.dict['site'])
                inv = self.list_transact.get_last_inv()
                self.confirm_payment.open(self.dict['site'])
                self.confirm_payment.confirm_payment(inv, self.dict['payment_method'], self.dict['destination_bank'], self.dict['password_buyer'])
            if self.dict["is_until_finish"] == True and payment == "Deposit":
                self.order_status.open(self.dict['site'])
                inv, order_product_name, order_shop_name = self.order_status.get_last_inv()
                self.logout.open(self.dict['site'])
                self.login.open(self.dict['site'])
                self.login.do_login(self.dict['email_seller'], self.dict['password_seller'])
                self.myshop_order.open(self.dict['site'])
                self.myshop_order.response_order(inv)
                time.sleep(5)
                self.process_order.open(self.dict['site'])
                self.process_order.confirm_shipping(inv)
                self.logout.open(self.dict['site'])
                self.login.open(self.dict['site'])
                self.login.do_login(self.dict['email_buyer'], self.dict['password_buyer'])
                self.order_status.open(self.dict['site'])
                self.order_status.finish_order(inv)
                self.inbox_review.goto_inbox_review(self.dict['site'])
                self.inbox_review.change_filter_all()
                self.inbox_review.skip_review(order_product_name, order_shop_name)
            i = i + 1