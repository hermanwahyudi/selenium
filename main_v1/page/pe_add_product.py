from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import os, time, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from base import BasePage


class addProduct(BasePage):

    url = "https://www.tokopedia.com/product-add.pl"

    #locators
    _pname_loc = (By.ID, 'p-name')
    _pdep1_loc = (By.ID, 'p-dep-1')
    _pdep2_loc = (By.ID, 'p-dep-2')
    _pdep3_loc = (By.ID, 'p-dep-3')
    _pminorder_loc = (By.ID, 'p-min-order')
    _pprice_loc = (By.ID, 'p-price')
    _pweight_loc = (By.ID, 'p-weight')
    _puploadto_loc = (By.ID, 'p-upload-to')
    _mustinsurance_loc = (By.ID, 'must_insurance')
    _pcondition_loc = (By.ID, 'p-condition')
    _returnable_loc = (By.ID, 'returnable')
    _pdescription_loc = (By.ID, 'p-description')
    _submit_loc = (By.ID, 's-save-prod')


    # dictionary
    dict = {
        "index_url" : "http://www.tokopedia.com/",
        "email" : "tkpd.qc+18@gmail.com",
        "password" : "imtokopedia91"
    }

    
    def open(self, url):
        self.driver.get(url)
        time.sleep(2)

    def go_to_add_product(self):
        self.open(self.dict['index_url'] + 'product-add.pl')
    
    def add_to_product(self):
        self.go_to_add_product()
        try:
            self.driver.find_element(By.ID, "p-name").send_keys("Product AB")
            time.sleep(4)
            self.choose_category()
            self.driver.find_element(By.ID, "p-min-order").clear()
            self.driver.find_element(By.ID, "p-min-order").send_keys(randint(1, 5))
            self.driver.find_element(By.ID, "p-price").send_keys(randint(5000, 10000))
            self.driver.find_element(By.ID, "p-weight").send_keys(randint(100, 250))
            self.choose_upload_to()
            self.driver.find_element(By.ID, "s-save-prod").submit()
        except Exception as inst:
            print(inst)
        
    def choose_category(self):
        try:
            time.sleep(6)
            self.driver.execute_script("document.getElementById('p-dep-1').style.display = '';")
            time.sleep(6)
            list_category_first = self.driver.find_elements(By.XPATH, "//select[@id='p-dep-1']/option")
            i = 0
            while i < len(list_category_first):
                if i == randint(0, len(list_category_first)-1):
                    list_category_first[i].click()
                    break
                i += 1
            time.sleep(6)
            self.driver.execute_script("document.getElementById('p-dep-2').style.display = '';")
            time.sleep(6)
            list_category_second = self.driver.find_elements(By.XPATH, "//select[@id='p-dep-2']/option")
            i = 0
            while i < len(list_category_second):
                if i == randint(0, len(list_category_second)-1):
                    list_category_second[i].click()
                    break
                i += 1
            time.sleep(6)
            self.driver.execute_script("document.getElementById('p-dep-3').style.display = '';")
            time.sleep(6)
            list_category_third = self.driver.find_elements(By.XPATH, "//select[@id='p-dep-3']/option")
            i = 0   
            while i < len(list_category_third):
                if i == randint(0, len(list_category_third)-1):
                    list_category_third[i].click()
                    break
                i += 1
        except Exception as inst:
            print(inst)

    def choose_upload_to(self):
        try:
            time.sleep(6)
            self.driver.execute_script("document.getElementById('p-upload-to').style.display = '';")
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.ID,'p-upload-to')))
            time.sleep(6)
            list_upload_to = self.driver.find_elements(By.XPATH, "//select[@id='p-upload-to']/option")
            list_upload_to[0].click()

            time.sleep(6)
            self.driver.execute_script("document.getElementById('p-menu-id').style.display = '';")
            time.sleep(6)
            list_etalase = self.driver.find_elements(By.XPATH, "//select[@id='p-menu-id']/option")
            i = 0
            while i < len(list_etalase):
                if i == randint(0, len(list_etalase)-1):
                    list_etalase[i].click()
                    break
                i += 1
        except Exception as inst:
            print(inst)