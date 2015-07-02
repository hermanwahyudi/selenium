from main.page.base import BasePage
from selenium.webdriver.common.by import By
import os,sys, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class ForgotPassword(BasePage):
    #locator path
    _pl = "reset.pl"

    _form_input_email = (By.XPATH, "/html/body/div[1]/section/div/div/form/div[3]/div/input")
    _button_submit = (By.XPATH, ".//*[@id='submit']")
    _err1 = (By.XPATH, ".//*[@id='register-form']/div[2]/ul/li")
    _emailspan = (By.XPATH, ".//*[@id='register-form']/div/p[1]/strong")

    def open (self, site, pl=""):
        self._open(site, self._pl)

    def ActionSendP(self, driver, input_email):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(self._form_input_email))
            self.find_element(*self._form_input_email).send_keys(input_email)
            self.find_element(*self._button_submit).click()

            try:
                self.check_visible_element(*self._err1)
                err_1 = self.find_element(*self._err1)
                if err_1.is_displayed():

                    if err_1.text == "Alamat Email harus diisi." or err_1.text == "Email Address must be filled.":
                        print("Email Address must be filled")
                    else:
                        print("Email Address is not valid. Please correct your entries")


            except:
                e1 = self.find_element(*self._emailspan)
                if e1.is_displayed():
                    print("Your Password Will Be Reset")
                    print("Your email address is : "+ e1.text + ". Please check it")


        except Exception as inst:
            print (inst)

