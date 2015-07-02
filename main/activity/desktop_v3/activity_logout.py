from main.page.desktop_v3.login.pe_logout import *


class logoutActivity():
    def do_logout(self, driver, site):
        logout_page = LogoutPage(driver)

        logout_page.check_current_url()
        logout_page.open(site)

