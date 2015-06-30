from main.page.purchase.pe_tx_payment_base import *
from selenium.webdriver.common.by import By

class TransactionListPage(TxPaymentBasePage):
    _page = "tx_order_list.pl"

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
    def open(self, site=""):
        self._open(site, self._page)

    def get_last_inv(self):
        last_order = self.driver.find_element(*self._last_order_loc)
        id_order = last_order.find_element(By.TAG_NAME, "tr").get_attribute("id")
        self.inv = self.driver.find_element(By.XPATH, "//*[@id='"+ id_order +"']/td[2]/a/b")
        return self.inv.text