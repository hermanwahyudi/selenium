__author__ = 'QC1'

from main.page.android.andr_pe_transaction import *

class ActivityTransaction():

    def do_buyer_purchase(self, driver, password):
        transaction_page = PageTransaction(driver)

        transaction_page.tap_favshop()
        transaction_page.snooze()
        transaction_page.tap_product()
        transaction_page.snooze()
        transaction_page.tap_buy_product()
        transaction_page.snooze()
        transaction_page.tap_buy_detail()
        transaction_page.snooze()
        transaction_page.tap_buy_payment_method()
        transaction_page.snooze()
        transaction_page.tap_buy_final_confirmation(password)

    def do_seller_order_process(self, driver):
        transaction_page = PageTransaction(driver)

        order_process_text = transaction_page.tap_order()
        return order_process_text

    def do_buyer_receive_confirm(self, driver):
        transaction_page = PageTransaction(driver)

        transaction_page.tap_buyer_confirm()