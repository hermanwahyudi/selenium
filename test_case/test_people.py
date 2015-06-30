from main.activity.activity_login import *
from main.page.people.pe_people import *
from main.page.setting.pe_user import *
from main.page.setting.pe_user_notif import *
from selenium import webdriver
import time
import unittest

class TestEditPeople(unittest.TestCase):

    _site = "live"

    # dictionary user
    dict_user = {
        "email_buyer" : "tkpd.qc+35@gmail.com",
        "password_buyer" : "8delapan",
        "email_seller" : "tkpd.qc+36@gmail.com",
        "password_seller" : "8delapan"
    }

    def setUp(self):
        # self.driver = webdriver.Chrome("C:\driver\chromedriver")
        self.driver = webdriver.Firefox() 
        self.peoplePage = peoplePage(self.driver)                     #Set Firefoxdriver
        self.driver.implicitly_wait(10)
        self.login = LoginPage(self.driver)
        self.header = HeaderPage(self.driver)
        self.tabulasi = UserSetting(self.driver)
        self.ceklist= UserNotif(self.driver)

    def test_1_edit_tab_1_personal_profile(self):
        print ("TEST #1 : Halaman People")
        driver = self.driver
        self.login.open(self._site)
        self.login.do_login(self.dict_user['email_buyer'], self.dict_user['password_buyer'])
        self.header.mouse_hover_to_user_bar()
        self.header.mouse_hover_to_setting()
        self.tabulasi.goto_notif_tab()
        self.ceklist.set_notification()
        time.sleep(2)

        ####### comment dan uncomment untuk mengganti-ganti test case di bawah ini #######
        #self.peoplePage.edit_personal_profile()
        #self.peoplePage.edit_photo()
        # self.peoplePage.edit_password()
        # self.peoplePage.action_address("add", 2)
        # self.peoplePage.action_address("edit", 2)
        # self.peoplePage.action_address("delete", 2)
        # self.peoplePage.action_address("default", 2)
        # self.peoplePage.search_address()
        # self.peoplePage.choose_sorting()
        # self.peoplePage.action_bank_account("add", 2)
        # self.peoplePage.action_bank_account("edit", 2)
        # self.peoplePage.action_bank_account("delete", 2)
        # self.peoplePage.action_bank_account("default", 2)
        # self.peoplePage.set_notification()
        # self.peoplePage.set_privacy_settings()
        
        time.sleep(5)

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()