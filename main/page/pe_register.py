import os,sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))
from base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class RegisterPage(BasePage):
    url = "https://www.tokopedia.com/register.pl"

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
    _birthdate_year_filter_loc = (By.XPATH, '/html/body/ul[3]/li[8]/a')
    _email_loc = (By.ID, 'email')
    _pwd_loc = (By.ID, 'password')
    _conf_pwd_loc = (By.ID, 'confirm-password')
    _check_tos = (By.CSS_SELECTOR, 'div.control-group label.checkbox input.register_tos')
    _submit_loc = (By.CSS_SELECTOR, 'div.span6 button.btn-action')

    #Actions
    def open(self):
        self._open(self.url)

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
        except NoSuchElementException:
            print ("Birth-day Element not found")


    def choose_birth_month(self, driver):
        try:
            WebDriverWait(driver, 15).until(EC.presence_of_element_located(self._birthdate_month_loc))
            self.find_element(*self._birthdate_month_loc).click()
            self.find_element(*self._birhtdate_month_filter_loc).click()
        except NoSuchElementException:
            print ("Birth-month Element not found")

    def choose_birth_year(self, driver):
        try:
            WebDriverWait(driver, 15).until(EC.presence_of_element_located(self._birthdate_year_loc))
            self.find_element(*self._birthdate_year_loc).click()
            self.find_element(*self._birthdate_year_filter_loc).click()
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


def test_do_register(driver, f_name, phone, gender_type, email_addr, password, conf_password, select_check_tos):
    register_page=RegisterPage(driver)

    register_page.open()
    register_page.input_full_name(f_name)
    register_page.input_phone_number(phone)
    register_page.choose_gender(gender_type)
    register_page.choose_birth_day(driver)
    register_page.choose_birth_month(driver) #<--belum selesai function nya, samakan dengan choose_birth_day
    register_page.choose_birth_year(driver)
    register_page.input_email(email_addr)
    register_page.input_password(password)
    register_page.input_confirm_password(conf_password)
    register_page.check_tos(select_check_tos)
    register_page.submit()



