import time,os,sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from base import BasePage
from selenium.webdriver.common.by import By


list_login_validation = {
    'v_email'       : "Email harus diisi.",
    'v_password'    : "Kata Sandi harus diisi.",
    'v_invalid'     : "Email / Password yang anda masukkan salah. Pastikan caps lock dalam keadaan mati.",
    'v_limit'       : "Anda gagal login beberapa kali. Silahkan menunggu beberapa saat untuk login kembali."
}

class LoginPage(BasePage):

    url = "https://www.tokopedia.com/login.pl"

    #locators
    _email_loc = (By.ID, 'inputEmail')
    _pwd_loc = (By.ID, 'inputPassword')
    _submit_loc = (By.CLASS_NAME, 'btn-action')

    #Property
    def user_status(self, status):
        status = 0

    #Actions
    def open(self):
        self._open(self.url)

    def input_email(self, email):
        self.find_element(*self._email_loc).send_keys(email)

    def input_pwd(self, pwd):
        self.find_element(*self._pwd_loc).send_keys(pwd)

    def submit(self):
        self.find_element(*self._submit_loc).click()

class LogoutPage(BasePage):

    url= "https://www.tokopedia.com/logout.pl"

    def check_current_url(self):
        #print(self.driver.current_url)
        if self.driver.current_url == 'https://www.tokopedia.com/':
            print("Saat ini berada di %s , dan bersiap Logout.." %self.driver.current_url)
            time.sleep(3)

    def open(self):
        self._open(self.url)


#aksi 1
def test_user_login(driver, email, password):
    h_flag = 0

    login_page = LoginPage(driver)

    login_page.open()
    login_page.input_email(email)
    login_page.input_pwd(password)
    login_page.submit()
    if driver.current_url == 'https://www.tokopedia.com/':
        print ("Login Succeed!")
        h_flag = 1
        return h_flag
    else:
        return h_flag


#aksi 2
def check_validasi_login_input_empty(driver):
    login_page = LoginPage(driver)
    print ("===========================")
    print ("CHECK VALIDATION : Input Null")
    print ("===========================")


    login_page.open()
    login_page.submit()
    print ("Checking Validation... ")
    assert list_login_validation['v_email'] in driver.find_element_by_tag_name("body").text
    print("Validasi Login Email Sukses: " + list_login_validation['v_email'])
    assert list_login_validation['v_password'] in driver.find_element_by_tag_name("body").text
    print("Validasi Login Password Sukses: " + list_login_validation['v_password'])
    assert list_login_validation['v_invalid'] not in driver.find_element_by_tag_name("body").text
    assert list_login_validation['v_limit'] not in driver.find_element_by_tag_name("body").text

#aksi 3
def check_validasi_input_email(driver,email):
    login_page = LoginPage(driver)
    print ("========================")
    print ("CHECK VALIDATION : Input Email Tanpa Password")
    print ("========================")

    login_page.open()
    login_page.input_email(email)
    login_page.submit()
    print ("Melakukan input username : " + email + " tanpa input password")
    print ("Checking Validation...")
    assert list_login_validation['v_email'] not in driver.find_element_by_tag_name("body").text
    assert list_login_validation['v_password'] in driver.find_element_by_tag_name("body").text
    print("Validasi Login Password Sukses: " + list_login_validation['v_password'])
    assert list_login_validation['v_invalid'] not in driver.find_element_by_tag_name("body").text
    assert list_login_validation['v_limit'] not in driver.find_element_by_tag_name("body").text

def check_validasi_input_password(driver,pwd):
    login_page = LoginPage(driver)
    print ("===========================")
    print ("CHECK VALIDASI : Input Password Tanpa Email")
    print ("===========================")

    login_page.open()
    login_page.input_pwd(pwd)
    login_page.submit()
    print ("Melakukan input password tanpa username..")
    print ("Checking Validation...")
    assert list_login_validation['v_email'] in driver.find_element_by_tag_name("body").text
    print("Validasi Login Email Sukses: " + list_login_validation['v_email'])
    assert list_login_validation['v_password'] not in driver.find_element_by_tag_name("body").text
    assert list_login_validation['v_invalid'] not in driver.find_element_by_tag_name("body").text
    assert list_login_validation['v_limit'] not in driver.find_element_by_tag_name("body").text



def test_user_logout(driver):
    logout_page = LogoutPage(driver)

    logout_page.check_current_url()
    logout_page.open()

