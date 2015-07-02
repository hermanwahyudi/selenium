from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_logout import *
from main.activity.desktop_v3.activity_myshop_editor import *
from utils.lib.user_data import *
from utils.function.setup import *
import unittest

class TestMyshopInfo_Validation(unittest.TestCase):

    _site = "live"

    def setUp(self):
        print ('[VALIDATION TEST] "Myshop-Editor"')
        self.driver = tsetup()
        self.user = user1

    def test_1_check_validation_shop_slogan(self):
        print ("TEST #1 : [Validation] Input Shop Slogan")
        print ("========================================")
        driver = self.driver

        email = self.user['email']
        pwd = self.user['pwd']

        login = loginActivity()
        myshopEdit = myshopEditorActivity()
        logout = logoutActivity()

        login.do_login(driver, self.user, email, pwd, self._site)
        myshopEdit.setObject(driver)
        myshopEdit.goto_myshop_editor(self._site)
        myshopEdit.check_validation_input_shop_slogan_empty(driver)

        time.sleep(2)
        logout.do_logout(driver, self._site)

    def test_2_check_validation_shop_description(self):
        print ("TEST #2 : [Validation] Input Shop Description")
        print ("=============================================")
        driver = self.driver

        email = user1['email']
        pwd = user1['pwd']

        login = loginActivity()
        myshopEdit = myshopEditorActivity()
        logout = logoutActivity()

        login.do_login(driver, self.user, email, pwd, self._site)
        myshopEdit.setObject(driver)
        myshopEdit.goto_myshop_editor(self._site)
        myshopEdit.check_validation_input_shop_description_empty(driver)

        time.sleep(2)
        logout.do_logout(driver, self._site)

    def test_3_check_validation_shop_closed_note(self):
        print ("TEST #3 : [Validation] Input Shop Close Note")
        print ("=============================================")
        driver = self.driver

        email = user1['email']
        pwd = user1['pwd']

        login = loginActivity()
        myshopEdit = myshopEditorActivity()
        logout = logoutActivity()

        login.do_login(driver, self.user, email, pwd, self._site)
        myshopEdit.setObject(driver)
        myshopEdit.goto_myshop_editor(self._site)
        myshopEdit.check_validation_input_shop_closed_note_empty(driver)

        time.sleep(2)
        logout.do_logout(driver, self._site)

    def test_4_check_validation_shop_closed_date(self):
        print ("TEST #4 : [Validation] Input Shop Close Date")
        print ("============================================")
        driver = self.driver

        email = user1['email']
        pwd = user1['pwd']

        login = loginActivity()
        myshopEdit = myshopEditorActivity()
        logout = logoutActivity()

        login.do_login(driver, self.user, email, pwd, self._site)
        myshopEdit.setObject(driver)
        myshopEdit.goto_myshop_editor(self._site)
        myshopEdit.check_validation_input_shop_closed_date_empty(driver)

        time.sleep(2)
        logout.do_logout(driver, self._site)

    def test_5_check_validation_shop_info_all(self):
        print ("TEST #4 : [Validation] Input Empty")
        print ("============================================")
        driver = self.driver

        email = user1['email']
        pwd = user1['pwd']

        login = loginActivity()
        myshopEdit = myshopEditorActivity()
        logout = logoutActivity()

        login.do_login(driver, self.user, email, pwd, self._site)
        myshopEdit.setObject(driver)
        myshopEdit.goto_myshop_editor(self._site)
        myshopEdit.check_validation_input_all_empty(driver)

        time.sleep(2)
        logout.do_logout(driver, self._site)

    def tearDown(self):
        print("Testing akan selesai dalam beberapa saat..")
        self.driver.close()

if __name__ == '__main__':
    unittest.main(warnings='ignore')


