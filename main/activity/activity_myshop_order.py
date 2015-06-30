from main.page.sales.pe_myshop_order import *
from main.page.sales.pe_myshop_order_process import *


class myshopOrderActivity():
    #Myshop Order
    def goto_myshop_order(self, driver, site):
        new_order_page = MyshopOrderPage(driver)
        new_order_page.open(site)

    def select_tab_new_order(self, driver):
        new_order_page = MyshopOrderPage(driver)
        new_order_page.select_tab_new_order()

    #Myshop Order Process
    def goto_myshop_order_process(self, driver, site):
        myshop_order_process_page = MyshopOrderProcessPage(driver)
        myshop_order_process_page.open(site)

    def input_search_for_invoice(self, driver, search=""):
        myshop_order_process_page = MyshopOrderProcessPage(driver)
        myshop_order_process_page.input_search(search)

    def choose_due_date(self, driver, input_due_date=""):
        myshop_order_process_page = MyshopOrderProcessPage(driver)
        myshop_order_process_page.select_due_date(input_due_date)

    def choose_shipment(self, driver, courier=""):
        myshop_order_process_page = MyshopOrderProcessPage(driver)
        myshop_order_process_page.select_shipment(courier)

    def do_search(self, driver):
        myshop_order_process_page = MyshopOrderProcessPage(driver)
        myshop_order_process_page.click_search_button()

    def reject_order(self, driver):
    #[STATE] Check Order
        order_flag = MyshopOrderProcessPage(driver).check_order_exists()
        if order_flag == 0:
            pass
        elif order_flag == 1:
            MyshopOrderProcessPage(driver).do_cancel_order()

    def select_tab_shipping_confirmation(self, driver):
        shipping_confirmation_page = MyshopOrderProcessPage(driver)
        shipping_confirmation_page.select_tab_shipping_confirmation()

