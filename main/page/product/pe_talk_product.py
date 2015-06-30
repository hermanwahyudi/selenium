#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from random import randint
from main.page.base import *
from main.page.product.pe_product import *
import os, time, sys


class TalkProductPage(ProductPage):
    # instance variable
    # _textarea_loc = (By.XPATH, "//textarea[@id='']")
    _textarea_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div[4]/div/div/div[1]/div/textarea[2]')
    _submit_loc = (By.CSS_SELECTOR, "div.talk-input-container button.submit-talk-button")
    _list_of_message_loc = (By.XPATH, '//*[@id="talk-list-container"]')
    _total_message_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div[4]/div/ul/li[3]/a/span')
    _next_page_loc = (By.CSS_SELECTOR,
                      'div.row-fluid div.product-content-container div.product-talk-container div.clear-b div.pull-right ul li a i.icon-chevron-right')

    #tulis dan kirim diskusi
    def input_talk(self, count):
        self.driver.implicitly_wait(10)
        try:
            testnumber = str(count)
            talk = 'asdfghjklmnbvcxzwertyuii #' + testnumber
            self.driver.find_element(*self._textarea_loc).send_keys(talk)
            print('Berhasil memasukkan pesan diskusi')
            time.sleep(2)
            self.driver.find_element(*self._submit_loc).click()
            print('Pesan diskusi berhasil terkirim')
            time.sleep(5)
        except Exception as inst:
            print(inst)

    #klik next page kalo ada
    def click_next_page(self):
        print("Next page found")
        try:
            next_page_elmt = self.find_element(*self._next_page_loc)
            self.click(next_page_elmt)
        except NoSuchElementException:
            print("Next page not found")

    #Get total messages from counter in Tab Discussion. Returning total message (int) if available, or 0 if there's no message
    def get_jumlah_message(self):
        try:
            jumlah_message = self.find_element(*self._total_message_loc).text
            jumlah_message = int(jumlah_message)
            return (jumlah_message)
        except NoSuchElementException:
            return (0)

    #Ambil seluruh pesan diskusi yang ada dalam 1 halaman
    def list_message(self):
        list_all_message = self.find_elements(*self._list_of_message_loc)
        return (list_all_message)

    #ambil semua talk yang baru dikirim
    def list_new_message(self, end_of_list):
        new_list_msg = []
        if (end_of_list) >= 1:
            list_msg = self.list_message()
            print('----get list ....')
            for i in list_msg[0:(end_of_list)]:
                new_list_msg.append(i.get_attribute('class'))
                print('----ID Message :')
                print(i.get_attribute('class'))
            print('daftar message baru OK')
            return (new_list_msg)
        else:
            print('Timeout. Pesan baru belum muncul')
            return (new_list_msg)


    def __str__(self):
        return "Page Talk"