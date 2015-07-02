#!/usr/bin/env python

import unittest, random, string
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_logout import *
from main.activity.desktop_v3.activity_myshop_editor import *
from utils.lib.user_data import *
from utils.function.setup import *


def random_etal_name(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Test_add_etalase(unittest.TestCase):

    _site = "live"


    def setUp(self):
        print ('TEST "Add-Etalase"')
        self.driver = tsetup("firefox")

    def test_1_add_etalase(self):
        print ("TEST #1 : Add  Etalase")
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
        for i in range(15):
            temp = myshop_etalase.add_new_etalase(random_etal_name())
            if temp ==0:
                break

        #self.etalse.do_validation()
        logout.do_logout(driver,self._site)

    def test_2_delete_etalase(self):
        print ("TEST #1 : Delete Etalase[Top]")
        driver = self.driver

        email = 'test.tokopedia+01@gmail.com'
        pwd = 'asdasd789'

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
        myshop_etalase.delete_last_etalase()

        logout.do_logout(driver, self._site)


    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(warnings='ignore')
