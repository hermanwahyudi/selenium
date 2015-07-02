from main.page.desktop_v3.add_product.pe_add_products import *
from main.page.base import *

#validation dictionary
dict_valid ={
    'success': "Anda berhasil memasukkan produk"
}

class addProductActivity():

    def set_objects(self, driver):
        #Object Activity
        self.addProduct = AddProduct(driver)
        self.openSite = BasePage(driver)
        #--

    def add_product_only(self, driver, i, pro_min_order, currency, pro_price, unit, pro_weight, picture, add_to, insurance, condition, pro_desc):
        self.set_objects(driver)
        self.action_add_product(driver, i, pro_min_order, currency, pro_price, unit, pro_weight, picture, add_to, insurance, condition, pro_desc)

    def add_product_catalog(self, driver, i, pro_min_order, currency, pro_price, unit, pro_weight, picture, add_to, insurance, condition, pro_desc):
        self.set_objects(driver)
        self.action_add_product_catalog(driver, i, pro_min_order, currency, pro_price, unit, pro_weight, picture, add_to, insurance, condition, pro_desc)

    def action_add_product(self, driver, N, pro_min_order, currency, pro_price, unit, pro_weight, picture, add_to, insurance, condition, pro_desc):
        try:
            print("> ::Action Add Product Only - " + str(N) + " times::")
            print("=====================================")
            i = 1
            while(i <= N):
                print("> ::Add Product only - " + str(i) + "::")
                print("==========================")
                self.addProduct.add_to_product(i, pro_min_order, currency, pro_price, unit, pro_weight, picture, add_to, insurance, condition, pro_desc)
                try:
                    assert dict_valid['success'] in driver.find_element_by_tag_name("body").text

                    print("> ::Success to add a new product::")
                except:
                    print("> ::Failed to add a new product::")
                time.sleep(2)
                i += 1
        except Exception as inst:
            print(inst)

    def action_add_product_catalog(self, driver, N, pro_min_order, currency, pro_price, unit, pro_weight, picture, add_to, insurance, condition, pro_desc):
        try:
            print("> ::Action Add Product Catalog - " + str(N) + " times::")
            print("==========================================")
            i = 1
            while(i <= N):
                print("> ::Add Product Catalog - " + str(i) + "::")
                print("==============================")
                self.addProduct.add_to_product_catalog(i, pro_min_order, currency, pro_price, unit, pro_weight, picture, add_to, insurance, condition, pro_desc)
                try:
                    assert dict_valid['success'] in driver.find_element_by_tag_name("body").text
                    print("> ::Success to add a new product::")
                except:
                    print("> ::Failed to add a new product::")
                time.sleep(2)
                i += 1
        except Exception as inst:
            print(inst)