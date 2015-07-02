#!/usr/bin/env python

from main.page.base import BasePage
from selenium.webdriver.common.by import By

class TxPaymentBasePage(BasePage):

    #Tab Locators
    _tab_payment_confirmation_loc = (By.XPATH, '//*[@id="transaction-menu"]/li[1]/a')
    _tab_tx_order_status_loc = (By.XPATH, '//*[@id="transaction-menu"]/li[2]/a')
    _tab_tx_delivery_confirm_loc = (By.XPATH, '//*[@id="transaction-menu"]/li[3]/a')
    _tab_tx_order_list_loc = (By.XPATH, '//*[@id="transaction-menu"]/li[4]/a')

    #Global Actions
    def select_tab_payment_confirmation(self):
        tab_payment_confirmation = self.find_element(*self._tab_payment_confirmation_loc)
        self._click(tab_payment_confirmation)
        if (self.driver.current_url == "https://www.tokopedia.com/tx_payment_confirm.pl"):
            print("Saat ini berada di https://www.tokopedia.com/tx_payment_confirm.pl")
        else:
            print(self.driver.current_url + " tidak benar.")

    def select_tab_order_status(self):
        tab_order_status = self.find_element(*self._tab_tx_order_status_loc)
        self._click(tab_order_status)
        if (self.driver.current_url == "https://www.tokopedia.com/tx_order_status.pl"):
            print("Saat ini berada di https://www.tokopedia.com/tx_order_status.pl")
        else:
            print(self.driver.current_url + " tidak benar.")

    def select_tab_receive_confirmation(self):
        tab_receive_confirmation = self.find_element(*self._tab_tx_delivery_confirm_loc)
        self._click(tab_receive_confirmation)
        if (self.driver.current_url == "https://www.tokopedia.com/tx_delivery_confirm.pl"):
            print("Saat ini berada di https://www.tokopedia.com/tx_delivery_confirm.pl ")
        else:
            print(self.driver.current_url + " tidak benar.")

    def select_tab_transaction_list(self):
        tab_transaction_list = self.find_element(*self._tab_tx_order_list_loc)
        self._click(tab_transaction_list)
        if (self.driver.current_url == "https://www.tokopedia.com/tx_order_list.pl"):
            print("Saat ini berada di https://www.tokopedia.com/tx_order_list.pl")
        else:
            print(self.driver.current_url + " tidak benar.")

