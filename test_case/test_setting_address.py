from main.function.setup import *
from main.activity.activity_login import *
from main.activity.activity_logout import *
from main.activity.activity_user_settings import *
import unittest


class TestAddress(unittest.TestCase):
    # Instance
    _site = "live"

    #dictionary user
    dict = {
        "email_1": "tkpd.qc+35@gmail.com",
        "pass_1": "123456789",
        "email_2": "tkpd.qc+36@gmail.com",
        "pass_2": "12345678",

        "keyword": "roadway",

        "add_address_as": "alamat paling hits",
        "add_receiver_name": "gak ada penerima",
        "add_the_address": "jalan raya rawa",
        "add_postal_code": "52888",
        "add_phone_number": "0818985555",

        "edit_address_as": "alamat edit",
        "edit_receiver_name": "edit penerima",
        "edit_the_address": "jalan raya edit",
        "edit_postal_code": "85588",
        "edit_phone_number": "0818987977",
    }


    def setUp(self):
        test_driver = ""
        self.driver = tsetup("firefox")
        self.flag = 0

    def test_add_address(self):
        print("> ::TEST ADD ADDRESS::")
        print("======================")
        driver = self.driver

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        addAddress = settingAddressActivity()
        #--

        loginValidate.do_login(driver, self.dict['email_1'], self.dict['pass_1'], self._site)
        addAddress.address_add(driver, self.dict['add_address_as'], self.dict['add_receiver_name'],
                               self.dict['add_the_address'], self.dict['add_postal_code'],
                               self.dict['add_phone_number'])
        logoutValidate.do_logout(driver, self._site)

    def test_edit_address(self):
        print("> ::TEST EDIT ADDRESS::")
        print("=======================")
        driver = self.driver

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        editAddress = settingAddressActivity()
        #--

        loginValidate.do_login(driver, self.dict['email_1'], self.dict['pass_1'], self._site)
        editAddress.address_edit(driver, self.dict['edit_address_as'], self.dict['edit_receiver_name'],
                                 self.dict['edit_the_address'], self.dict['edit_postal_code'],
                                 self.dict['edit_phone_number'], self.dict['pass_1'])
        logoutValidate.do_logout(driver, self._site)

    def test_delete_address(self):
        print("> ::TEST DELETE ADDRESS::")
        print("=========================")
        driver = self.driver

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        deleteAddress = settingAddressActivity()
        #--

        loginValidate.do_login(driver, self.dict['email_1'], self.dict['pass_1'], self._site)
        deleteAddress.address_delete(driver)
        logoutValidate.do_logout(driver, self._site)

    def test_default_address(self):
        print("> ::TEST DEFAULT ADDRESS::")
        print("==========================")
        driver = self.driver

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        defaultAddress = settingAddressActivity()
        #--

        loginValidate.do_login(driver, self.dict['email_1'], self.dict['pass_1'], self._site)
        defaultAddress.address_default(driver)
        logoutValidate.do_logout(driver, self._site)

    def test_search_address(self):
        print("> ::TEST SEARCH ADDRESS::")
        print("=========================")
        driver = self.driver

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        searchAddress = settingAddressActivity()
        #--

        loginValidate.do_login(driver, self.dict['email_1'], self.dict['pass_1'], self._site)
        searchAddress.address_search(driver, self.dict['keyword'])
        logoutValidate.do_logout(driver, self._site)

    def test_sort_address(self):
        print("> ::TEST SORTING ADDRESS::")
        print("==========================")
        driver = self.driver

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        sortAddress = settingAddressActivity()
        #--

        loginValidate.do_login(driver, self.dict['email_1'], self.dict['pass_1'], self._site)
        sortAddress.address_sorting(driver)
        logoutValidate.do_logout(driver, self._site)

    def tearDown(self):
        print("> ::Testing has done, the browser window will be closed soon::")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')