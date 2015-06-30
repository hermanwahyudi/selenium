from main.page.index.pe_index import *
from selenium.webdriver.common.by import By
from main.lib.user import *

class indexActivity():
    def now_at_index(self, driver):
        index_page = IndexPage(driver)

        my_username = index_page.check_my_username()
        my_deposit = index_page.check_my_deposit()

        index_page.check_all_panel_left()
        index_page.check_all_product_listed()

        user_profile = UserInfo(my_deposit)

        user_profile.getUsername(my_username)
        user_profile.getDeposit()
