from main.activity.activity_login import *
from main.activity.activity_logout import *
from main.activity.activity_myshop_editor import *
from main.lib.user_data import *
from main.function.setup import *
import unittest

class TestEditMyshopInfo(unittest.TestCase):

    _site = "live"

    def setUp(self):
        print ('TEST "Myshop-Editor"')
        self.driver = tsetup()

    def test_1_edit_shop_info(self):
        print ("TEST #1 : Edit Shop Information")
        print ("============================")
        driver = self.driver

        email = user1['email']
        pwd = user1['pwd']

        login = loginActivity()
        myshopEdit = myshopEditorActivity()
        logout = logoutActivity()

        login.do_login(driver, email, pwd, self._site)

        myshopEdit.setObject(driver)
        myshopEdit.goto_myshop_editor(self._site)
        myshopEdit.edit_slogan_shop()
        myshopEdit.edit_shop_description()
        myshopEdit.change_shop_status_to("close")
        time.sleep(3)

        myshopEdit.do_save_changes()
        time.sleep(2)

        logout.do_logout(driver, self._site)




    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        self.driver.close()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
