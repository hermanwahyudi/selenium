import os,sys, time
from random import randint
from selenium import webdriver
from main.page.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CreatePasswordPage(BasePage):
    _pl = 'create-password.pl'

    _new_password_loc = (By.ID, 'new_pass')
    _confirm_new_password_loc = (By.ID, 'confirm_pass')
    _mobile_phone_loc = (By.ID, 'msisdn')
    _check_tos = (By.NAME, 'register_tos')
    _create_passwd_button_loc = (By.CSS_SELECTOR, 'div.span6 button.btn-login-top')
    _birth_day_loc = (By.CSS_SELECTOR,'div.controls-date-field a.tanggal span.selectBox-label')
    _birth_day_choice_loc = (By.XPATH, '/html/body/ul[1]/li/a')
    _birth_month_loc = (By.CSS_SELECTOR, 'div.controls-date-field a.bulan span.selectBox-label')
    _birth_month_choice_loc = (By.XPATH, '/html/body/ul[2]/li/a')
    _birth_year_loc = (By.CSS_SELECTOR, 'div.controls-date-field a.tahun span.selectBox-label')
    _birth_year_choice_loc = (By.XPATH, '/html/body/ul[3]/li/a')

    def open(self, site, pl=""):
        self.open(site, self._pl)

    def input_new_password(self, driver, new_password):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._new_password_loc))
            self.find_element(*self._new_password_loc).send_keys(new_password)
            print('Berhasil input password baru untuk tokopedia')
        except TimeoutException:
            print("Timeout. Elemen tidak ditemukan")

    def confirm_new_password(self, driver, conf_new_password):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._confirm_new_password_loc))
            self.find_element(*self._confirm_new_password_loc).send_keys(conf_new_password)
            print('Berhasil input konfirmasi password baru untuk tokopedia')
        except TimeoutException:
            print('Timeout. Elemen tidak ditemukan')

    def input_phone_number(self, driver, phone):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._mobile_phone_loc))
            self.find_element(*self._mobile_phone_loc).send_keys(phone)
            print('Berhasil input nomor HP')
        except TimeoutException:
            print('Timeout. Elemen tidak ditemukan')

    def choose_birth_day(self, driver):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._birth_day_loc))
            self.find_element(*self._birth_day_loc).click()
            list_tanggal = self.find_elements(*self._birth_day_choice_loc)
            list_tanggal[randint(1, len(list_tanggal)-1)].click()
            time.sleep(1)
            print('Berhasil pilih tanggal')
        except TimeoutException:
            print('Timeout. Elemen Tanggal tidak ditemukan')

    def choose_birth_month(self, driver):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._birth_month_loc))
            self.find_element(*self._birth_month_loc).click()
            list_bulan = self.find_elements(*self._birth_month_choice_loc)
            list_bulan[randint(1, len(list_bulan)-1)].click()
            time.sleep(1)
            print('Berhasil pilih bulan')
        except TimeoutException:
            print('Timeout. Elemen Tanggal tidak ditemukan')

    def choose_birth_year(self, driver):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._birth_year_loc))
            self.find_element(*self._birth_year_loc).click()
            list_tahun = self.find_elements(*self._birth_year_choice_loc)
            list_tahun[randint(1, len(list_tahun)-1)].click()
            time.sleep(1)
            print('Berhasil pilih tahun')
        except TimeoutException:
            print('Timeout. Elemen Tanggal tidak ditemukan')

    def check_tos(self, driver, select_check_tos):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._check_tos))
            if select_check_tos == 'yes':
                self.find_element(*self._check_tos).click()
                print('Check terms of service')
            else:
                pass
        except TimeoutException:
            print('Timeout. Elemen tidak ditemukan.')

    def submit(self, driver):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._create_passwd_button_loc))
            self.find_element(*self._create_passwd_button_loc).click()
            print('Berhasil klik tombol Buat Password')
        except TimeoutException:
            print('Timeout. Elemen tidak ditemukan')