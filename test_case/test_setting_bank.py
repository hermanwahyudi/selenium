from main.function.setup import *
from main.activity.activity_login import *
from main.activity.activity_logout import *
from main.activity.activity_user_settings import *
import unittest


class TestBank(unittest.TestCase):
    # Instance
    _site = "live"

    #dictionary user
    dict = {
        "email_1": "tkpd.qc+35@gmail.com",
        "pass_1": "123456789",
        "email_2": "tkpd.qc+36@gmail.com",
        "pass_2": "123456789",

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

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        addBank = settingBankActivity()
        #--

        loginValidate.do_login(driver, self.dict['email_1'], self.dict['pass_1'], self._site)
        addBank.bank_add(driver, self.dict['add_acc_name'], self.dict['add_acc_numb'], self.dict['add_bank_name'],
                           self.dict['add_bank_branch'], self.dict['pass_1'])
        logoutValidate.do_logout(driver, self._site)

    def test_edit_bank(self):
        print("> ::TEST EDIT BANK::")
        print("====================")
        driver = self.driver

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        editBank = settingBankActivity()
        #--

        loginValidate.do_login(driver, self.dict['email_1'], self.dict['pass_1'], self._site)
        editBank.bank_edit(driver,  self.dict['edit_acc_name'], self.dict['edit_acc_numb'], self.dict['edit_bank_name'],
                           self.dict['edit_bank_branch'], self.dict['pass_1'])
        logoutValidate.do_logout(driver, self._site)

    def test_delete_bank(self):
        print("> ::TEST DELETE BANK::")
        print("======================")
        driver = self.driver

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        deleteBank = settingBankActivity()
        #--

        loginValidate.do_login(driver, self.dict['email_1'], self.dict['pass_1'], self._site)
        deleteBank.bank_delete(driver)
        logoutValidate.do_logout(driver, self._site)

    def test_default_bank(self):
        print("> ::TEST DEFAULT BANK::")
        print("=======================")
        driver = self.driver

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        defaultBank = settingBankActivity()
        #--

        loginValidate.do_login(driver, self.dict['email_1'], self.dict['pass_1'], self._site)
        defaultBank.bank_default(driver)
        logoutValidate.do_logout(driver, self._site)

    def tearDown(self):
        print("> ::Testing has done, the browser window will be closed soon::")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')