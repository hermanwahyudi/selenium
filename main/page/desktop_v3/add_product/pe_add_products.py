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
    _prod_description_loc = (By.ID, 'p-description')
    _catalog_loc = (By.CSS_SELECTOR, "a.catalog-select")

    _first_list_category = (By.XPATH, "//select[@id='p-dep-1']/option")
    _second_list_category = (By.XPATH, "//select[@id='p-dep-2']/option")
    _third_list_category = (By.XPATH, "//select[@id='p-dep-3']/option")

    _first_list_category_catalog = (By.XPATH, "//select[@id='p-dep-1']/option[9]")
    _second_list_category_catalog = (By.XPATH, "//select[@id='p-dep-2']/option[2]")

    _list_upload_to = (By.XPATH, "//select[@id='p-upload-to']/option")
    _list_etalase = (By.XPATH, "//select[@id='p-menu-id']/option")

    _currency_loc = (By.CSS_SELECTOR, "html.no-js.svg body div#content-container div.container-fluid div.row-fluid div.maincontent-admin div.row-fluid.clear-b form#frm-add-product div#s_form_price.controls.controls-row.mb-20 div.controls div.span10 a.selectBox.select-normal.w-120.ml-0.mr-5.pull-left.selectBox-dropdown span.selectBox-arrow")
    _dollar_loc = (By.XPATH, "/html/body/ul[4]/li[2]/a")

    _open_catalog1_loc = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div/form/div[2]/div[2]/div/div[1]/a")
    _handphonetablet_catalog_loc = (By.XPATH, "/html/body/ul[1]/li[9]/a")
    _open_catalog2_loc = (By.XPATH, "/html/body/div[1]/div[5]/div/div[2]/div/form/div[2]/div[2]/div/div[2]/a")
    _handphone_catalog_loc = (By.CSS_SELECTOR, "html.no-js.svg body ul.selectBox-dropdown-menu.selectBox-options.span12-selectBox-dropdown-menu.select-normal-selectBox-dropdown-menu.ml-0-selectBox-dropdown-menu.selectBox-options-bottom li.opt a")
    _s4_catalog_loc = (By.CSS_SELECTOR, "html.no-js.svg body div#content-container div.container-fluid div.row-fluid div.maincontent-admin div.row-fluid.clear-b form#frm-add-product div#tr-p-catalog.controls.controls-row.mb-20 div.controls div.span10 div.row-fluid div.span12.catalog-view a#ctg-12797.catalog-select")

    _etalase_loc = (By.CSS_SELECTOR, "html.no-js.svg body ul.selectBox-dropdown-menu.selectBox-options.span12-selectBox-dropdown-menu.select-normal-selectBox-dropdown-menu.ml-0-selectBox-dropdown-menu.mb-5-selectBox-dropdown-menu.selectBox-options-bottom li a")
    _warehouse_loc = (By.XPATH, "/html/body/ul[6]/li[2]/a")

    _button_add_to_loc = (By.CSS_SELECTOR, "html.no-js.svg body div#content-container div.container-fluid div.row-fluid div.maincontent-admin div.row-fluid.clear-b form#frm-add-product div.controls.controls-row.mb-15 div.controls div#s-etalase.span10 div.row-fluid a.selectBox.span12.select-normal.ml-0.mb-5.selectBox-dropdown span.selectBox-label")
    _button_add_prod_loc = (By.XPATH, "//*[@id='accordion-shop']/div/ul/li[2]/a")

    def add_to_product(self, i, pro_min_order, currency, pro_price, unit, pro_weight, picture, add_to, insurance, condition, pro_desc):
        try:
            print("> ::Enter add product page::")
            self.driver.find_element(*self._button_add_prod_loc).click()
            print("> ::Fill product name::")
            self.driver.find_element(*self._prod_name_loc).send_keys('Automated Product - ' + str(i))
            print("> ::Choose product category::")
            self.choose_category()
            print("> ::Fill minimum order::")
            self.driver.find_element(*self._prod_min_order_loc).clear()
            self.driver.find_element(*self._prod_min_order_loc).send_keys(pro_min_order)
            if currency == "dollar":
                print("> ::Set the currency::")
                self.set_currency()
            print("> ::Fill product price::")
            self.driver.find_element(*self._prod_price_loc).clear()
            self.driver.find_element(*self._prod_price_loc).send_keys(pro_price)
            if unit == "kg":
                print("> ::Set the unit measure::")
                self.set_unit_measure()
            print("> ::Fill product weight::")
            self.driver.find_element(*self._prod_weight_loc).clear()
            self.driver.find_element(*self._prod_weight_loc).send_keys(pro_weight)
            if insurance == "yes":
                print("> ::Set the product insurance::")
                self.set_insurance()
            print("> ::Choose upload to::")
            self.check_visible_element(By.CSS_SELECTOR, "html.no-js.svg body div#content-container div.container-fluid div.row-fluid div.maincontent-admin div.row-fluid.clear-b form#frm-add-product div.controls.controls-row.mb-15 div.controls div#s-etalase.span10 div.row-fluid a.selectBox.span12.ml-0.mb-5.selectBox-dropdown span.selectBox-arrow")
            if add_to == "etalase":
                print("> ::Choose add to::")
                self.choose_upload_to()
            if condition == "used":
                print("> ::Set the condition::")
                self.set_condition()
            print("> ::Fill product description::")
            self.driver.find_element(*self._prod_description_loc).clear()
            self.driver.find_element(*self._prod_description_loc).send_keys(pro_desc)
            if picture == "yes":
                print("> ::Upload product image::")
                self.driver.find_element(*self._upload_image_loc).click()
                time.sleep(4)
                subprocess.Popen(r"C:\autoit\upload-image.exe")
                time.sleep(2)
            self.driver.find_element(*self._submit_loc).submit()
            time.sleep(2)
        except Exception as inst:
            print(inst)

    def add_to_product_catalog(self, i, pro_min_order, currency,  pro_price, unit, pro_weight, picture, add_to, insurance, condition, pro_desc):
        try:
            print("> ::Enter add product page::")
            self.driver.find_element(*self._button_add_prod_loc).click()
            print("> ::Fill product name::")
            self.driver.find_element(*self._prod_name_loc).send_keys('Samsung Galaxy S4 AUTOMATED ' + str(i))
            print("> ::Choose product category::")
            self.choose_catalog()
            print("> ::Fill minimum order::")
            self.driver.find_element(*self._prod_min_order_loc).clear()
            self.driver.find_element(*self._prod_min_order_loc).send_keys(pro_min_order)
            if currency == "dollar":
                print("> ::Set the currency::")
                self.set_currency()
            print("> ::Fill product price::")
            self.driver.find_element(*self._prod_price_loc).clear()
            self.driver.find_element(*self._prod_price_loc).send_keys(pro_price)
            if unit == "kg":
                print("> ::Set the unit measure::")
                self.set_unit_measure()
            print("> ::Fill product weight::")
            self.driver.find_element(*self._prod_weight_loc).clear()
            self.driver.find_element(*self._prod_weight_loc).send_keys(pro_weight)
            if insurance == "yes":
                print("> ::Set the product insurance::")
                self.set_insurance()
            print("> ::Choose upload to::")
            self.check_visible_element(By.CSS_SELECTOR, "html.no-js.svg body div#content-container div.container-fluid div.row-fluid div.maincontent-admin div.row-fluid.clear-b form#frm-add-product div.controls.controls-row.mb-15 div.controls div#s-etalase.span10 div.row-fluid a.selectBox.span12.ml-0.mb-5.selectBox-dropdown span.selectBox-arrow")
            if add_to == "etalase":
                print("> ::Choose add to::")
                self.choose_upload_to()
            if condition == "used":
                print("> ::Set the condition::")
                self.set_condition()
            print("> ::Fill product description::")
            self.driver.find_element(*self._prod_description_loc).clear()
            self.driver.find_element(*self._prod_description_loc).send_keys(pro_desc)
            if picture == "yes":
                print("> ::Upload product image::")
                self.driver.find_element(*self._upload_image_loc).click()
                time.sleep(4)
                subprocess.Popen(r"C:\autoit\upload-image.exe")
                time.sleep(2)
            self.driver.find_element(*self._submit_loc).submit()
            time.sleep(2)
        except Exception as inst:
            print(inst)

    def set_insurance(self):
        try:
            time.sleep(2)
            self.driver.execute_script("document.getElementById('must_insurance').style.display = '';")
            list_insurance = self.driver.find_elements(By.XPATH, "//select[@id='must_insurance']/option")
            list_insurance[1].click()
        except Exception as inst:
            print(inst)

    def set_condition(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.getElementById('p-condition').style.display = '';")
            time.sleep(1)
            list_condition = self.driver.find_elements(By.XPATH, "//select[@id='p-condition']/option")
            time.sleep(2)
            list_condition[1].click()
        except Exception as inst:
            print(inst)

    def choose_category(self):
        try:
            self.driver.execute_script("document.getElementById('p-dep-1').style.display = '';")
            list_category1 = self.driver.find_elements(By.XPATH, "//select[@id='p-dep-1']/option")
            list_category1[6].click()
            time.sleep(2)
            self.driver.execute_script("document.getElementById('p-dep-2').style.display = '';")
            list_category2 = self.driver.find_elements(By.XPATH, "//select[@id='p-dep-2']/option")
            list_category2[3].click()
            time.sleep(2)
            self.driver.execute_script("document.getElementById('p-dep-3').style.display = '';")
            list_category3 = self.driver.find_elements(By.XPATH, "//select[@id='p-dep-3']/option")
            i = randint(1, len(list_category3)-1)
            list_category3[i].click()
        except Exception as inst:
            print(inst)

    def choose_catalog(self):
        try:
            self.driver.find_element(*self._open_catalog1_loc).click()
            self.driver.find_element(*self._handphonetablet_catalog_loc).click()
            time.sleep(2)
            self.driver.find_element(*self._open_catalog2_loc).click()
            time.sleep(2)
            self.driver.find_element(*self._handphone_catalog_loc).click()
            time.sleep(2)
            self.driver.find_element(*self._s4_catalog_loc).click()
        except Exception as inst:
            print(inst)

    def choose_upload_to(self):
        try:
            self.driver.find_element(*self._button_add_to_loc).click()
            self.driver.find_element(*self._etalase_loc).click()
            print("> ::Choose product etalase::")
            self.choose_etalase()
        except Exception as inst:
            print(inst)

    def choose_etalase(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.getElementById('p-menu-id').style.display = '';")
            time.sleep(1)
            list_etalase = self.driver.find_elements(By.XPATH, "//select[@id='p-menu-id']/option")
            time.sleep(2)
            list_etalase[1].click()
        except Exception as inst:
            print(inst)

    def set_currency(self):
        try:
            self.check_visible_element(By.CSS_SELECTOR, "html.no-js.svg body div#content-container div.container-fluid div.row-fluid div.maincontent-admin div.row-fluid.clear-b form#frm-add-product div#s_form_price.controls.controls-row.mb-20 div.controls div.span10 a.selectBox.select-normal.w-120.ml-0.mr-5.pull-left.selectBox-dropdown span.selectBox-arrow")
            self.driver.find_element(*self._currency_loc).click()
            self.check_visible_element(By.XPATH, "/html/body/ul[4]/li[2]/a")
            self.driver.find_element(*self._dollar_loc).click()
        except Exception as inst:
            print(inst)

    def set_unit_measure(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.getElementById('p-weight-unit').style.display = '';")
            list_unit = self.driver.find_elements(By.XPATH, "//select[@id='p-weight-unit']/option")
            time.sleep(2)
            list_unit[1].click()
        except Exception as inst:
            print(inst)
