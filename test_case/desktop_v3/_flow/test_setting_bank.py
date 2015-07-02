from utils.function.setup import *
from utils.lib.user_data import *
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_logout import *
from main.activity.desktop_v3.activity_user_settings import *
import unittest


class TestBank(unittest.TestCase):
    # Instance
    _site = "live"

    #dictionary user
    dict = {
        "add_acc_name": "bank add",
        "add_acc_numb": "85851111",
        "add_bank_name": "BANK CENTRAL ASIA",
        "add_bank_branch": "cihampelas",

        "edit_acc_name": "bank edit",
        "edit_acc_numb": "7475555",
        "edit_bank_name": "BANK CENTRAL ASIA",
        "edit_bank_branch": "cibinong"
    }

    def setUp(self):
        test_driver = ""
        self.driver = tsetup("firefox")
        self.flag = 0

    def test_add_bank(self):
        print("> ::TEST ADD BANK::")
        print("===================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        addBank = settingBankActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        addBank.bank_add(driver, self.dict['add_acc_name'], self.dict['add_acc_numb'], self.dict['add_bank_name'], self.dict['add_bank_branch'], pwd)
        logoutValidate.do_logout(driver, self._site)

    def test_edit_bank(self):
        print("> ::TEST EDIT BANK::")
        print("====================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        editBank = settingBankActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        editBank.bank_edit(driver,  self.dict['edit_acc_name'], self.dict['edit_acc_numb'], self.dict['edit_bank_name'], self.dict['edit_bank_branch'], pwd)
        logoutValidate.do_logout(driver, self._site)

    def test_delete_bank(self):
        print("> ::TEST DELETE BANK::")
        print("======================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        deleteBank = settingBankActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        deleteBank.bank_delete(driver)
        logoutValidate.do_logout(driver, self._site)

    def test_default_bank(self):
        print("> ::TEST DEFAULT BANK::")
        print("=======================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        defaultBank = settingBankActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        defaultBank.bank_default(driver)
        logoutValidate.do_logout(driver, self._site)

    def tearDown(self):
        print("> ::Testing has done, the browser window will be closed soon::")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')