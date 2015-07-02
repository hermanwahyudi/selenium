#!/usr/bin/env python

import time, unittest, os, sys
from selenium import webdriver
from main.page.desktop_v3.login.pe_login import *
from main.page.desktop_v3.login.pe_logout import *
from main.page.desktop_v3.shop.pe_shop import *
from main.page.desktop_v3.product.pe_product import *
from main.page.desktop_v3.backend.pe_admin_report_abuse_product import *

class ReportProductActivity:

    def __init__(self, driver):
        self.login = LoginPage(driver)
        self.logout = LogoutPage(driver)
        self.shop = ShopPage(driver)
        self.prod = ProductPage(driver)
        self.admin = AdminPage(driver)

    def set_parameter(self, param):
        self.dict = param

    def set_report_product(self, category, desc):
        self.login.open(self.dict['site'])
        self.login.do_login(self.dict['email_buyer'], self.dict['password_buyer'])
        self.shop.domain(self.dict['site'], self.dict['domain_shop'])
        self.shop.choose_product()
        print("Report product", self.dict['category'])
        self.prod.report_product(category, desc)

    def check_product_report(self, abuserName, desc):
        self.login.open(self.dict['site'])
        self.login.do_login(self.dict['email_buyer'], self.dict['password_buyer'])
        self.admin.domain(self.dict['site'], self.dict['backend_link'])
        self.admin.check_admin_page()
        reasonMessage = self.admin.search_abuser_name_and_report(abuserName, desc)
        return reasonMessage



