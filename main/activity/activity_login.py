from main.page.login.pe_login import *
from main.page.index.pe_index import *
from main.page.header import *
from main.page.base import *


class loginActivity():
    #aksi 1
    def do_login(self, driver, email, password, site):
        h_flag = 0

        login_page = LoginPage(driver)

        login_page.open(site)
        login_page.input_email(email)
        login_page.input_pwd(password)
        login_page.submit()
        if driver.current_url == 'https://www.tokopedia.com/':
            print ("Success login with %s!" %(email))
            h_flag = 1
            return h_flag
        else:
            return h_flag

    #aksi 2
    def check_validasi_login_input_empty(self, driver, site):
        login_page = LoginPage(driver)
        print ("===========================")
        print ("CHECK VALIDATION : Input Null")
        print ("===========================")


        login_page.open(site)
        login_page.submit()
        print ("Checking Validation... ")
        assert list_login_validation['v_email'] in driver.find_element_by_tag_name("body").text
        print("Validasi Login Email Sukses: " + list_login_validation['v_email'])
        assert list_login_validation['v_password'] in driver.find_element_by_tag_name("body").text
        print("Validasi Login Password Sukses: " + list_login_validation['v_password'])
        assert list_login_validation['v_invalid'] not in driver.find_element_by_tag_name("body").text
        assert list_login_validation['v_limit'] not in driver.find_element_by_tag_name("body").text

    #aksi 3
    def check_validasi_input_email(self, driver,email, site):
        login_page = LoginPage(driver)
        print ("========================")
        print ("CHECK VALIDATION : Input Email Tanpa Password")
        print ("========================")

        login_page.open(site)
        login_page.input_email(email)
        login_page.submit()
        print ("Melakukan input username : " + email + " tanpa input password")
        print ("Checking Validation...")
        assert list_login_validation['v_email'] not in driver.find_element_by_tag_name("body").text
        assert list_login_validation['v_password'] in driver.find_element_by_tag_name("body").text
        print("Validasi Login Password Sukses: " + list_login_validation['v_password'])
        assert list_login_validation['v_invalid'] not in driver.find_element_by_tag_name("body").text
        assert list_login_validation['v_limit'] not in driver.find_element_by_tag_name("body").text

    #aksi 4
    def check_validasi_input_password(self, driver, pwd, site):
        login_page = LoginPage(driver)
        print ("===========================")
        print ("CHECK VALIDASI : Input Password Tanpa Email")
        print ("===========================")

        login_page.open(site)
        login_page.input_pwd(pwd)
        login_page.submit()
        print ("Melakukan input password tanpa username..")
        print ("Checking Validation...")
        assert list_login_validation['v_email'] in driver.find_element_by_tag_name("body").text
        print("Validasi Login Email Sukses: " + list_login_validation['v_email'])
        assert list_login_validation['v_password'] not in driver.find_element_by_tag_name("body").text
        assert list_login_validation['v_invalid'] not in driver.find_element_by_tag_name("body").text
        assert list_login_validation['v_limit'] not in driver.find_element_by_tag_name("body").text


class loginActivityAtHeader():
    def doLoginAtIndex(self, driver, site, flag, email, pwd):
        homePage = IndexPage(driver)
        headerPage = HeaderPage(driver)

        homePage.open(site)
        headerPage.check_header_status(flag)
        headerPage.do_login(email,pwd)




