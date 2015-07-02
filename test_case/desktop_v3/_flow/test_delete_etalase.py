
import unittest, random, string
from main.activity.activity_login import *
from main.activity.activity_logout import *
from main.activity.activity_myshop_editor import *
from main.lib.user_data import *
from main.function.setup import *

class Test_add_etalase(unittest.TestCase):

    _site = "live"


    def setUp(self):
        print ('TEST "Add-Etalase"')
        self.driver = tsetup("firefox")


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