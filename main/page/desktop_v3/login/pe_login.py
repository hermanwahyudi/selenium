import time,os,sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from main.page.base import BasePage
from selenium.webdriver.common.by import By


list_login_validation = {
    'v_email'       : "Email harus diisi.",
    'v_password'    : "Kata Sandi harus diisi.",
    'v_invalid'     : "Email / Password yang anda masukkan salah. Pastikan caps lock dalam keadaan mati.",
    'v_limit'       : "Anda gagal login beberapa kali. Silahkan menunggu beberapa saat untuk login kembali."
}

class LoginPage(BasePage):

    _pl = "login.pl"
    #locators
    _email_loc = (By.ID, 'inputEmail')
    _pwd_loc = (By.ID, 'inputPassword')
    _submit_loc = (By.CLASS_NAME, 'btn-action')

    #Property
    def user_status(self, status):
        status = 0

    #Actions
    def open(self, site=""):
        selected_env = self._open(site, self._pl)
        return selected_env

    def input_email(self, email):
        self.check_visible_element(*self._email_loc)
        self.find_element(*self._email_loc).send_keys(email)

    def input_pwd(self, pwd):
        self.check_visible_element(*self._pwd_loc)
        self.find_element(*self._pwd_loc).send_keys(pwd)

    def submit(self):
        self.check_visible_element(*self._submit_loc)
        self.find_element(*self._submit_loc).click()

    def do_login(self, email, pwd):
        try:
            time.sleep(1)
            self.input_email(email)
            self.input_pwd(pwd)
            self.submit()
        except Exception as inst:
            print(inst)


