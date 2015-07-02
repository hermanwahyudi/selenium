#!/usr/bin/env python

from main.page.desktop_v3.sales.pe_myshop_order_base import *
from selenium.webdriver.common.by import By
import time

class MyshopOrderPage(MyshopOrderBasePage):
    _page = "myshop_order.pl"

    #Locators
    #search invoice box, deadline response select box, dan search invoice button nya merupakan 1 set
    _search_invoice_bar_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append input.input-medium')
    _deadline_response_select_box_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append a.selectBox-dropdown')
    _search_invoice_button_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append button.btn')

    
    # instance variable 
    #_condition_order_loc = (By.XPATH, "//*[@id='change-template']")
    _condition_order_loc = (By.CSS_SELECTOR, "div#change-template")
    _order_table_loc = (By.CSS_SELECTOR, "div.list-box-content table.transaction-table")
    _list_order_loc = (By.XPATH, "//div[@class='list-box-content']/table")
    _btn_response_loc = (By.CSS_SELECTOR, "div.dialog-footer button.btn-action")
    #_after_submit_loc = (By.XPATH, "//button[text()='Ok']")
    _after_submit_loc = (By.CSS_SELECTOR, "div.dialog-content div.container-fluid div.row-fluid div.dialog-footer button.btn-action")
  
    #counter
    _counter_loc = (By.XPATH, "//*[@class='count-sales-new-order-value']")
 
    #next page
    _next_page_loc = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div/div/ul/li[last()]/a/strong")

    #Action
    def open(self, site=""):
        self._open(site, self._page)

    def response_order(self, inv):
        found = False

        #print (self.find_element(*self._condition_order_loc).text)
        #condition_order = self.find_element(*self._condition_order_loc)

        # if("No Order List" in condition_order.text or "Tidak ada Daftar Pemesanan" in condition_order.text):
        #     print("No Order List")
        try:
            self.find_element(*self._order_table_loc)
            counter = int(self.find_element(*self._counter_loc).text)
            j, r, s = 0, int(counter/10), int(counter%10)
            if(s > 0):
                r += 1
            while j < r and not found:
                print("Page", int(j+1))
                list_order = self.driver.find_elements(*self._list_order_loc)
                for i in list_order:
                    if inv in i.text:
                        time.sleep(2)
                        id_order = i.find_element(By.TAG_NAME, "tr").get_attribute("id")
                        time.sleep(2)
                        response_order = self.driver.find_element(By.XPATH, "//*[@id='"+id_order+"']/td[3]/div[3]/div/form/div[1]/div/div[2]/button")
                        response_order.click()
                        found = True
                        break
                j += 1
                if(j < r and not found):
                    self.next_page()
                    print("Next page MyshopOrder")
                time.sleep(2)
                if(found == True):
                    self.driver.find_element(*self._btn_response_loc).click()
                    print("Response", inv)
                    time.sleep(4)
                    self.driver.find_element(*self._after_submit_loc).click()
                    print ("after submit btn sukses")


            if(not found):
                print(inv, "not found!")
            time.sleep(1)
        except:
            print ("No Order")



    def next_page(self):
        try:
            next = self.driver.find_element(*self._next_page_loc)
            next.click()
            time.sleep(2)
        except Exception as inst:
            print(inst)