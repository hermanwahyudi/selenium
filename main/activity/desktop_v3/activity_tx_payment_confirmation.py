from main.page.purchase.pe_tx_payment_confirmation import *
from main.page.purchase.pe_tx_order_status import *
from main.page.purchase.pe_tx_receive_confirmation import *
from main.page.purchase.pe_tx_transaction_list import *

class paymentConfirmation():
    def goto_payment_confirmation(self, driver, site):
        payment_confirmation_page = PaymentConfirmationPage(driver)
        payment_confirmation_page.open(site)

    def select_payment_confirmation(self, driver):
        payment_confirmation_page = PaymentConfirmationPage(driver)
        payment_confirmation_page.select_tab_payment_confirmation()


class orderStatus():
    def goto_order_status(self, driver,site):
        order_status_page = OrderStatusPage(driver)
        order_status_page.open(site)

    def select_order_status(self, driver):
        order_status_page = OrderStatusPage(driver)
        order_status_page.select_tab_order_status()

class receiveConfirmation():
    def goto_receive_confirmation(self, driver, site):
        receive_confirmation_page = ReceiveConfirmationPage(driver)
        receive_confirmation_page.open(site)

    def select_receive_confirmation(self, driver):
        receive_confirmation_page = ReceiveConfirmationPage(driver)
        receive_confirmation_page.select_tab_receive_confirmation()


class transactionList():
    def goto_transaction_list(self, driver, site):
        transaction_list_page = TransactionListPage(driver)
        transaction_list_page.open(site)

    def select_transaction_list(self, driver):
        transaction_list_page = TransactionListPage(driver)
        transaction_list_page.select_tab_transaction_list()



