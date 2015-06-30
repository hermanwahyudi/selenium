from random import randint
from main.page.base import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os, time, sys, subprocess
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))


class AddProduct(BasePage):

    #locators of add product
    _prod_name_loc = (By.ID, 'p-name')
    _prod_dep1_loc = (By.ID, 'p-dep-1')
    _prod_dep2_loc = (By.ID, 'p-dep-2')
    _prod_dep3_loc = (By.ID, 'p-dep-3')
    _prod_price_loc = (By.ID, 'p-price')
    _submit_loc = (By.ID, 's-save-prod')
    _prod_weight_loc = (By.ID, 'p-weight')
    _returnable_loc = (By.ID, 'returnable')
    _upload_image_loc = (By.ID, 'pickfiles')
    _prod_condition_loc = (By.ID, 'p-condition')
    _prod_min_order_loc = (By.ID, 'p-min-order')
    _prod_photo_upload_loc = (By.ID, 'p-upload-to')
    _must_insurance_loc = (By.ID, 'must_insurance')
    _prod_description_loc = (By.ID, 'p-description')
    _catalog_loc = (By.CSS_SELECTOR, "a.catalog-select")

    _first_list_category = (By.XPATH, "//select[@id='p-dep-1']/option")
    _second_list_category = (By.XPATH, "//select[@id='p-dep-2']/option")
    _third_list_category = (By.XPATH, "//select[@id='p-dep-3']/option")

    _first_list_category_catalog = (By.XPATH, "//select[@id='p-dep-1']/option[9]")
    _second_list_category_catalog = (By.XPATH, "//select[@id='p-dep-2']/option[2]")

    _list_upload_to = (By.XPATH, "//select[@id='p-upload-to']/option")
    _list_etalase = (By.XPATH, "//select[@id='p-menu-id']/option")

    #site of add product
    _pl = 'product-add.pl'
    #--

    def open(self, site=""):
        self._open(site, self._pl)

    def add_to_product(self, i, _site):
        try:
            self.driver.find_element(*self._prod_name_loc).send_keys('Automated Product - ' + str(i))
            self.choose_category_1()
            self.choose_category_2()
            self.choose_category_3()
            self.driver.find_element(*self._prod_min_order_loc).clear()
            self.driver.find_element(*self._prod_min_order_loc).send_keys(randint(1, 5))
            self.driver.find_element(*self._prod_price_loc).send_keys(randint(5000, 10000))
            self.driver.find_element(*self._prod_weight_loc).send_keys(randint(100, 250))
            self.driver.find_element(*self._upload_image_loc).click()
            time.sleep(2)
            subprocess.Popen(r"C:\autoit\upload-image.exe")
            time.sleep(2)
            self.choose_upload_to()
            time.sleep(3)
            self.choose_etalase()
            self.driver.find_element(*self._submit_loc).submit()
            time.sleep(5)
            print(">> ::Success to add product::")
            self._open(_site, self._pl)
        except Exception as inst:
            print(inst)

    def add_to_product_catalog(self, i, _site):
        try:
            self.driver.find_element(*self._prod_name_loc).send_keys('Samsung Galaxy S4 AUTOMATED' + str(i))
            self.choose_category_1_catalog()
            self.choose_category_2_catalog()
            self.driver.find_element(*self._catalog_loc).click()
            self.driver.find_element(*self._prod_min_order_loc).clear()
            self.driver.find_element(*self._prod_min_order_loc).send_keys(randint(1, 5))
            self.driver.find_element(*self._prod_price_loc).send_keys(randint(5000, 10000))
            self.driver.find_element(*self._prod_weight_loc).send_keys(randint(100, 250))
            self.driver.find_element(*self._upload_image_loc).click()
            time.sleep(2)
            subprocess.Popen(r"C:\autoit\upload-image.exe")
            time.sleep(2)
            self.choose_upload_to()
            time.sleep(3)
            self.choose_etalase()
            self.driver.find_element(*self._submit_loc).submit()
            time.sleep(5)
            print(">> ::Success to add product::")
            self._open(_site, self._pl)
        except Exception as inst:
            print(inst)

    def action_add_product(self, N, _site):
        try:
            print("> ::Action Add Product " + str(N) + " times::")
            i = 1
            while(i <= N):
                print("> ::Add Product - " + str(i) + " ::")
                self.add_to_product(i, _site)
                i += 1
        except Exception as inst:
            print(inst)

    def action_add_product_catalog(self, N, _site):
        try:
            print("> ::Action Add Product to Catalog - " + str(N) + " times::")
            i = 1
            while(i <= N):
                print("> ::Add Product to Catalog - " + str(i) + " ::")
                self.add_to_product_catalog(i, _site)
                i += 1
        except Exception as inst:
            print(inst)

    def choose_category_1(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.querySelector('div#slct-p-dep-1 select#p-dep-1').style.display = '';")
            self.driver.execute_script("document.querySelector('div#slct-p-dep-1 a.selectBox').style.display = 'none';")
            list_category_first = self.driver.find_elements(*self._first_list_category)
            i = randint(1, len(list_category_first)-1)
            list_category_first[i].click()
        except Exception as inst:
            print(inst)

    def choose_category_2(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.querySelector('div#slct-p-dep-2 select#p-dep-2').style.display = '';")
            self.driver.execute_script("document.querySelector('div#slct-p-dep-2 a.selectBox').style.display = 'none';")
            list_category_second = self.driver.find_elements(*self._second_list_category)
            i = randint(1, len(list_category_second)-1)
            list_category_second[i].click()
        except Exception as inst:
            print(inst)

    def choose_category_3(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.querySelector('div#slct-p-dep-3 select#p-dep-3').style.display = '';")
            self.driver.execute_script("document.querySelector('div#slct-p-dep-3 a.selectBox').style.display = 'none';")
            list_category_third = self.driver.find_elements(*self._third_list_category)
            i = randint(1, len(list_category_third)-1)
            list_category_third[i].click()
        except Exception as inst:
            print(inst)

    def choose_category_1_catalog(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.querySelector('div#slct-p-dep-1 select#p-dep-1').style.display = '';")
            self.driver.execute_script("document.querySelector('div#slct-p-dep-1 a.selectBox').style.display = 'none';")
            self.driver.find_element(*self._first_list_category_catalog).click()
        except Exception as inst:
            print(inst)

    def choose_category_2_catalog(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.querySelector('div#slct-p-dep-2 select#p-dep-2').style.display = '';")
            self.driver.execute_script("document.querySelector('div#slct-p-dep-2 a.selectBox').style.display = 'none';")
            self.driver.find_element(*self._second_list_category_catalog).click()
        except Exception as inst:
            print(inst)

    def choose_upload_to(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.getElementById('p-upload-to').style.display = '';")
            list_upload_to = self.driver.find_elements(*self._list_upload_to)
            list_upload_to[0].click()
        except Exception as inst:
            print(inst)

    def choose_etalase(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.getElementById('p-menu-id').style.display = '';")
            list_etalase = self.driver.find_elements(*self._list_etalase)
            list_etalase[1].click()
        except Exception as inst:
            print(inst)