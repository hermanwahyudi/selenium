from utils.function.setup import *
from utils.lib.user_data import *
from main.activity.desktop_v3.activity_login import *
from main.activity.desktop_v3.activity_logout import *
from main.activity.desktop_v3.activity_user_settings import *
import unittest


class TestAddress(unittest.TestCase):
    # Instance
    _site = "live"

    #dictionary user
    dict = {
        "keyword": "roadway",

        "add_address_as": "alamat tambahan",
        "add_receiver_name": "penerima tambahan",
        "add_the_address": "alamat tambahan",
        "add_postal_code": "88888",
        "add_phone_number": "0818888888",

        "edit_address_as": "alamat editan",
        "edit_receiver_name": "penerima editan",
        "edit_the_address": "alamat editan",
        "edit_postal_code": "99999",
        "edit_phone_number": "0819999999",
    }

    def setUp(self):
        test_driver = ""
        self.driver = tsetup("firefox")
        self.user = user
        self.flag = 0

    def test_add_address(self):
        print("> ::TEST ADD ADDRESS::")
        print("======================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        addAddress = settingAddressActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        addAddress.address_add(driver, self.dict['add_address_as'], self.dict['add_receiver_name'], self.dict['add_the_address'], self.dict['add_postal_code'], self.dict['add_phone_number'])
        logoutValidate.do_logout(driver, self._site)

    def test_edit_address(self):
        print("> ::TEST EDIT ADDRESS::")
        print("=======================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        editAddress = settingAddressActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        editAddress.address_edit(driver, self.dict['edit_address_as'], self.dict['edit_receiver_name'], self.dict['edit_the_address'], self.dict['edit_postal_code'], self.dict['edit_phone_number'], pwd)
        logoutValidate.do_logout(driver, self._site)

    def test_delete_address(self):
        print("> ::TEST DELETE ADDRESS::")
        print("=========================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        deleteAddress = settingAddressActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        deleteAddress.address_delete(driver)
        logoutValidate.do_logout(driver, self._site)

    def test_default_address(self):
        print("> ::TEST DEFAULT ADDRESS::")
        print("==========================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        defaultAddress = settingAddressActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        defaultAddress.address_default(driver)
        logoutValidate.do_logout(driver, self._site)

    def test_search_address(self):
        print("> ::TEST SEARCH ADDRESS::")
        print("=========================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        searchAddress = settingAddressActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        searchAddress.address_search(driver, self.dict['keyword'])
        logoutValidate.do_logout(driver, self._site)

    def test_sort_address(self):
        print("> ::TEST SORTING ADDRESS::")
        print("==========================")
        driver = self.driver
        self.user= user8

        email = self.user['email']
        pwd = self.user['password']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        sortAddress = settingAddressActivity()
        #--

        loginValidate.do_login(driver, self.user, email, pwd, self._site)
        sortAddress.address_sorting(driver)
        logoutValidate.do_logout(driver, self._site)

    def tearDown(self):
        print("> ::Testing has done, the browser window will be closed soon::")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')