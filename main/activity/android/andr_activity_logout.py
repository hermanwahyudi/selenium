__author__ = 'QC1'

from main.page.android.andr_pe_index import *


class ActivityLogout():

    def do_logout(self, driver):
        index_page = PageIndex(driver)

        print("Logging out. . .")
        index_page.tap_logout()

