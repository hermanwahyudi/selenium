#!/usr/bin/env python

from main.page.desktop_v3.sales.pe_myshop_order_base import *
from selenium.webdriver.common.by import By
from random import randint
import time

class MyshopOrderStatusPage(MyshopOrderBasePage):
    _page = "myshop_order_status.pl"

    #LOCATORS
    #Search Invoice
    _search_invoice_bar_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append input.input-medium')
    _search_invoice_button_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append button.btn')

    #Button Sembunyikan/Tampilkan Semua
    _collapse_show_all_loc = (By.CSS_SELECTOR, 'div#change-template a#collapse_show_all span#colapse_show_open')

    #Jumlah Table transaction
    _table_transaction_loc = (By.CSS_SELECTOR, 'div.row-fluid div.span12 div.list-box-content table.transaction-table')

    #Invoice Link
    _t_invoice_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/div/div/div/table/tbody/tr[1]/td[2]/div[1]/a/b')

    #Buyer Name Link
    _list_buyer_name_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/div/div/div/table/tbody/tr[1]/td[1]/a')

    #Snapshot Product Link (Single)
    _snapshot_product_link = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/span[2]/a')

    #Button Edit Nomor Resi
    _list_edit_ref_number_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/div/div/div/table/tbody/tr[1]/td[2]/div[4]/button[1]')

    #Button Track
    _list_button_track_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/div/div/div/table/tbody/tr[1]/td[2]/div[4]/button[2]')

    #Button Sembunyikan/Tampilkan per transaction
    _list_collapse_show_transaction_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/div/div/div/table[1]/tbody/tr[1]/td[2]/div[5]/small[1]')

    #Action
    def open(self, site=""):
        self._open(site, self._page)