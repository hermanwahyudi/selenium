#!/usr/bin/env python

import unittest
from main.activity.activity_login import *
from main.activity.activity_logout import *
from main.activity.activity_myshop_editor import *
from main.lib.user_data import *
from main.function.setup import *


class Test_add_etalase(unittest.TestCase):

    _site = "live"


    def setUp(self):
        print ('[VALIDATION TEST] "Myshop-Etalase"')
        self.driver = tsetup("firefox")

    def test_1_check_add_and_edit_etalase(self):
        print ("TEST #1 : [Validation] Add and Edit Etalase using Unknown Character")
        driver = self.driver

        email = user2['email']
        pwd = user2['pwd']

        #Object activity
        login = loginActivity()
        myshop_etalase = myshopEditorActivity()
        logout = logoutActivity()

        #Object initiation
        myshop_etalase.setObject(driver)


        #Action
        login.do_login(driver, email, pwd, self._site)

        myshop_etalase.goto_myshop_editor(self._site)
        myshop_etalase.click_tab_etalase(self.driver)
        myshop_etalase.add_then_edit_etalase(self.driver)
        #self.etalse.do_validation()
        logout.do_logout(driver,self._site)

    def test_2_check_act_n_times(self):
        #test_user_login(self.driver, self.dict_user['email'], self.dict_user['password'], self._site)

        print ("TEST #2 : [Validation] Act N-times ")
        driver = self.driver

        email = user2['email']
        pwd = user2['pwd']

        #Object activity
        login = loginActivity()
        myshop_etalase = myshopEditorActivity()
        logout = logoutActivity()

        #Object initiation
        myshop_etalase.setObject(driver)

         #Action
        login.do_login(driver, email, pwd, self._site)

        myshop_etalase.goto_myshop_editor(self._site)
        myshop_etalase.click_tab_etalase(self.driver)
        #
        print ("==========")
        print ("Act - Edit")
        print ("==========")
        myshop_etalase.act_n_times(self.driver, "edit", 15)
        #self.etalse.do_validation()
        logout.do_logout(driver,self._site)



    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        time.sleep(3)
        self.driver.close()

# main

if __name__ == "__main__":
    unittest.main(warnings='ignore')
