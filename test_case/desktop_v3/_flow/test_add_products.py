from utils.function.setup import *
from utils.lib.user_data import *
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_logout import *
from main.activity.desktop_v3.activity_add_products import *
import unittest

class TestAddProduct(unittest.TestCase):
    #Instance
    _site = "live"

    #dictionary product
    dict_product = {
        #WARNING!! Dollar currency just available for gold merchant
        'repeat': "1",
        'min_order': "2",
        'currency': "rupiah",                       #rupiah [OR] dollar
        'price': "3500000",
        'unit': "gr",                                       #gr [OR] kg
        'weight': "250",
        'picture': "yes",                                  #yes [OR] no
        'insurance': "yes",                                #yes [OR] no
        'add_to': "etalase",                    #etalase [OR] warehouse
        'condition': "used",                             #new [OR] used
        'description': "produk ini tuhh"
    }

    def setUp(self):
        test_driver = ""
        self.driver = tsetup("firefox")
        self.flag = 0

    def test_add_product_only(self):
        print("> ::TEST ADD PRODUCT ONLY::")
        print("===========================")
        driver = self.driver
        self.user= user10

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        addingProduct = addProductActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        addingProduct.add_product_only(driver, int(self.dict_product['repeat']), int(self.dict_product['min_order']), self.dict_product['currency'], int(self.dict_product['price']), self.dict_product['unit'], int(self.dict_product['weight']), self.dict_product['picture'], self.dict_product['add_to'], self.dict_product['insurance'], self.dict_product['condition'], self.dict_product['description'])
        logoutValidate.do_logout(driver, self._site)

    def test_add_product_catalog(self):
        print("> ::TEST ADD PRODUCT CATALOG::")
        print("==============================")
        driver = self.driver
        self.user= user10

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        addingProduct = addProductActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        addingProduct.add_product_catalog(driver, int(self.dict_product['repeat']), int(self.dict_product['min_order']), self.dict_product['currency'], int(self.dict_product['price']), self.dict_product['unit'], int(self.dict_product['weight']), self.dict_product['picture'], self.dict_product['add_to'], self.dict_product['insurance'], self.dict_product['condition'], self.dict_product['description'])
        logoutValidate.do_logout(driver, self._site)

    def tearDown(self):
        print("> ::Testing has done, the browser window will be closed soon::")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')