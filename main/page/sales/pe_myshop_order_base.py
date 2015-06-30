from main.page.base import BasePage
from selenium.webdriver.common.by import By
from random import randint
import time


class MyshopOrderBasePage(BasePage):

    #Tab Locators
    _tab_new_order_loc = (By.XPATH, '//*[@id="transaction-menu"]/li[1]/a')
    _tab_shipping_confirmation_loc = (By.XPATH, '//*[@id="transaction-menu"]/li[2]/a')
    _tab_shipping_status_loc = (By.XPATH, '//*[@id="transaction-menu"]/li[3]/a')
    _tab_transaction_list_loc = (By.XPATH, '//*[@id="transaction-menu"]/li[4]/a')

    #Global Action
    def select_tab_new_order(self):
        tab_new_order = self.find_element(*self._tab_new_order_loc)
        self._click(tab_new_order)
        if (self.driver.current_url == "https://www.tokopedia.com/myshop_order.pl"):
            print ("saat ini berada di %s" %(self.driver.current_url))
        else:
            print(self.driver.current_url + " is a wrong accessed page")

    def select_tab_shipping_confirmation(self):
        tab_shipping_confirmation = self.find_element(*self._tab_shipping_confirmation_loc)
        self._click(tab_shipping_confirmation)
        if (self.driver.current_url == "https://www.tokopedia.com/myshop_order_process.pl"):
            print ("saat ini berada di %s" %(self.driver.current_url))
        else:
            print(self.driver.current_url + " is a wrong accessed page")

    def select_tab_shipping_status(self):
        tab_shipping_status = self.find_element(*self._tab_shipping_status_loc)
        self._click(tab_shipping_status)
        if (self.driver.current_url == "https://www.tokopedia.com/myshop_order_status.pl"):
            print ("saat ini berada di %s" %(self.driver.current_url))
        else:
            print(self.driver.current_url + " is a wrong accessed page")

    def select_tab_transaction_list(self):
        tab_transaction_list = self.find_element(*self._tab_transaction_list_loc)
        self._click(tab_transaction_list)
        if (self.driver.current_url == "https://www.tokopedia.com/myshop_order_list.pl"):
            print ("saat ini berada di %s" %(self.driver.current_url))
        else:
            print(self.driver.current_url + " is a wrong accessed page")
















