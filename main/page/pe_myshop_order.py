import os,sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from base import BasePage
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
        if (self.driver.current_url == MyshopOrderPage.url):
            print ("saat ini berada di " + MyshopOrderPage.url)
        else:
            print(self.driver.current_url + " tidak benar")

    def select_tab_shipping_confirmation(self):
        tab_shipping_confirmation = self.find_element(*self._tab_shipping_confirmation_loc)
        self._click(tab_shipping_confirmation)
        if (self.driver.current_url == MyshopOrderProcessPage.url):
            print ("saat ini berada di " + MyshopOrderPage.url)
        else:
            print(self.driver.current_url + " tidak benar")

    def select_tab_shipping_status(self):
        tab_shipping_status = self.find_element(*self._tab_shipping_status_loc)
        self._click(tab_shipping_status)
        if (self.driver.current_url == MyshopOrderStatusPage.url):
            print ("saat ini berada di " + MyshopOrderStatusPage.url)
        else:
            print(self.driver.current_url + " tidak benar")

    def select_tab_transaction_list(self):
        tab_transaction_list = self.find_element(*self._tab_transaction_list_loc)
        self._click(tab_transaction_list)
        if (self.driver.current_url == MyshopOrderListPage.url):
            print ("saat ini berada di " + MyshopOrderListPage.url)
        else:
            print(self.driver.current_url + " tidak benar")


class MyshopOrderPage(MyshopOrderBasePage):
    url = "https://www.tokopedia.com/myshop_order.pl"

    #Locators
    #search invoice box, deadline response select box, dan search invoice button nya merupakan 1 set
    _search_invoice_bar_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append input.input-medium')
    _deadline_response_select_box_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append a.selectBox-dropdown')
    _search_invoice_button_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append button.btn')

    
    # instance variable 
    _condition_order_loc = (By.XPATH, "//*[@id='change-template']")
    _list_order_loc = (By.XPATH, "//div[@class='list-box-content']/table")
    _btn_response_loc = (By.CSS_SELECTOR, "div.dialog-footer button.btn-action")
    _after_submit_loc = (By.XPATH, "//button[text()='Ok']")


    #Action
    def open(self):
        self._open(self.url)

    def response_order(self, inv):
        found = False
        try:
            condition_order = self.driver.find_element(*self._condition_order_loc)
            if("No Order List" in condition_order.text or "Tidak ada Daftar Pemesanan" in condition_order.text):
                print("No Order List")
            else:
                list_order = self.driver.find_elements(*self._list_order_loc)
                j = 0
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
                time.sleep(2)
                if(found == True):
                    self.driver.find_element(*self._btn_response_loc).click()
                    time.sleep(2)
                    self.driver.find_element(*self._after_submit_loc).click()
                else:
                    print(inv, "not found!")
                    
        except Exception as inst:
            print(inst)


class MyshopOrderProcessPage(BasePage):
    url = "https://www.tokopedia.com/myshop_order_process.pl"

    list_order_info = {
        'info_no_data_ID' : "No order List",
        'info_no_data_EN' : "Tidak ada Daftar Pemesanan"
    }

    flag = 0

    #Locators
    #Search Invoice
    _search_invoice_bar_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append input.input-medium')
    _due_date_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append div.input-append a.w-80 span.selectBox-label')
    _shipment_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append div.input-append a.w-120 span.selectBox-label')
    _search_invoice_button_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append button.btn')

    #Button Confirm All
    _confirm_all_loc = (By.CSS_SELECTOR, 'div#change-template div.mb-10 button.confirm-multiple')

    #Button Print Multiple
    _print_multiple_loc = (By.CSS_SELECTOR, 'div#change-template div.mb-10 button.print-address-multiple-btn')

    #Checkbox all
    _checkbox_all_loc = (By.CSS_SELECTOR, 'div#change-template div.mb-10 input.checkall')

    #CANCELATION COMPONENT
    #Button Cancel Single
    _single_cancel_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[4]/div[2]/div/div/table/tbody/tr/td[5]/p[3]/a')

    #Cancel Confirmation
    _text_area_cancel_loc = (By.CSS_SELECTOR, 'div.dialog-content div.dialog-msg-confirm textarea.cancel-remark')
    _button_cancel_loc = (By.CSS_SELECTOR, 'div.container-fluid div.row-fluid button.jqmClose')
    _button_confirm_loc = (By.CSS_SELECTOR, 'div.container-fluid div.row-fluid button.jqmYES')

    #Reject Confirmation (After Cancel Confirmation)
    _reject_ok_confirm_loc = (By.CSS_SELECTOR, 'div.container-fluid div.row-fluid div.dialog-footer button.jqmClose')

    # incstance varibale 
    _condition_confirm_loc = (By.XPATH, "//*[@id='change-template']")
    _list_order_loc = (By.XPATH, "//*[@id='change-template']/div[2]/div/div/table/tbody/tr")
    _btn_confirm_loc = (By.CSS_SELECTOR, "div.dialog-footer button.btn-action")
    _after_submit_loc = (By.XPATH, "//button[text()='Ok']")

    #Action
    def open(self):
        self._open(self.url)

    def check_order_exists(self):
        try:
            assert self.list_order_info['info_no_data_ID'] not in self.driver.find_element_by_tag_name("body").text
            assert self.list_order_info['info_no_data_EN'] not in self.driver.find_element_by_tag_name("body").text
            self.flag = 1
        except:
            return print("No order found")

    def confirm_shipping(self, inv):
        found = False
        rand_ref = randint(10000000000, 100000000000)
        try:
            condition_confirm = self.driver.find_element(*self._condition_confirm_loc)
            if("No Order List" in condition_confirm.text or "Tidak ada Daftar Pemesanan" in condition_confirm.text):
                print("No Order List")
            else:
                list_confirm_shipping = self.driver.find_elements(*self._list_order_loc)
                for x in list_confirm_shipping:
                    if(inv in x.text):
                        print(inv)
                        time.sleep(4)
                        id_order = x.get_attribute("id")
                        self.driver.find_element(By.XPATH, "//*[@id='"+id_order+"']/td[4]/div[2]/input").send_keys(rand_ref)
                        time.sleep(1)
                        self.driver.find_element(By.XPATH, "//*[@id='"+id_order+"']/td[5]/p[1]/a").click()
                        found = True
                        break
                time.sleep(2)
                if(found):
                    self.driver.find_element(*self._btn_confirm_loc).click()
                    time.sleep(2)
                    self.driver.find_element(*self._after_submit_loc).click()
                else:
                    print(inv, "not found!")

        except Exception as inst:
            print(inst)


    def do_cancel_order(self):
        #Click Button Cancel
        self.check_visible_element(*self._single_cancel_loc)
        button_cancel = self.find_element(*self._single_cancel_loc)
        self._click(button_cancel)

        #Input text area
        self.check_visible_element(*self._text_area_cancel_loc)
        text_area_cancel = self.find_element(*self._text_area_cancel_loc)
        text_area_cancel.send_keys("qwertylioup m,nbvcxzpiu!@#^$((*&*{}")

        #Submit
        self.check_visible_element(*self._button_confirm_loc)
        button_cancel_confirm = self.find_element(*self._button_confirm_loc)
        self._click(button_cancel_confirm)

        #Verify Confirmation
        self.check_visible_element(*self._reject_ok_confirm_loc)
        button_reject_ok_confirm = self.find_element(*self._reject_ok_confirm_loc)
        self._click(button_reject_ok_confirm)

class MyshopOrderStatusPage(BasePage):
    url = "https://www.tokopedia.com/myshop_order_status.pl"

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
    def open(self):
        self._open(self.url)


class MyshopOrderListPage(BasePage):
    url = "https://www.tokopedia.com/myshop_order_list.pl"

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
    def open(self):
        self._open(self.url)

    def get_last_inv(self):
        last_order = self.driver.find_element(*self._last_order_loc)
        id_order = last_order.find_element(By.TAG_NAME, "tr").get_attribute("id")
        self.inv = self.driver.find_element(By.XPATH, "//*[@id='"+ id_order +"']/td[2]/a/b")
        return self.inv.text


#direct from test-case
#Myshop Order
def goto_myshop_order(driver):
    myshop_order_page = MyshopOrderPage(driver)

    myshop_order_page.open()
    myshop_order_page.select_tab_shipping_confirmation()
    myshop_order_page.select_tab_transaction_list()
    goto_myshop_order_process(driver)

#Myshop Order Process
def goto_myshop_order_process(driver):
    myshop_order_process_page = MyshopOrderProcessPage(driver)

    myshop_order_process_page.open()
    myshop_order_process_page.check_order_exists()
    if myshop_order_process_page.flag == 1:
        myshop_order_process_page.do_cancel_order()
    else:
        pass


#indirect
def from_to_myshop_order_process(driver):
    fromto_myshop_order_process = MyshopOrderProcessPage(driver)




