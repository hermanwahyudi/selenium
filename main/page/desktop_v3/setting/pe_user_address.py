from main.page.desktop_v3.setting.pe_user import *
from random import *
from main.page.base import *
import time

class UserAddress(UserSetting):
    #tab locator for address list
    #_add_new_address_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/div/div[1]/div/div[2]/small/a")
    _add_new_address_loc = (By.CSS_SELECTOR, "a.actionlink-newadd-tab.btn.btn-action")
    #--

    #tab instance for add new address
    _address_as_loc = (By.ID, "addr_name")
    _receiver_name_loc = (By.ID, "receiver_name")
    _address_loc = (By.ID, "alamat")
    _postal_code_loc = (By.ID, "postal_code")
    _province_loc = (By.XPATH, "//select[@id='provinsi']/option")
    _regency_loc = (By.XPATH, "//select[@id='kota']/option")
    _district_loc = (By.XPATH, "//select[@id='kec']/option")
    _phone_address_loc = (By.ID, "kontak")
    _password_address_loc = (By.ID, "usr_pwd")
    _submit_new_address_loc = (By.XPATH, '//*[@id="add-address"]/div[9]/button[2]')
    #--

    #tab instance for edit address
    _link_edit_loc = (By.CSS_SELECTOR, "a.edit-address")
    _submit_edit_address_loc = (By.XPATH, '//*[@id="edit-address"]/div[10]/button[2]')
    _link_delete_loc = (By.CSS_SELECTOR, "a.delete-address")
    _submit_delete_address_loc = (By.XPATH, '//*[@id="delete-address"]/div[2]/button[2]')
    _link_set_default_loc = (By.CSS_SELECTOR, "a.set-default")
    _submit_set_default_address_loc = (By.XPATH, '//*[@id="set-default-address"]/div[2]/button[2]')
    #--

    #tab instance for sorting address
    _search_address_loc = (By.ID, 'siteSearchBox')
    _button_search_loc = (By.XPATH, '//*[@id="siteSearchSubmit"]')
    _sorting_address_loc = (By.ID, 'address-order-by')
    #--

    def add_new_address(self, address_as, receiver_name, the_address, postal_code, phone_number):

        driver = self.driver
        click_it = BasePage(driver)

        try:
            self.check_visible_element(By.CSS_SELECTOR, "a.actionlink-newadd-tab.btn.btn-action")
            click_it.click_on_javascript(self.driver.find_element(*self._add_new_address_loc))
            self.check_visible_element(By.ID, "addr_name")
            self.driver.find_element(*self._address_as_loc).send_keys(address_as)
            self.driver.find_element(*self._receiver_name_loc).send_keys(receiver_name)
            self.driver.find_element(*self._address_loc).send_keys(the_address)
            self.driver.find_element(*self._postal_code_loc).send_keys(postal_code)
            self.choose_province()
            self.choose_regency()
            self.choose_district()
            self.driver.find_element(*self._phone_address_loc).send_keys(phone_number)
            click_it.click_on_javascript(self.driver.find_element(*self._submit_new_address_loc))
            time.sleep(3)
        except Exception as inst:
            print(inst)


    def choose_province(self):
        try:
            time.sleep(1)
            list_province = self.driver.find_elements(*self._province_loc)
            i = randint(1, len(list_province))
            list_province[i].click()
        except Exception as inst:
            print(inst)

    def choose_regency(self):
        try:
            time.sleep(1)
            list_regency = self.driver.find_elements(*self._regency_loc)
            i = randint(1, len(list_regency))
            list_regency[i].click()
        except Exception as inst:
            print(inst)

    def choose_district(self):
        try:
            time.sleep(1)
            list_district = self.driver.find_elements(*self._district_loc)
            i = randint(1, len(list_district))
            list_district[i].click()
        except Exception as inst:
            print(inst)

    def edit_address(self, address_as, receiver_name, the_address, postal_code, phone_number, pwd):
        try:
            self.check_visible_element(By.CSS_SELECTOR, "a.edit-address")
            self.driver.find_element(*self._link_edit_loc).click()
            self.check_visible_element(By.ID, "addr_name")
            self.driver.find_element(*self._address_as_loc).clear()
            self.driver.find_element(*self._address_as_loc).send_keys(address_as)
            self.driver.find_element(*self._receiver_name_loc).clear()
            self.driver.find_element(*self._receiver_name_loc).send_keys(receiver_name)
            self.driver.find_element(*self._address_loc).clear()
            self.driver.find_element(*self._address_loc).send_keys(the_address)
            self.driver.find_element(*self._postal_code_loc).clear()
            self.driver.find_element(*self._postal_code_loc).send_keys(postal_code)
            self.choose_province()
            self.choose_regency()
            self.choose_district()
            self.driver.find_element(*self._phone_address_loc).clear()
            self.driver.find_element(*self._phone_address_loc).send_keys(phone_number)
            self.driver.find_element(*self._password_address_loc).clear()
            self.driver.find_element(*self._password_address_loc).send_keys(pwd)
            self.driver.find_element(*self._submit_edit_address_loc).click()
            time.sleep(3)
        except Exception as inst:
            print(inst)


    def delete_address(self):
        try:
            self.check_visible_element(By.CSS_SELECTOR, "a.delete-address")
            self.driver.find_element(*self._link_delete_loc).click()
            self.check_visible_element(By.XPATH, '//*[@id="delete-address"]/div[2]/button[2]')
            self.driver.find_element(*self._submit_delete_address_loc).click()
        except Exception as inst:
            print(inst)

    def set_default_address(self):
        try:
            time.sleep(2)
            self.driver.find_element(*self._link_set_default_loc).click()
            time.sleep(2)
            self.driver.find_element(*self._submit_set_default_address_loc).click()
        except Exception as inst:
            print(inst)


    def search_address(self, keyword):
        try:
            self.check_visible_element(By.ID, 'siteSearchBox')
            self.driver.find_element(*self._search_address_loc).send_keys(keyword)
            self.driver.find_element(*self._button_search_loc).click()
            time.sleep(5)
        except Exception as inst:
            print(inst)

    def choose_sorting(self):
        try:
            time.sleep(2)
            self.driver.execute_script("document.getElementById('address-order-by').style.display = '';")
            list_sorting = self.driver.find_elements(By.XPATH, "//select[@id='address-order-by']/option")
            i = randint(1, len(list_sorting))
            list_sorting[i].click()
        except Exception as inst:
            print(inst)