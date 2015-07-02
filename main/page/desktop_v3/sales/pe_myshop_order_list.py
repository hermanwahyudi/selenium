from main.page.desktop_v3.sales.pe_myshop_order_base import *
from selenium.webdriver.common.by import By
from random import randint
import time

class MyshopOrderListPage(MyshopOrderBasePage):
    _page = "myshop_order_list.pl"

    #LOCATORS
    #Search Invoice
    _search_invoice_bar_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append input.input-medium')
    _t_status_select_box_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append a.selectBox')
    _start_date_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append input#start-date')
    _end_date_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append input#end-date')
    _search_invoice_button_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append button.btn')

    #Button Sembunyikan/Tampilkan Semua
    _collapse_show_all_loc = (By.CSS_SELECTOR, 'div#change-template a#collapse_show_all span#colapse_show_open')

    #Jumlah Table transaction
    _table_transaction_loc = (By.CSS_SELECTOR, 'div.row-fluid div.span12 div.list-box-content table.transaction-table')

    #Invoice Link
    _t_invoice_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/div/div/div/table/tbody/tr[1]/td[2]/div[1]/a/b')

    #Buyer Name Link
    _buyer_name_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/div/div/div/table/tbody/tr[1]/td[1]/a')

    #Snapshot Product Link (Single)
    _snapshot_product_link = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/span[2]/a')

    #Button Sembunyikan/Tampilkan per transaction
    _list_collapse_show_transaction_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/div/div/div/table[1]/tbody/tr[1]/td[2]/div[5]/small[1]')

    _last_order_loc = (By.XPATH, "//*[@class='list-box-content']/table")

    #Action
    def open(self, site=""):
        self._open(site, self._page)

    def get_last_inv(self):
        last_order = self.driver.find_element(*self._last_order_loc)
        id_order = last_order.find_element(By.TAG_NAME, "tr").get_attribute("id")
        self.inv = self.driver.find_element(By.XPATH, "//*[@id='"+ id_order +"']/td[2]/a/b")
        return self.inv.text
