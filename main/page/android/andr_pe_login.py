__author__ = 'QC1'

from appium import webdriver
from main.page.android.andr_base import *

class PageLogin(PageBaseMobile):

    loc_widget_email = ("//android.widget.EditText[@resource-id='com.tokopedia.tkpd:id/email_auto']")
    loc_widget_password = "//android.widget.EditText[@resource-id='com.tokopedia.tkpd:id/password']"

    id_widget_signIn = 'com.tokopedia.tkpd:id/sign_in_button'
    id_widget_facebookLogIn = 'com.tokopedia.tkpd:id/facebook_login'
    id_widget_googleLogIn = 'com.tokopedia.tkpd:id/gplus_login'
    id_button_register = 'com.tokopedia.tkpd:id/register_button'
    id_button_forgot_pass = 'com.tokopedia.tkpd:id/forgot_pass'


    def input_email(self, email):
        print("Typing email. . .")
        self.explicit_wait(self.loc_widget_email)
        self.driver.find_element_by_xpath(self.loc_widget_email).send_keys(email)
        self.driver.find_element_by_xpath(self.loc_widget_email).click()

    def input_password(self, password):
        print("Typing password. . .")
        self.explicit_wait(self.loc_widget_password)
        self.driver.find_element_by_xpath(self.loc_widget_password).send_keys(password)

    def sign_in(self):
        print("Tapping login button. . .")
        self.driver.find_element_by_id(self.id_widget_signIn).click()

    def check_login_button(self):
        print("Checking validation. . .")
        assert self.driver.find_element_by_id(self.id_widget_signIn)
        print("Log in button found.")
        assert self.driver.find_element_by_id(self.id_widget_facebookLogIn)
        print("Facebook log in button found.")
        assert self.driver.find_element_by_id(self.id_widget_googleLogIn)
        print("Google log in button found.")
        print("Unable to login validation succeeded.")

    def login_validation(self):
        print("Swipe to the right")
        self.swipeRight()
        sleep(2)
        print("Swipe to the right")
        self.swipeRight()
        sleep(2)
        print("Swipe to the right")
        self.swipeRight()
        sleep(2)




