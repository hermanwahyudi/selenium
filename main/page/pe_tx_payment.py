import os,sys, time
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from base import BasePage
from selenium.webdriver.common.by import By

class TxPaymentBasePage(BasePage):

    #Tab Locators
    _tab_payment_confirmation_loc = (By.XPATH, '//*[@id="transaction-menu"]/li[1]/a')
    _tab_tx_order_status_loc = (By.XPATH, '//*[@id="transaction-menu"]/li[2]/a')
    _tab_tx_delivery_confirm_loc = (By.XPATH, '//*[@id="transaction-menu"]/li[3]/a')
    _tab_tx_order_list_loc = (By.XPATH, '//*[@id="transaction-menu"]/li[4]/a')

    #Global Actions
    def select_tab_payment_confirmation(self):
        tab_payment_confirmation = self.find_element(*self._tab_payment_confirmation_loc)
        self._click(tab_payment_confirmation)
        if (self.driver.current_url == PaymentConfirmationPage.url):
            print("Saat ini berada di " + PaymentConfirmationPage.url)
        else:
            print(self.driver.current_url + " tidak benar.")

    def select_tab_order_status(self):
        tab_order_status = self.find_element(*self._tab_tx_order_status_loc)
        self._click(tab_order_status)
        if (self.driver.current_url == OrderStatusPage.url):
            print("Saat ini berada di " + OrderStatusPage.url)
        else:
            print(self.driver.current_url + " tidak benar.")

    def select_tab_receive_confirmation(self):
        tab_receive_confirmation = self.find_element(*self._tab_tx_delivery_confirm_loc)
        self._click(tab_receive_confirmation)
        if (self.driver.current_url == ReceiveConfirmationPage.url):
            print("Saat ini berada di " + ReceiveConfirmationPage.url)
        else:
            print(self.driver.current_url + " tidak benar.")

    def select_tab_transaction_list(self):
        tab_transaction_list = self.find_element(*self._tab_tx_order_list_loc)
        self._click(tab_transaction_list)
        if (self.driver.current_url == TransactionListPage.url):
            print("Saat ini berada di " + TransactionListPage.url)
        else:
            print(self.driver.current_url + " tidak benar.")

class PaymentConfirmationPage(TxPaymentBasePage):
    url = "https://www.tokopedia.com/tx_payment_confirm.pl"

    #LOCATORS
    #Button Konfirmasi Order
    _button_confirmation_upper_loc = (By.CSS_SELECTOR, 'div.span12 div.pull-left button.confirm-payment-btn')
    _button_confirmation_lower_loc = (By.CSS_SELECTOR, 'div.mb-30 button.confirm-payment-btn')

    #Button Cancel Order
    _button_cancel_upper_loc = (By.CSS_SELECTOR, 'div.span12 div.pull-left')
    _button_cancel_lower_loc = (By.CSS_SELECTOR, 'div.mb-30 button.cancel-payment-btn')

    #Button Sembunyikan/Tampilkan Semua
    _collapse_show_all_loc = (By.CSS_SELECTOR, 'a#collapse_show_all span#colapse_show_open')

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

    #Action
    def open(self):
        self._open(self.url)

    def show_all_confirm(self):
        time.sleep(2)
        self.driver.find_element(*self._collapse_show_all_loc).click()

    def payment_method(self, method="", password=""):
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
        except Exception as inst:
            print(inst)

    def confirm_payment(self, inv, method="", password=""):
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
                        time.sleep(2)
                        found = True
                        self.driver.find_element(*self._check_selected_loc).click()
                time.sleep(1)
                if(found == True):
                    if(method == "Saldo Tokopedia"):
                        self.payment_method(method, password)
                    time.sleep(2)
                    self.driver.find_element(*self._btn_submit_loc).click()
                else:
                    print(inv, "not found!")

        except Exception as inst:
            print(inst)


class OrderStatusPage(TxPaymentBasePage):
    url = "https://www.tokopedia.com/tx_order_status.pl"

    #LOCATORS
    #Button Sembunyikan/Tampilkan Semua
    _collapse_show_all_loc = (By.CSS_SELECTOR, 'a#collapse_show_all span#colapse_show_open')

    #Invoice Link
    _order_invoice_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[2]/a/b')

    # intance variable last order loc
    _last_order_loc = (By.XPATH, "//*[@class='list-box-content']/table")

    # intance variable button finish
    _btn_finish_loc = (By.XPATH, "//*[@id='frm_delivery_action']/div[2]/button[2]")
    _after_submit_loc = (By.XPATH, "//button[text()='Ok']")

    #Action
    def open(self):
        self._open(self.url)

    def get_last_inv(self):
        last_order = self.driver.find_element(*self._last_order_loc)
        id_order = last_order.find_element(By.TAG_NAME, "tr").get_attribute("id")
        self.inv = self.driver.find_element(By.XPATH, "//*[@id='"+ id_order +"']/td[2]/a/b")
        return self.inv.text

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

class ReceiveConfirmationPage(TxPaymentBasePage):
    url = "https://www.tokopedia.com/"


    #Action
    def open(self):
        self._open(self.url)


class TransactionListPage(TxPaymentBasePage):
    url = "https://www.tokopedia.com/tx_order_list.pl"

    #LOCATORS
    #Search Invoice
    _search_invoice_bar_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter input.input-medium')
    _search_invoice_button_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter button.pull-left')
    _search_invoice_status_loc = (By.CSS_SELECTOR, 'div.row-fluid form#form-filter a.selectBox-dropdown')

    #Button Sembunyikan/Tampilkan Semua
    _collapse_show_all_loc = (By.CSS_SELECTOR, 'a#collapse_show_all span#colapse_show_open')

    #Invoice Link
    _order_invoice_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/div[1]/div/div/table/tbody/tr[1]/td[2]/a/b')

    #Snapshot product
    _snapshot_product_loc = (By.XPATH, '/html/body/div[1]/div[5]/div/div[2]/div[3]/div[1]/div/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[1]/span[2]/a')

    _last_order_loc = (By.XPATH, "//*[@class='list-box-content']/table")

    #Action
    def open(self):
        self._open(self.url)

    def get_last_inv(self):
        last_order = self.driver.find_element(*self._last_order_loc)
        id_order = last_order.find_element(By.TAG_NAME, "tr").get_attribute("id")
        self.inv = self.driver.find_element(By.XPATH, "//*[@id='"+ id_order +"']/td[2]/a/b")
        return self.inv.text
