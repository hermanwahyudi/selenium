import os,sys, time
from main.page.register.pe_register import RegisterPage
from main.page.register.pe_facebookapi import FacebookLoginPage
from main.page.register.pe_googleapi import GooglePlusLoginPage
from main.page.register.pe_create_password import CreatePasswordPage
from main.page.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException



#List semua error message yang mungkin muncul di halaman registrasi
error_list = {
    'err_fullname' : "Nama Lengkap harus diisi.",
    'err_phone' : "Nomor HP harus diisi.",
    'err_gender' : "Jenis Kelamin harus dipilih.",
    'err_birthdate' : "Tanggal Lahir tidak benar.",
    'err_email' : "Alamat Email harus diisi.",
    'err_passwd' : "Kata Sandi harus diisi.",
    'err_toc' : "Anda harus menyetujui Syarat dan Ketentuan dari Tokopedia"
}

#akun fb
usr_email = 'testqcmir1@gmail.com'
usr_passwd = 'ukauka'

#akun google (sementara ngasal dulu)
usr_email2 = 'testqcmir2@gmail.com'
usr_passwd2 = 'cumicumi'

#create new password for tokopedia via fb
new_passwd = '12345678'
phone = '081312345678'

class registerActivity():

    _site = "live"

    fb_url = 'https://www.tokopedia.com/facebook_login.pl' #sementara di hardcode dulu, buat ngetes jalan apa engga


    #register normal
    def test_do_register(self, driver, f_name, phone, gender_type, email_addr, password, conf_password, select_check_tos):
        print("TEST #1 : REGISTER NORMAL")
        register_page=RegisterPage(driver)
        print("Masuk halaman register")
        register_page.open(self._site)
        print("Input nama")
        register_page.input_full_name(f_name)
        print("Input nomor HP")
        register_page.input_phone_number(phone)
        print("Pilih gender")
        register_page.choose_gender(gender_type)
        print("Pilih Tanggal Lahir")
        register_page.choose_birth_day(driver)
        print("Pilih Bulan Lahir")
        register_page.choose_birth_month(driver) #<--belum selesai function nya, samakan dengan choose_birth_day
        print("Pilih Tahun Lahir")
        register_page.choose_birth_year(driver) 
        print("Input alamat e-mail")
        register_page.input_email(email_addr)
        print("Input Password")
        register_page.input_password(password)
        print("Input konfirmasi password")
        register_page.input_confirm_password(conf_password)
        print("Menyetujui terms of service")
        register_page.check_tos(select_check_tos)
        print("Klik Submit")
        register_page.submit()
        print("Selesai.")

    #added by mir#

    #action 1 : Input Null
    def check_validasi_input_null(self, driver):
        print ("TEST #2 : REGISTER NULL")
        register_page=RegisterPage(driver)
        register_page.open(self._site)
        register_page.submit()
        print ("Checking validation....")
        assert error_list['err_fullname'] in driver.find_element_by_tag_name("body").text
        print ("Fullname error message validation OK")
        assert error_list['err_phone'] in driver.find_element_by_tag_name("body").text
        print ("Mobile phone error message validation OK")
        assert error_list['err_gender'] in driver.find_element_by_tag_name("body").text
        print ("Gender error message validation OK")
        assert error_list['err_birthdate'] in driver.find_element_by_tag_name("body").text
        print ("Birthdate error message validation OK")
        assert error_list['err_email'] in driver.find_element_by_tag_name("body").text
        print ("E-mail error message validation OK")
        assert error_list['err_passwd'] in driver.find_element_by_tag_name("body").text
        print ("Password error message validation OK")
        assert error_list['err_toc'] in driver.find_element_by_tag_name("body").text
        print ("Terms of Conduct error message validation OK")
        print ("")
        print ("Validation finished.")

    #action 2: Register with Facebook, FB not logged in & not connected to tokopedia
    #FIRST TIME USE ONLY!
    def check_link_register_via_fb(self, driver):
        register_page=RegisterPage(driver)
        register_page.open(self._site)
        print("TEST #3 : REGISTER VIA FB")
        print("Klik tombol 'Masuk dengan Facebook'")
        register_page.register_via_facebook()
        #insert assertion buat halaman login fb
        print("Masuk www.tokopedia.com/facebook_login.pl (redirect ke halaman fb)")
        fb_login = FacebookLoginPage(driver)
        print("input e-mail akun fb")
        fb_login.input_email_or_hp(usr_email)
        time.sleep(1)
        print("input password akun fb")
        fb_login.input_password(usr_passwd)
        time.sleep(1)
        print("Klik tombol login")
        fb_login.login()
        driver.switch_to_alert()
        print('Berhasil masuk dialog box connect apps')
        fb_login.fb_okay(driver)
        print('Berhasil connect app')
        print("Masuk halaman create_password.pl")
        create_password = CreatePasswordPage(driver)
        create_password.input_new_password(driver, new_passwd)
        create_password.confirm_new_password(driver, new_passwd)
        create_password.input_phone_number(driver, phone)
        create_password.check_tos(driver, 'yes')
        create_password.submit(driver)
        print('selesai')

    #action 3: Register with Google+, google not login & not connected to tokopedia
    #FIRST TIME USE ONLY!
    def check_link_register_via_google(self, driver):
        register_page=RegisterPage(driver)
        register_page.open(self._site)
        print ('TEST #4 : REGISTER VIA GOOGLE+')
        register_page.register_via_google()
        print('Masuk halaman konfirmasi utk connect tokopedia & google')
        google_login = GooglePlusLoginPage(driver)
        print("input e-mail akun google")
        google_login.input_email(driver, usr_email2)
        time.sleep(1)
        print("input password akun google")
        google_login.input_password(driver,usr_passwd2)
        time.sleep(1)
        print("Klik tombol login")
        google_login.login(driver)
        #driver.switch_to_alert()
        print('Masuk halaman autentikasi')
        time.sleep(3)
        google_login.click_accept(driver)
        print("Masuk halaman create_password.pl")
        time.sleep(1)
        create_password = CreatePasswordPage(driver)
        create_password.input_new_password(driver, new_passwd)
        create_password.confirm_new_password(driver, new_passwd)
        create_password.choose_birth_day(driver)
        create_password.choose_birth_month(driver)
        create_password.choose_birth_year(driver)
        create_password.input_phone_number(driver, phone)
        create_password.check_tos(driver, 'yes')
        create_password.submit(driver)
        print('Selesai')


