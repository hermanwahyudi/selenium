import os,sys, time

from main.page.base import BasePage
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class RegisterPage(BasePage):

    _pl = "register.pl"

    #url = "https://www.tokopedia.com/register.pl"

    #Locators
    _full_name_loc = (By.ID, 'full-name')
    _phone_loc = (By.ID, 'phone')
    _gender_male_loc = (By.ID, 'gender-male')
    _gender_female_loc = (By.ID, 'gender-female')
    _birthdate_day_loc = (By.CSS_SELECTOR, 'div.controls-date-field a.tanggal span.selectBox-label')
    _birthdate_day_filter_loc = (By.XPATH, '/html/body/ul[1]/li[4]/a')
    _birthdate_month_loc = (By.CSS_SELECTOR, 'div.controls-date-field a.bulan span.selectBox-label')
    _birhtdate_month_filter_loc = (By.XPATH, '/html/body/ul[2]/li[9]/a')
    _birthdate_year_loc = (By.CSS_SELECTOR, 'div.controls-date-field a.tahun span.selectBox-label')
    _birthdate_year_filter_loc = (By.XPATH, '/html/body/ul[3]/li[18]/a')

    #test
    _yy1 = (By.XPATH, '/html/body/ul[3]/li/a')

    _email_loc = (By.ID, 'email')
    _pwd_loc = (By.ID, 'password')
    _conf_pwd_loc = (By.ID, 'confirm-password')
    _check_tos = (By.CSS_SELECTOR, 'div.control-group label.checkbox input.register_tos')
    _submit_loc = (By.CSS_SELECTOR, 'div.span6 button.btn-action')
    _register_via_fb = (By.CSS_SELECTOR, 'div.span6 div.mt-40 button.btn-facebook')
    _register_via_google = (By.CSS_SELECTOR, 'div.span6 div.mt-40 button.btn-buy')

    #Actions
    #def open(self):
    #    self._open(self.url)

    def open(self, site, pl=""):
        self._open(site, self._pl)

    def input_full_name(self, full_name):
        self.find_element(*self._full_name_loc).send_keys(full_name)

    def input_phone_number(self, phone_number):
        self.find_element(*self._phone_loc).send_keys(phone_number)

    def choose_gender(self, gender):
        if gender == "Pria" or gender == "Male":
            self.find_element(*self._gender_male_loc).click()
        elif gender == "Wanita" or gender == "Female":
            self.find_element(*self._gender_female_loc).click()
        else:
            print ("Jenis Kelamin '%s' tidak sesuai"  %gender)

    def choose_birth_day(self, driver):
        try:
            WebDriverWait(driver, 15).until(EC.presence_of_element_located(self._birthdate_day_loc))
            self.find_element(*self._birthdate_day_loc).click()
            self.find_element(*self._birthdate_day_filter_loc).click()
            print(self.find_element(*self._birthdate_day_filter_loc))
        except NoSuchElementException:
            print ("Birth-day Element not found")


    def choose_birth_month(self, driver):
        try:
            WebDriverWait(driver, 15).until(EC.presence_of_element_located(self._birthdate_month_loc))
            self.find_element(*self._birthdate_month_loc).click()
            self.find_element(*self._birhtdate_month_filter_loc).click()
        except NoSuchElementException:
            print ("Birth-month Element not found")

    def choose_birth_year(self, driver): #masih ngebug di phantom js
        try:
            print("   cari elemen")
            WebDriverWait(driver, 15).until(EC.presence_of_element_located(self._birthdate_year_loc))
            print("   klik dropdown tahun")
            self.find_element(*self._birthdate_year_loc).click()
            print("   list tahun")
            #self.driver.execute_script("document.querySelector('div.controls-date-field a.tahun span.selectBox-label').style.display = '';")
            #self.find_element(*self._birthdate_year_filter_loc).click()
            list_tahun = self.find_elements(*self._yy1)
            """for i in list_tahun:
                print (i)"""
            print("   pilih tahun dan klik")
            list_tahun[randint(1, len(list_tahun)-1)].click()
            time.sleep(1)
            print("   selesai")
        except NoSuchElementException:
            print ("Birth-year Element not found")

    def input_email(self, email):
        self.find_element(*self._email_loc).send_keys(email)

    def input_password(self, pwd):
        self.find_element(*self._pwd_loc).send_keys(pwd)

    def input_confirm_password(self, conf_pwd):
        self.find_element(*self._conf_pwd_loc).send_keys(conf_pwd)

    def check_tos(self, select_check_tos):
        if select_check_tos == 'yes':
            self.find_element(*self._check_tos).click()
        else:
            pass

    def submit(self):
        self.find_element(*self._submit_loc).click()

    #added by mir
    def register_via_facebook(self):
        self.find_element(*self._register_via_fb).click()

    def register_via_google(self):
        self.find_element(*self._register_via_google).click()
        
    #end of funct by mir
