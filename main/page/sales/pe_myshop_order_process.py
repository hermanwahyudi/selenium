from main.page.sales.pe_myshop_order_base import *
from selenium.webdriver.common.by import By
import time

class MyshopOrderProcessPage(MyshopOrderBasePage):
    _page = "myshop_order_process.pl"

    list_order_info = {
        'info_no_data_ID' : "No order List",
        'info_no_data_EN' : "Tidak ada Daftar Pemesanan"
    }

    lists_due_date_loc = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div[3]/form/div/div/select[1]/option")

    lists_courier_loc = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div[3]/form/div/div/select[2]/option")

    flag = 0

    #Locators
    #Template Order
    _order_table_loc = (By.CSS_SELECTOR, 'table.table-bordered tbody')
    _order_count_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[4]/div[2]/div/div/table/tbody/tr')

    #Search Invoice
    _search_invoice_bar_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append input.input-medium')
    _due_date_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append div.pull-left select.w-80')
    _shipment_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter div.input-append div.pull-left select.w-120')
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
    _button_cancel_loc = (By.CSS_SELECTOR, 'div.container-fluid div.row-fluid div.dialog-footer button.jqmClose')
    _button_confirm_cancel_loc = (By.CSS_SELECTOR, 'div.container-fluid div.row-fluid div.dialog-footer button.jqmYES')

    #Reject Confirmation (After Cancel Confirmation)
    _reject_ok_confirm_loc = (By.CSS_SELECTOR, 'div.container-fluid div.row-fluid div.dialog-footer button.jqmClose')

    # incstance varibale 
    _condition_confirm_loc = (By.XPATH, "//*[@id='change-template']")
    _list_order_loc = (By.XPATH, "//*[@id='change-template']/div[2]/div/div/table/tbody/tr")
    _btn_confirm_loc = (By.CSS_SELECTOR, "div.dialog-footer button.btn-action")
    _after_submit_loc = (By.XPATH, "//button[text()='Ok']")

    #Action
    def open(self, site=""):
        self._open(site, self._page)

    def input_search(self, search=""):
        self.driver.find_element(*self._search_invoice_bar_loc).send_keys(search)


    def select_due_date(self, input_due_date=""):
        self.driver.execute_script("document.querySelector('div.input-append select.w-80').style.display = '';")
        self.driver.execute_script("document.querySelector('div.input-append a.mr-10').style.display = 'none';")
        self.driver.find_element(*self._due_date_loc).click()
        list_due_date = self.driver.find_elements(*self.lists_due_date_loc)
        for total_due_date in list_due_date:
            if total_due_date.text == input_due_date:
                total_due_date.click()

    def select_shipment(self, input_courier=""):
        self.driver.execute_script("document.querySelector('div.input-append select.w-120').style.display = '';")
        self.driver.execute_script("document.querySelector('div.input-append a.mr-5').style.display = 'none';")
        self.driver.find_element(*self._shipment_loc).click()
        list_courier = self.driver.find_elements(*self.lists_courier_loc)
        for total_courier in list_courier:
            if total_courier.text == input_courier:
                total_courier.click()


    def click_search_button(self):
        search_button = self.driver.find_element(*self._search_invoice_button_loc)
        print("Search for Receiver Name / Invoice...")
        self._click(search_button)
        try:
            self.driver.find_element(*self._order_table_loc)
        except:
            print("No order found")

    def check_order_exists(self):
        try:
            #assert self.list_order_info['info_no_data_ID'] not in self.driver.find_element_by_tag_name("body").text
            #assert self.list_order_info['info_no_data_EN'] not in self.driver.find_element_by_tag_name("body").text
            self.driver.find_element(*self._order_table_loc)
            self.flag = 1
            return self.flag
        except:
            print("No order found")
            return self.flag


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
                time.sleep(3)
                if(found):
                    self.driver.find_element(*self._btn_confirm_loc).click()
                    time.sleep(2)
                    self.driver.find_element(*self._after_submit_loc).click()
                else:
                    print(inv, "not found!")

        except Exception as inst:
            print(inst)

    def do_cancel_order(self):
        #Multiple cancel order
        count_orders = 0
        for each_cancel_button in self.driver.find_elements(*self._single_cancel_loc):
            self.check_visible_element(*self._single_cancel_loc)
            button_cancel = self.find_element(*self._single_cancel_loc)
            self._click(button_cancel)
            time.sleep(1)
            #Input text area
            self.check_visible_element(*self._text_area_cancel_loc)
            text_area_cancel = self.find_element(*self._text_area_cancel_loc)
            text_area_cancel.send_keys("qwertylioup m,nbvcxzpiu!@#^$((*&*{}")
            time.sleep(1)
            #Submit
            self.check_visible_element(*self._button_confirm_cancel_loc)
            self.driver.find_element(*self._button_confirm_cancel_loc).click()
            time.sleep(3)
            #Verify Confirmation
            self.check_visible_element(*self._reject_ok_confirm_loc)
            button_reject_ok_confirm = self.find_element(*self._reject_ok_confirm_loc)
            self._click(button_reject_ok_confirm)
            time.sleep(4)
            count_orders+=1
        print ("Total order reject : %s" %(count_orders))

