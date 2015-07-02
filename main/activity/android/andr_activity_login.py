__author__ = 'QC1'

from main.page.android.andr_pe_index import *
from main.page.android.andr_pe_login import *


class ActivityLogin():

    def do_login(self, driver, email, password):
        index_page = PageIndex(driver)
        login_page = PageLogin(driver)

        index_page.tap_login()
        login_page.input_email(email)
        login_page.input_password(password)
        login_page.sign_in()
        login_page.snooze()
        login_page.login_validation()

    def do_login_input_empty(self, driver):
        index_page = PageIndex(driver)
        login_page = PageLogin(driver)

        index_page.tap_login()
        login_page.sign_in()
        sleep(1)
        login_page.check_login_button()


    def seller_login_validation(self, driver):
        index_page = PageIndex(driver)
        print("Able to swipe in to favorite shop. Tap into profile.")
        index_page.tap_profile()
        print("Able to tap into my profile. Now tap into my store")
        index_page.tap_my_store()
        print("Able to tap into my store. Seller login successful")

    def buyer_login_validation(self, driver):
        index_page = PageIndex(driver)
        print("Able to swipe in to favorite shop. Tap into profile.")
        index_page.tap_profile("buyer")