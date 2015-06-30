from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import os, time, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from main.page.base import BasePage
import subprocess


class addProduct(BasePage):

    #locators
    _pname_loc = (By.ID, 'p-name')
    _pdep1_loc = (By.ID, 'p-dep-1')
    _pdep2_loc = (By.ID, 'p-dep-2')
    _pdep3_loc = (By.ID, 'p-dep-3')
    _pminorder_loc = (By.ID, 'p-min-order')
    _pprice_loc = (By.ID, 'p-price')
    _pweight_loc = (By.ID, 'p-weight')
    _upload_image_loc = (By.ID, 'pickfiles')
    _puploadto_loc = (By.ID, 'p-upload-to')
    _mustinsurance_loc = (By.ID, 'must_insurance')
    _pcondition_loc = (By.ID, 'p-condition')
    _returnable_loc = (By.ID, 'returnable')
    _pdescription_loc = (By.ID, 'p-description')
    _submit_loc = (By.ID, 's-save-prod')

    _catalog_loc = (By.CSS_SELECTOR, "a.catalog-select")

    # current page
    _pl = 'product-add.pl'
    #--

    def open(self, site=""):
        self._open(site, self._pl)
    
    def add_to_product(self, i, _site):
        try:
            self.driver.find_element(*self._pname_loc).send_keys('Product Otomatis ke ' + str(i)) 
            self.choose_category_1()
            self.choose_category_2()
            self.choose_category_3()
            self.driver.find_element(*self._pminorder_loc).clear()
            self.driver.find_element(*self._pminorder_loc).send_keys(randint(1, 5))
            self.driver.find_element(*self._pprice_loc).send_keys(randint(5000, 10000))
            self.driver.find_element(*self._pweight_loc).send_keys(randint(100, 250))
            self.driver.find_element(*self._upload_image_loc).click()
            time.sleep(2)
            subprocess.Popen(r"C:\autoit\upload-image.exe")
            time.sleep(2)
            self.choose_upload_to()
            time.sleep(3)
            self.choose_etalase()
            self.driver.find_element(*self._submit_loc).submit()
            time.sleep(5)
            print("SUKSES")
            self._open(_site, self._pl)
        except Exception as inst:
            print(inst)

    def add_to_product_catalog(self, i, _site):
        try:
            self.driver.find_element(*self._pname_loc).send_keys('Samsung B221' + str(i)) 
            self.choose_category_1_catalog()
            self.choose_category_2_catalog()
            self.driver.find_element(*self._catalog_loc).click()
            self.driver.find_element(*self._pminorder_loc).clear()
            self.driver.find_element(*self._pminorder_loc).send_keys(randint(1, 5))
            self.driver.find_element(*self._pprice_loc).send_keys(randint(5000, 10000))
            self.driver.find_element(*self._pweight_loc).send_keys(randint(100, 250))
            self.driver.find_element(*self._upload_image_loc).click()
            time.sleep(2)
            subprocess.Popen(r"C:\autoit\upload-image.exe")
            time.sleep(2)
            self.choose_upload_to()
            time.sleep(3)
            self.choose_etalase()
            self.driver.find_element(*self._submit_loc).submit()
            time.sleep(5)
            print("SUKSES")
            self._open(_site, self._pl)
        except Exception as inst:
            print(inst)

    def action_add_product(self, N, _site):
        try:
            print("Action Add Product" + " " + str(N) + " kali.")
            i = 1
            while(i <= N):
                print("================ Add Product Ke " + str(i) + " ================")
                self.add_to_product(i, _site)
                i += 1
        except Exception as inst:
            print(inst)

    def action_add_product_catalog(self, N, _site):
        try:
            print("Action Add Product ke dalam Katalog " + " " + str(N) + " kali.")
            i = 1
            while(i <= N):
                print("================ Add Product Katalog Ke " + str(i) + " ================")
                self.add_to_product_catalog(i, _site)
                i += 1
        except Exception as inst:
            print(inst)
        
    def choose_category_1(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.querySelector('div#slct-p-dep-1 select#p-dep-1').style.display = '';")
            self.driver.execute_script("document.querySelector('div#slct-p-dep-1 a.selectBox').style.display = 'none';")
            list_category_first = self.driver.find_elements(By.XPATH, "//select[@id='p-dep-1']/option")
            i = randint(1, len(list_category_first)-1)
            list_category_first[i].click()
        except Exception as inst:
            print(inst)

    def choose_category_2(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.querySelector('div#slct-p-dep-2 select#p-dep-2').style.display = '';")
            self.driver.execute_script("document.querySelector('div#slct-p-dep-2 a.selectBox').style.display = 'none';")
            list_category_second = self.driver.find_elements(By.XPATH, "//select[@id='p-dep-2']/option")
            i = randint(1, len(list_category_second)-1)
            list_category_second[i].click()
        except Exception as inst:
            print(inst)

    def choose_category_3(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.querySelector('div#slct-p-dep-3 select#p-dep-3').style.display = '';")
            self.driver.execute_script("document.querySelector('div#slct-p-dep-3 a.selectBox').style.display = 'none';")
            list_category_third = self.driver.find_elements(By.XPATH, "//select[@id='p-dep-3']/option")
            i = randint(1, len(list_category_third)-1)
            list_category_third[i].click()
        except Exception as inst:
            print(inst)

    def choose_category_1_catalog(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.querySelector('div#slct-p-dep-1 select#p-dep-1').style.display = '';")
            self.driver.execute_script("document.querySelector('div#slct-p-dep-1 a.selectBox').style.display = 'none';")
            self.driver.find_element(By.XPATH, "//select[@id='p-dep-1']/option[9]").click()
        except Exception as inst:
            print(inst)

    def choose_category_2_catalog(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.querySelector('div#slct-p-dep-2 select#p-dep-2').style.display = '';")
            self.driver.execute_script("document.querySelector('div#slct-p-dep-2 a.selectBox').style.display = 'none';")
            self.driver.find_element(By.XPATH, "//select[@id='p-dep-2']/option[2]").click()
        except Exception as inst:
            print(inst)

    def choose_upload_to(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.getElementById('p-upload-to').style.display = '';")
            list_upload_to = self.driver.find_elements(By.XPATH, "//select[@id='p-upload-to']/option")
            list_upload_to[0].click()
        except Exception as inst:
            print(inst)

    def choose_etalase(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.getElementById('p-menu-id').style.display = '';")
            list_etalase = self.driver.find_elements(By.XPATH, "//select[@id='p-menu-id']/option")
            list_etalase[1].click()
        except Exception as inst:
            print(inst)