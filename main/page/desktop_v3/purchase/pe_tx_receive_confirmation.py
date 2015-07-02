#!/usr/bin/env python

from main.page.desktop_v3.purchase.pe_tx_payment_base import *

class ReceiveConfirmationPage(TxPaymentBasePage):
    _page = "tx_delivery_confirm.pl"

    #Action
    def open(self, site=""):
        self._open(site, self._page)