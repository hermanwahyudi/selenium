__author__ = 'QC1'

from main.page.base import *
from selenium.webdriver.common.by import By
from utils.function.general import *
import os, time, sys, json, requests
import urllib.parse
import urllib.request

class AdminPage(BasePage):

    _tokopedia_backend_image_loc = (By.XPATH, "/html/body/div[1]/div/div/a/img")

    #backend tabs locator
    _general_tab_loc = (By.XPATH, "/html/body/div[1]/div/ul/li[1]")
    _user_tab_loc = (By.XPATH, "/html/body/div[1]/div/ul/li[2]")
    _shop_tab_loc = (By.XPATH, "/html/body/div[1]/div/ul/li[3]")
    _catalog_tab_loc = (By.XPATH, "/html/body/div[1]/div/ul/li[4]")
    _product_tab_loc = (By.XPATH, "/html/body/div[1]/div/ul/li[5]")
    _transaction_tab_loc = (By.XPATH, "/html/body/div[1]/div/ul/li[6]")
    _order_tab_loc = (By.XPATH, "/html/body/div[1]/div/ul/li[7]")
    _statistic_tab_loc = (By.XPATH, "/html/body/div[1]/div/ul/li[8]")
    _monitor_tab_loc = (By.XPATH, "/html/body/div[1]/div/ul/li[9]")
    _shipping_agency_tab_loc = (By.XPATH, "/html/body/div[1]/div/ul/li[10]")
    _seo_tab_loc = (By.XPATH, "/html/body/div[1]/div/ul/li[11]")
    _marketing_tab_loc = (By.XPATH, "/html/body/div[1]/div/ul/li[12]")
    _system_tab_loc = (By.XPATH, "/html/body/div[1]/div/ul/li[13]")

    _abuser_name_input_loc = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div[1]/input")
    _total_abuse_input_loc = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div[2]/input")
    _search_abuser_button_loc = (By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/button")
    _view_abuse_button_loc = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[5]/a[1]")

    #look for the report description and compare it with dict ['description']
    _reason_message_loc = (By.CSS_SELECTOR, "html.dialog-mode body.img-down.admin-page div#dialog.jqmWindow.jqmID1 div.jqm-inner div.content div#content-table div#admin-view-abuse_wrapper.dataTables_wrapper table#admin-view-abuse.display.data-table tbody tr.odd td.fs-12 div")


    def domain(self, site, x=""):
        self._open(site, x)
        self.target_domain = x

    def check_admin_page(self):
        print("Inspecting elements on backend page #1: tokopedia image...")
        self.mouse_hover_to(*self._tokopedia_backend_image_loc)
        print("Inspecting elements on backend page #1 succeeded: tokopedia image found!")
        time.sleep(1)
        print("Inspecting elements on backend page #2: general tab...")
        self.mouse_hover_to(*self._general_tab_loc)
        print("Inspecting elements on backend page #2 succeeded: general tab found!")
        time.sleep(1)
        print("Inspecting elements on backend page #3: user tab...")
        self.mouse_hover_to(*self._user_tab_loc)
        print("Inspecting elements on backend page #3 succeeded: user tab found!")
        time.sleep(1)
        print("Inspecting elements on backend page #4: shop tab...")
        self.mouse_hover_to(*self._shop_tab_loc)
        print("Inspecting elements on backend page #4 succeeded: shop tab found!")
        time.sleep(1)
        print("Inspecting elements on backend page #5: catalog tab...")
        self.mouse_hover_to(*self._catalog_tab_loc)
        print("Inspecting elements on backend page #5 succeeded: catalog tab found!")
        time.sleep(1)
        print("Inspecting elements on backend page #6: product tab...")
        self.mouse_hover_to(*self._product_tab_loc)
        print("Inspecting elements on backend page #6 succeeded: product tab found!")
        time.sleep(1)
        print("Inspecting elements on backend page #7: transaction tab...")
        self.mouse_hover_to(*self._transaction_tab_loc)
        print("Inspecting elements on backend page #7 succeeded: transaction tab found!")
        time.sleep(1)
        print("Inspecting elements on backend page #8: order tab...")
        self.mouse_hover_to(*self._order_tab_loc)
        print("Inspecting elements on backend page #8 succeeded: order tab found!")
        time.sleep(1)
        print("Inspecting elements on backend page #9: statistic tab...")
        self.mouse_hover_to(*self._statistic_tab_loc)
        print("Inspecting elements on backend page #9 succeeded: statistic tab found!")
        time.sleep(1)
        print("Inspecting elements on backend page #10: monitor tab...")
        self.mouse_hover_to(*self._monitor_tab_loc)
        print("Inspecting elements on backend page #10 succeeded: monitor tab found!")
        time.sleep(1)
        print("Inspecting elements on backend page #11: shipping tab...")
        self.mouse_hover_to(*self._shipping_agency_tab_loc)
        print("Inspecting elements on backend page #11 succeeded: shipping tab found!")
        time.sleep(1)
        print("Inspecting elements on backend page #12: seo tab...")
        self.mouse_hover_to(*self._seo_tab_loc)
        print("Inspecting elements on backend page #12 succeeded: seo tab found!")
        time.sleep(1)
        print("Inspecting elements on backend page #13: marketing tab...")
        self.mouse_hover_to(*self._marketing_tab_loc)
        print("Inspecting elements on backend page #13 succeeded: marketing tab found!")
        time.sleep(1)
        print("Inspecting elements on backend page #14: system tab...")
        self.mouse_hover_to(*self._system_tab_loc)
        print("Inspecting elements on backend page #14 succeeded: system tab found!")
        time.sleep(1)
        print("All elements found! Backend element inspection completed!")


    def search_abuser_name_and_report(self, abuserName, desc):
        print("Searching for the report started")
        print("Sending the abuser name..")
        self.find_element(*self._abuser_name_input_loc).send_keys(abuserName)
        self.find_element(*self._search_abuser_button_loc).click()
        print("Finding the abuser name. . .")
        time.sleep(1)
        print("Name found! Checking reason. . .")
        self.find_element(*self._view_abuse_button_loc).click()
        time.sleep(2)
        print ("The reason message in the backend is : ", self.find_element(*self._reason_message_loc).text)
        time.sleep(2)
        reasonMessage = self.find_element(*self._reason_message_loc).text
        return reasonMessage

