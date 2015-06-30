from main.page.purchase.pe_tx_payment_base import *


class ReceiveConfirmationPage(TxPaymentBasePage):
    _page = "tx_delivery_confirm.pl"

    #Action
    def open(self, site=""):
        self._open(site, self._page)