__author__ = 'QC1'

from main.page.android.andr_pe_shop import *
from main.page.android.andr_pe_index import *
import string

def random_etal_name(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class ActivityShop():

    def add_etalase(self, driver,x = 5):
        index_page = PageIndex(driver)
        shop_page = PageShop(driver)

        index_page.tap_etalase()
        for i in range(1, x):
            print("Adding etalase #", i)
            shop_page.add_new_etalase(random_etal_name())

    def delete_etalase(self, driver, x=3):
        index_page = PageIndex(driver)
        shop_page = PageShop(driver)

        index_page.tap_etalase()
        for i in range(1, x):
            print("Deleting etalase #", i)
            shop_page.delete_etalase()

    def add_product(self, driver):
        index_page = PageIndex(driver)
        shop_page = PageShop(driver)

        index_page.tap_add_product()
        shop_page.upload_picture()
        shop_page.insert_product_detail()

