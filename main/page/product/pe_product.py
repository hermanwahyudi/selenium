#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from main.page.base import *
import os, time, sys


class ProductPage(BasePage):
    # instance variable
    _pnav_info_loc = (By.ID, "p-nav-infoprod")
    _pnav_review_loc = (By.ID, "p-nav-review")
    # _pnav_talk_loc = (By.ID, "p-nav-talk")
    _pnav_talk_loc = (By.XPATH, '//*[@id="p-nav-talk"]/a')
    _min_order_loc = (By.ID, "min-order")
    _notes_loc = (By.CSS_SELECTOR, "div.offset1 div.control-group textarea#notes")
    _btn_atc_loc = (By.CSS_SELECTOR, "div.span3 div.mt-70 a#btn-atc i.icon-shopping-cart")
    _list_shipping_agency_loc = (By.XPATH, "//select[@name='shipping_agency']/option")
    _list_service_type_loc = (By.XPATH, "//select[@id='shipping-product']/option")
    _btn_buy_loc = (By.CSS_SELECTOR, "button.btn-buy")

    # instance add new address in add to cart
    _add_addr_loc = (By.XPATH, "//*[@id='new-addr']/small/b")
    _addr_as_loc = (By.XPATH, "//*[@id='sell']/div[3]/div/div[1]/div/p/input")
    _receiver_name_loc = (By.XPATH, "//*[@id='sell']/div[3]/div/div[2]/div[1]/p/input")
    _receiver_telp_loc = (By.XPATH, "//*[@id='sell']/div[3]/div/div[2]/div[2]/p/input")
    _zip_loc = (By.XPATH, "//*[@id='sell']/div[3]/div/div[2]/div[3]/p/input")
    _province_loc = (By.XPATH, "//*[@id='province']/option")
    _regency_loc = (By.XPATH, "//*[@id='city']/option")
    _district_loc = (By.XPATH, "//*[@id='district']/option")
    _addr_loc = (By.XPATH, "//*[@id='address-street']")

    # price alert loc
    _price_alert_link_loc = (By.XPATH, "//*[@id='btn-wishlist']")
    _price_alert_input_loc = (By.XPATH, "//*[@id='wl-price']")
    _price_alert_add_loc = (By.XPATH, "/html/body/div[3]/div[1]/div[2]/div/div/div/form/div[2]/button")
    _price_alert_after_add_loc = (By.XPATH, "//*[@id='rf']/div/button")

    # report product
    _report_product_link_loc = (By.XPATH, "//*[@id='report-it']")
    _list_category_report_loc = (By.XPATH, "//*[@id='r-type']/option")
    _desc_report_loc = (By.XPATH, "//*[@id='r_message']")
    _button_report_loc = (By.XPATH, "//*[@id='d-report']/form/div[3]/button[2]")
    _button_after_report_loc = (By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[2]/div/div/button")

    # dictionary shipping agency
    dict_shipping_agency = {
        "JNE": 1,
        "TIKI": 2,
        "RPX": 3,
        "Wahana": 6,
        "Cahaya": 7,
        "Pandu": 8,
        "First": 9
    }

    def get_name_product(self):
        url = self.driver.current_url
        ar1 = url.split("/")[4]
        ar2 = ar1.split("-")
        self.name_product = ""
        for i in ar2:
            self.name_product = self.name_product + " " + i
        return self.name_product

    def go_to_infoprod(self):
        self.driver.find_element(*self._pnav_infoprod_loc).click()

    def go_to_review(self):
        self.driver.find_element(*self._pnav_review_loc).click()

    def go_to_talk(self):
        self.driver.find_element(*self._pnav_talk_loc).click()

    def report_product(self, category="", desc=""):
        try:
            time.sleep(1)
            self.driver.find_element(*self._report_product_link_loc).click()
            time.sleep(1)
            list_category_report = self.driver.find_elements(*self._list_category_report_loc)
            print(category)
            if category != "":
                for item in list_category_report:
                    if item.text == category:
                        item.click()
                        break
            else:
                rand = randint(0, len(list_category_report) - 1)
                list_category_report[rand].click()
            time.sleep(1)
            self.driver.find_element(*self._desc_report_loc).send_keys(desc)
            self.driver.find_element(*self._button_report_loc).click()
            time.sleep(1)
            b = self.driver.find_element(*self._button_after_report_loc).click()
            print(b)
        except Exception as inst:
            print(inst)

    def price_alert(self, price):
        try:
            time.sleep(4)
            self.driver.find_element(*self._price_alert_link_loc).click()
            time.sleep(1)
            self.driver.find_element(*self._price_alert_input_loc).clear()
            self.driver.find_element(*self._price_alert_input_loc).send_keys(price)
            self.driver.find_element(*self._price_alert_add_loc).click()
            time.sleep(1)
            self.driver.find_element(*self._price_alert_after_add_loc).click()
        except Exception as inst:
            print(inst)

    def add_to_cart(self, shipping_agency, is_add_address):

        # time.sleep(3)
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((self._btn_atc_loc))
        # )
        # element.click()
        print("cari btn buy")
        #self.driver.refresh()
        self.check_visible_element(*self._btn_atc_loc)
        print ("checked visibility")
        coba = self.find_element(*self._btn_atc_loc)
        self.click_on_javascript(coba)

        time.sleep(7)
        notes = ""
        for i in range(10):
            notes += str(i)
        #self.driver.execute_script("document.querySelector('div.jqmWindow').style.display = '';")
        WebDriverWait(self.driver,60 ).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.offset1 div.control-group textarea#notes")))
        #self.check_visible_element(*self._notes_loc)
        self.find_element(*self._notes_loc).send_keys(notes)
        if is_add_address == True:
            self.add_address("addr_as", "receiver_name", "96969696", "12240", "addr")
        self.choose_shipping_agency(shipping_agency)
        time.sleep(1)
        self.driver.find_element(*self._btn_buy_loc).submit()


    def add_address(self, addr_as, receiver_name, receiver_telp, postal_cose, addr):
        try:
            print("Add New Address in Add to Cart")
            self.driver.find_element(*self._add_addr_loc).click()
            time.sleep(1)
            self.driver.find_element(*self._addr_as_loc).send_keys(addr_as)
            self.driver.find_element(*self._receiver_name_loc).send_keys(receiver_name)
            self.driver.find_element(*self._receiver_telp_loc).send_keys(receiver_telp)
            self.driver.find_element(*self._zip_loc).send_keys(postal_cose)
            list_province = self.driver.find_elements(*self._province_loc)
            list_province[randint(1, len(list_province) - 1)].click()
            time.sleep(1)
            list_regency = self.driver.find_elements(*self._regency_loc)
            list_regency[randint(1, len(list_regency) - 1)].click()
            time.sleep(1)
            list_district = self.driver.find_elements(*self._district_loc)
            list_district[randint(1, len(list_district) - 1)].click()
            self.driver.find_element(*self._addr_loc).send_keys(addr)
        except Exception as inst:
            print(inst)

    def choose_shipping_agency(self, x=""):
        try:
            time.sleep(2)
            found = False
            list_shipping_agency = self.driver.find_elements(*self._list_shipping_agency_loc)
            j, k, length = 0, 0, len(list_shipping_agency)
            if (length > 1):
                for i in list_shipping_agency:
                    if i.text == x:
                        found = True
                        j = k
                        break
                    k += 1
                if (x == "" or found == False):
                    j = randint(1, length - 1)
            else:
                j = 0
            time.sleep(1)
            list_shipping_agency[j].click()
            print("Choose shipping agency", list_shipping_agency[j].text)
            time.sleep(1)
            list_service_type = self.driver.find_elements(*self._list_service_type_loc)
            for q in range(len(list_service_type)):
                if q == randint(0, len(list_service_type) - 1):
                    print("Choose service type", list_service_type[q].text)
                    list_service_type[q].click()
                    break
            time.sleep(1)
        except Exception as inst:
            print(inst)

    def __str__(self):
        return "Page product " + self.name_product

