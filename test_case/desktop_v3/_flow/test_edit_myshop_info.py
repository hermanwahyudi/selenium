from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_logout import *
from main.activity.desktop_v3.activity_myshop_editor import *
from utils.lib.user_data import *
from utils.function.setup import *
import unittest

class TestEditMyshopInfo(unittest.TestCase):

    _site = "live"

    def setUp(self):
        print ('TEST "Myshop-Editor"')
        self.driver = tsetup("firefox")
        self.user = user1

    def test_1_edit_shop_info(self):
        print ("TEST #1 : Edit Shop Information")
        print ("============================")
        driver = self.driver

        email = self.user['email']
        pwd = self.user['pwd']

        login = loginActivity()
        myshopEdit = myshopEditorActivity()
        logout = logoutActivity()

        login.do_login(driver, self.user, email, pwd, self._site)

        myshopEdit.setObject(driver)
        myshopEdit.goto_myshop_editor(self._site)
        myshopEdit.edit_slogan_shop()
        myshopEdit.edit_shop_description()
        myshopEdit.change_shop_status_to("close")
        time.sleep(3)

        myshopEdit.do_save_changes()
        time.sleep(4)

        logout.do_logout(driver, self._site)


    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        self.driver.close()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
