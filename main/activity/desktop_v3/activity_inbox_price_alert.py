__author__ = 'QC1'

from main.page.desktop_v3.inbox_price_alert.pe_inbox_price_alert import *
from main.page.desktop_v3.shop.pe_shop import *
from main.page.desktop_v3.product.pe_product import *
from utils.lib.user import *

class PriceAlertActivity():



    def setObject(self, driver):
        self.inbox_price_alert = PriceAlertPage(driver)


    def update_price_alert(self, driver, site, domain):
        shop_page = ShopPage(driver)
        prod = ProductPage(driver)

        print("Heading toward the destination domain at: ", site, domain)
        shop_page.domain(site, domain)
        shop_page.choose_product_manual("Samsung Galaxy S4")
        time.sleep(3)
        i = 0
        while i < 2:
            price = randint(5000999, 5425999)
            print("Price update LOOP #", (i + 1))
            print("Updating price alert to", price)
            prod.price_alert(price)
            i += 1

    def check_inbox_price_alert(self, driver):
        inbox_price_alert_page = PriceAlertPage(driver)

        print("Now heading for Inbox - Price Alert in order to check notification...")
        inbox_price_alert_page.check_price_alert()

    def search_price_alert(self, driver):
        inbox_price_alert_page = PriceAlertPage(driver)

        print("Now heading for Inbox - Price Alert in order to check notification...")
        inbox_price_alert_page.search_inbox_price_alert()
