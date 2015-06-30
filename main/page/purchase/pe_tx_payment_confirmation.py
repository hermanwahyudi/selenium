#from main.page.base import BasePage
from main.page.purchase.pe_tx_payment_base import *
from selenium.webdriver.common.by import By
import time

class PaymentConfirmationPage(TxPaymentBasePage):
    _page = "tx_payment_confirm.pl"

    #LOCATORS
    #Button Konfirmasi Order
    _button_confirmation_upper_loc = (By.CSS_SELECTOR, 'div.span12 div.pull-left button.confirm-payment-btn')
    _button_confirmation_lower_loc = (By.CSS_SELECTOR, 'div.mb-30 button.confirm-payment-btn')

    #Button Cancel Order
    _button_cancel_upper_loc = (By.CSS_SELECTOR, 'div.span12 div.pull-left')
    _button_cancel_lower_loc = (By.CSS_SELECTOR, 'div.mb-30 button.cancel-payment-btn')

    #Button Sembunyikan/Tampilkan Semua
    _collapse_show_all_loc = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div/div/div/a/span[1]")

    #Checkbox all
    _checkbox_all_payment_upper_loc = (By.CSS_SELECTOR, 'div.pull-left input.checkall')

    #Jumlah Table Payment Confirmation
    _table_payment_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div/div/div/table/tbody/tr[1]')

    #Button Sembunyikan/Tampilkan per payment
    _list_collapse_show_payment_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]/div[3]/div[2]/small[1]')

    #Invoice Link
    _p_invoice_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div/div/div/table/tbody/tr[2]/td/a[2]/b')

    #Snapshot product Link (Single)
    _snapshot_product_name_loc = (By.XPATH,'/html/body/div[1]/div[5]/div/div[2]/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/span[2]/a')

    #Button 'Package Received'
    _button_package_received = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[2]/div[2]/div[2]/button[1]')

    #Button 'Track'
    _button_track = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[2]/div[2]/div[2]/button[2]')

    #Button 'Komplain'
    _button_komplain = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[2]/div[2]/div[2]/a')

    _notes_loc = (By.ID, "notes")
    _password_deposit_loc = (By.ID, "password_deposit")
    _list_payment_method_loc = (By.XPATH, "//select[@id='payment-method']/option")
    _condition_confirm_loc = (By.XPATH, "//div[@id='change-template']")
    _list_confirm_loc = (By.XPATH, "//div[@id='change-template']/div")
    _check_selected_loc = (By.XPATH, "//*[@id='change-template']/div/div/div[2]/button[1]/b")
    _btn_submit_loc = (By.CSS_SELECTOR, "div.dialog-footer button.btn-action")
    _total_inv_loc = (By.XPATH, "/html/body/div[3]/div[1]/div[2]/div/div/div/form[1]/div[2]/div[2]/strong")
    _list_dest_account_bank_loc = (By.XPATH, "//*[@id='system-bank']/option")
    _payment_amount_loc = (By.XPATH, "//*[@name='payment_amt']")

    #Action
    def open(self, site=""):
        self._open(site, self._page)

    def asd(self):
        self.select_tab_transaction_list()

    def show_all_confirm(self):
        time.sleep(2)
        self.driver.find_element(*self._collapse_show_all_loc).click()
        print("Show all payment confirmation.")

    def payment_method(self, method="", dest_bank="", password=""):
        try:
            list_payment_method = self.driver.find_elements(*self._list_payment_method_loc)
            for x in list_payment_method:
                if(method == x.text):
                    print(x.text)
                    x.click()
            if(method == "Saldo Tokopedia"):
                self.driver.find_element(*self._notes_loc).send_keys("QC")
                time.sleep(1)
                self.driver.find_element(*self._password_deposit_loc).send_keys(password)
            elif(method == "Transfer ATM"):
                dest_account = self.driver.find_elements(*self._list_dest_account_bank_loc)
                for i in dest_account:
                    y = i.text
                    if(dest_bank in y):
                        print(y)
                        i.click()
                        break
                t = self.driver.find_element(*self._total_inv_loc).text
                s = ""
                for i in t:
                    if i.isdigit():
                        s += i
                print(s)
                self.driver.find_element(*self._payment_amount_loc).send_keys(int(s))
                self.driver.find_element(*self._notes_loc).send_keys("QC Automated")
                time.sleep(1)
        except Exception as inst:
            print(inst)

    def confirm_payment(self, inv, method="", dest_bank="", password=""):
        found = False
        try:
            condition_confirm = self.driver.find_element(*self._condition_confirm_loc)
            if("No Payment Confirmation" in condition_confirm.text or "Tidak ada Data Konfirmasi"  in condition_confirm.text):
                print("No Payment Confirmation")
            else:
                self.show_all_confirm()
                time.sleep(3)
                list_confirm = self.driver.find_elements(*self._list_confirm_loc)
                for x in list_confirm:
                    if(inv in x.text):
                        id_confirmation = x.find_element(By.TAG_NAME, "tr").get_attribute("id")
                        self.driver.find_element(By.XPATH, "//*[@id='"+id_confirmation+"']/td[1]/input").click()
                        time.sleep(3)
                        found = True
                        self.driver.find_element(*self._check_selected_loc).click()
                time.sleep(1)
                if(found == True):
                    if(method == "Saldo Tokopedia"):
                        self.payment_method(method, password)
                    if(method == "Transfer ATM"):
                        self.payment_method(method, dest_bank)
                    time.sleep(3)
                    self.driver.find_element(*self._btn_submit_loc).click()
                else:
                    print(inv, "not found!")

        except Exception as inst:
            print(inst)