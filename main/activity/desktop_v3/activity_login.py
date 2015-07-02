from main.page.desktop_v3.login.pe_login import *
from main.page.desktop_v3.index.pe_index import *
from main.page.desktop_v3.header import *
from main.page.desktop_v3.secure_interrupt import *
from utils.lib.user import *

class loginActivity():
    # def setObject(self,driver):
    #     self.security_interrupt_page = SecurityInterruptPage(driver)

    #aksi 1

    def do_login(self, driver,user, email, password, site):
        h_flag = 0

        #initiate object
        login_page = LoginPage(driver)
        my_env = Environment()
        my_user = User()
        #--

        security_interrupt_page = SecurityInterruptPage(driver)
        selected_env = login_page.open(site)
        #driver.find_element(By.CSS_SELECTOR, 'form.form-login div.text-center h3.mb-0').send_keys(Keys.ESCAPE)
        print ("environment : %s" %(selected_env))
        login_page.input_email(email)
        login_page.input_pwd(password)
        login_page.submit()
        if driver.current_url == selected_env:
            print ("Success login with %s!" %(email))
            h_flag = 1
            return h_flag
        elif driver.current_url == selected_env + 'interrupt.pl?type=security_check':
            print ("Re-route: Interrupt Page")
            my_user.setDefaultBankAccount(user['default_bank_acc'])
            my_user.setPhone(user['phone'])
            bank_acc = my_user.getDefaultBankAccount()
            phone_numb = my_user.getPhone()
            print (my_user.getDefaultBankAccount())
            print (my_user.getPhone())
            security_interrupt_page.check_security_question(phone_numb, bank_acc)
        else:
            print ("after login -> activity_login.py")
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




