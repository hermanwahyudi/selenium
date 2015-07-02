#!/usr/bin/env python

from main.page.desktop_v3.purchase.pe_tx_payment_base import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
import time

class OrderStatusPage(TxPaymentBasePage):
    _page = "tx_order_status.pl"

    #LOCATORS
    #Button Sembunyikan/Tampilkan Semua
    _collapse_show_all_loc = (By.CSS_SELECTOR, 'a#collapse_show_all span#colapse_show_open')

    #Invoice Link
    _order_invoice_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[2]/a/b')

    # instance variable last order loc
    _last_order_loc = (By.XPATH, "//*[@class='list-box-content']/table")

    # instance variable button finish
    _btn_finish_loc = (By.XPATH, "//*[@id='frm_delivery_action']/div[2]/button[2]")
    _after_submit_loc = (By.XPATH, "//button[text()='Ok']")


    #Action
    def open(self, site=""):
        self._open(site, self._page)

    def get_last_inv(self):
        last_order = self.driver.find_element(*self._last_order_loc)
        id_order = last_order.find_element(By.TAG_NAME, "tr").get_attribute("id")
        id_number = id_order.split("-")[1]
        inv = self.driver.find_element(By.XPATH, "//*[@id='"+ id_order +"']/td[2]/a/b")
        #self.driver.execute_script("document.querySelector('tr#detail-drop-"+ id_order +"').style.display= '';")
        self.find_element(*self._collapse_show_all_loc).click()
        time.sleep(5)
        #WebDriverWait(self.driver, 15).until(EC.visibility_of((By.CSS_SELECTOR, "tr#detail-drop-"+id_order+" td.dashed-border")))
        order_product_name = self.find_element(By.CSS_SELECTOR, "tr#detail-drop-"+ id_number +" td.dashed-border table.transaction-detail tbody tr td.p-10 span.pull-left a.product-name").text
        order_shop_name = self.find_element(By.CSS_SELECTOR, "div.list-box-content table.transaction-table tbody tr#order-"+ id_number +" td.span3 a").text
        return inv.text, order_product_name ,order_shop_name

    def finish_order(self, inv):
        found = False
        try:
            list_order = self.driver.find_elements(*self._last_order_loc)
            for i in list_order:
                if inv in i.text:
                    print(inv)
                    found = True
                    time.sleep(3)
                    id_order = i.find_element(By.TAG_NAME, "tr").get_attribute("id")
                    self.driver.find_element(By.XPATH, "//*[@id='"+id_order+"']/td[2]/div[2]/div[2]/button").click()
                    break
            time.sleep(1)
            if(found):
                self.driver.find_element(*self._btn_finish_loc).click()
                time.sleep(2)
                self.driver.find_element(*self._after_submit_loc).click()
            else:
                print(inv, "not found!")
        except Exception as inst:
            print(inst)

