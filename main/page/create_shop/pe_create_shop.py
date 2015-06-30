from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import os, time, sys
from main.page.base import BasePage
from main.page.pe_login import *
from selenium.common.exceptions import WebDriverException,NoSuchElementException, TimeoutException

class createshop(BasePage):
    _in_domain = (By.XPATH, ".//*[@id='domain-checker']/div/div/div[1]/input")
    _butt_submit_dom = (By.XPATH, ".//*[@id='submit']")
    _in_shop_name = (By.XPATH, ".//*[@id='s-info']/div[1]/div[2]/input")
    _in_tagline_shop = (By.XPATH, ".//*[@id='s-info']/div[2]/div[2]/input")
    _in_desc_shop = (By.XPATH, ".//*[@id='s-info']/div[3]/div[2]/textarea[2]")
    _ch_prov_sh = "//select[@id='province']/option"
    _ch_city_sh = "//select[@id='city']/option"
    _ch_district_sh = "//select[@id='district']/option"
    _in_postal_sh = (By.XPATH, ".//*[@id='s-dukungan-kirim']/div/div[2]/input")
    _butt_cs = (By.XPATH, ".//*[@id='side-profile']/div[2]/a")
    _butt_finish = (By.XPATH, ".//*[@id='btn-buka-toko']")
    _err1 = (By.CSS_SELECTOR, ".alert.alert-error")
    _err2 = (By.CSS_SELECTOR, "div.error-div ul.square li")
    _butt_upload_image = (By.XPATH, ".//*[@id='pickfiles_shop']")

        # JNE
    _checkbox_jne_1 = (By.XPATH, ".//*[@id='courier-box']/div[4]/div/div/label/input")
    _checkbox_jne_reg = (By.XPATH, ".//*[@id='chk-courier-1-1']")
    _checkbox_jne_yes = (By.XPATH, ".//*[@id='chk-courier-1-6+']")
    _checkbox_jne_oke = (By.XPATH, ".//*[@id='chk-courier-1-2']")
    _checkbox_jne_oke_min_weight = (By.XPATH, ".//*[@id='oke-min-weight']")
    _input_jne_oke_min_weight = (By.XPATH, ".//*[@id='oke-min-weight-value']")
    _checkbox_jne_oke_shipoutside = (By.XPATH, ".//*[@id='courier-box']/div[7]/div[2]/div/label/input")
    _checkbox_jne_add_fee = (By.XPATH, ".//*[@id='jne-fee-flag']")
    _input_jne_add_fee = (By.XPATH, ".//*[@id='jne-fee-value']")

        # TIKI
    _checkbox_tiki_reg = (By.XPATH, ".//*[@id='chk-courier-2-3']")
    _checkbox_tiki_input_fee = (By.XPATH, ".//*[@id='tiki-fee-flag']")
    _input_tiki_add_fee = (By.XPATH, ".//*[@id='tiki-fee-value']")

        # RPX
    _checkbox_rpx_ndp = (By.XPATH, ".//*[@id='chk-courier-3-4']")
    _checkbox_rpx_ep = (By.XPATH, ".//*[@id='chk-courier-3-5']")

        # WAHANA
    _checkbox_wahana_reg = (By.XPATH, ".//*[@id='chk-courier-6-8']")

        # POS
    _all_elem = {
        '_elem_1_pos' : "/html/body/div[1]/div[5]/div/div[2]/div/div[2]/form/div/div/div[2]/div[6]/div[4]/div/label"

    }
    _all_elem_pisahin_pos_dari_atas ={
        '_checkbox_pos_kilatkhusus' : "//*[@id='chk-courier-4-10']",
        '_checkbox_pos_biasa' : "//*[@id='chk-courier-4-9']",
        '_checkbox_pos_express' : "//*[@id='chk-courier-4-11']",
        '_checkbox_pos_min_weight' : ".//*[@id='pos-min-weight']",
        '_input_pos_min_weight' : "//*[@id='pos-min-weight-value']",
        '_checkbox_pos_add_fee' :  "//*[@id='pos-fee-flag']",
        '_input_pos_add_fee' : "//*[@id='pos-fee-value']"
    }

        #CAHAYA.
    _checkbox_cahaya_reg = (By.XPATH, ".//*[@id='chk-courier-7-12']")

        # PANDU
    _checkbox_pandu_reg = (By.XPATH, ".//*[@id='chk-courier-8-14']")

        # FIRST LOGISTIC
    _checkbox_first_reg = (By.XPATH, ".//*[@id='chk-courier-9-15']")



    domain_shop = ['tokoqc10','tokoqc12','tokoqc100']

    shipping_method = "Jakarta"

    url = "https://www.tokopedia.com/msisdn-verification.pl?action=msisdn-verification"


    def opens(self):

        self.driver.implicitly_wait(2)


    def in_shop_info(self):


        try:
            time.sleep(2)
            element = WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((By.XPATH, ".//*[@id='side-profile']/div[2]/a"))
			)
            print ("This account doesn't have a shop")
            print ("--------------------------------")
            print ("Processing...")
            time.sleep(2)
            element.click()
            time.sleep(5)

            curpage = self.driver.current_url
            if curpage == self.url:
                print("Saat ini berada di halaman dan Mohon verifikasi nomor ponsel Anda dan coba lagi")
                print("Ready to Logout")
                time.sleep(3)
                os._exit(1)
            else:
                self.visible_element_dom_exists()
            #redirect_msisdn_verification_dev.check_current_url(self)
        except Exception as inst:
            print("This account already have a shop")
            print("--------------------------------")
            print("Trying stop process...")
            print("Process successfully stopped")
            print("Status : Terminated")
            sys.exit(None)



    def visible_element_dom_exists(self):


        try:
            length_shop = len(self.domain_shop)
            rand = randint(0, length_shop-1)
            self.driver.find_element(*self._in_domain).send_keys(self.domain_shop[rand])
            self.driver.find_element(*self._butt_submit_dom).click()
            time.sleep(1)


            try:
                self.check_visible_element(*self._err2)
                err2= self.driver.find_element(*self._err2)

                if err2.is_displayed():
                    print ("Domain name is not available")
                    print ("Response: Please change the domain name and try again..")
            except:
                print("Domain name is available")
                self.ch_shipping_agent()
                self.contains_elems()



            self.driver.find_element(*self._in_shop_name).send_keys("Toko QCE")
            self.driver.find_element(*self._in_tagline_shop).send_keys("YEYE TOKO QCE")
            self.driver.find_element(*self._in_desc_shop).send_keys("YUK BELANJA")

        except Exception as inst:
            print(inst)


    def contains_elems(self):
      #for eclem in self._all_elem:
       #   self.check_visible_element(*self._all_elem[eclem])
        #  print ("Element found such as :" + self.find_element(*self._all_elem[eclem]).text)

    # ..
        t = self.driver.find_elements(By.XPATH, self._all_elem['_elem_1_pos'])
        for ec_elem in t:
          print(ec_elem.text)
          return(ec_elem)
        self.contains_2()

    def contains_2(self):
        e = self.driver.find_elements(By.XPATH, self._all_elem_pisahin_pos_dari_atas)
        for i in  e:
          print (i.text)
          return(i)

        #if ec_elem == O:
          #print ("Element found like : " + self.driver.find_elements(ec_elem).)


    def ch_shipping_agent(self):
        try:

            time.sleep(5)

            self.driver.execute_script("document.getElementById('province').style.display = 'block'")
            #self.driver.execute_script("document.getElementsByClassName('selectBox select-normal span4 ml-0 selectBox-dropdown')[0].style.display = 'inline-block'")

            list_loc_prov = self.driver.find_elements(By.XPATH, "//select[@id='province']/option")

            for q in range(len(list_loc_prov)):
                if q == randint(0, len(list_loc_prov)-1):
                    list_loc_prov[q].click()
                    break

            self.driver.execute_script("document.getElementById('city').style.display = 'block'")
            #self.driver.execute_script("document.getElementsByClassName('selectBox select-normal span4 hid-city selectBox-dropdown')[0].style.display = 'inline-block'")
            time.sleep(5)

            list_loc_city = self.driver.find_elements(By.XPATH, "//select[@id='city']/option")

            for q in range(len(list_loc_city)):
                if q == randint(0, len(list_loc_city)-1):
                    list_loc_city[q].click()
                    break

            self.driver.execute_script("document.getElementById('district').style.display = 'block'")
            #self.driver.execute_script("document.getElementsByClassName('selectBox select-normal span4 hid-district selectBox-dropdown')[0].style.display = 'inline-block'")
            time.sleep(5)
            list_loc_district = self.driver.find_elements(By.XPATH, "//select[@id='district']/option")
            time.sleep(5)
            for q in range(len(list_loc_district)):
                if q == randint(0, len(list_loc_district)-1):
                    list_loc_district[q].click()
                    break

            self.postal()

        except Exception as inst:
            print (inst)



    def postal(self):
        self.driver.find_element(*self._in_postal_sh).send_keys("11460")
      # self.finish()

    #def finish(self): // Aktifkan jika ingin bener melakukan create shop
        #self.driver.find_element(*self._butt_finish).click()




