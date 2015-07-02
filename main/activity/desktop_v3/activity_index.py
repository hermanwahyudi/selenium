from main.page.desktop_v3.index.pe_index import *
from utils.lib.user import *

class indexActivity():
    def now_at_index(self, driver):
        index_page = IndexPage(driver)

        my_username = index_page.check_my_username()
        my_deposit = index_page.check_my_deposit()

        index_page.check_all_panel_left()
        index_page.check_all_product_listed()

        # user_profile = UserInfo(my_deposit)
        #
        # user_profile.getUsername(my_username)
        # user_profile.getDeposit()

    def index_no_shop(self, driver):
        index_page = IndexPage(driver)

        my_username = index_page.check_my_username()
        my_deposit = index_page.check_my_deposit()

        index_page.check_all_panel_left_no_shop()
        index_page.check_all_product_listed()

        # user_profile = UserInfo(my_deposit)
        #
        # user_profile.getUsername(my_username)
        # user_profile.getDeposit()
