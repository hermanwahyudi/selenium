from main.page.setting.pe_user import *
from main.page.base import *
import time

class UserBank(UserSetting):
    #tab instance for bank accounts list
    _add_bank_account_loc = (By.XPATH, '//*[@id="content-container"]/div[5]/div/div[2]/div/div[1]/small/a')
    #--

    #tab instance for bank accoounts add new bank accounts
    _account_name_loc = (By.ID, "acc_name")
    _account_no_loc = (By.ID, "acc_no")
    _choose_bank_loc = (By.ID, "choose-bank")
    _branch_name_loc = (By.ID, "nama-cabang")
    _send_otp_loc = (By.ID, "sent-verification-code")
    _password_bank_loc = (By.ID, "usr_pwd")
    _submit_new_bank_account_loc = (By.XPATH, "//*[@id='add-bank-acc']/div[7]/button[2]")

    _input_bank_loc = (By.ID, "input-bank")
    _button_search_bank_loc = (By.XPATH, "//*[@id='add-bank']/div[1]/button")
    _radio_choose_bank_loc = (By.ID, "nama-bank-sel1")
    #--

    #tab instance for edit bank accounts
    _link_edit_bank_loc = (By.CSS_SELECTOR, "a.edit-bank-acc")
    _link_edit_bank_list_loc = (By.ID, "edit-bank")
    _link_delete_bank_loc = (By.CSS_SELECTOR, "a.delete-bank-acc")
    _submit_delete_bank_loc = (By.XPATH, '//*[@id="delete-address"]/div[2]/button[2]')
    _link_set_default_bank_loc = (By.CSS_SELECTOR, "a.set-default-acc")
    #_submit_set_default_bank_loc = (By.XPATH, '//*[@id="set-default-bank-acc"]/div[2]/button[2]')
    _submit_set_default_bank_loc = (By.CSS_SELECTOR, 'div.dialog-footer button.btn.btn-action')
    _submit_edit_bank_account_loc = (By.XPATH, '//*[@id="edit-bank-acc"]/div[7]/button[2]')
    #--

    def add_bank_account(self, acc_name, acc_numb, bank_name, bank_branch, pwd):
        try:
            self.check_visible_element(By.XPATH, '//*[@id="content-container"]/div[5]/div/div[2]/div/div[1]/small/a')
            self.driver.find_element(*self._add_bank_account_loc).click()
            self.check_visible_element(By.ID, "acc_name")
            self.driver.find_element(*self._account_name_loc).send_keys(acc_name)
            self.driver.find_element(*self._account_no_loc).send_keys(acc_numb)

            self.driver.find_element(*self._choose_bank_loc).click()
            self.driver.find_element(*self._input_bank_loc).send_keys(bank_name)
            self.driver.find_element(*self._button_search_bank_loc).click()
            time.sleep(3)
            self.driver.find_element(*self._radio_choose_bank_loc).click()
            time.sleep(3)
            self.driver.find_element(*self._branch_name_loc).send_keys(bank_branch)
            self.driver.find_element(*self._send_otp_loc).click()
            time.sleep(30)

            self.driver.find_element(*self._password_bank_loc).send_keys(pwd)
            self.driver.find_element(*self._submit_new_bank_account_loc).click()
            time.sleep(3)
        except Exception as inst:
            print(inst)

    def edit_bank_account(self, acc_name, acc_numb, bank_name, bank_branch, pwd):
        try:
            self.check_visible_element(By.CSS_SELECTOR, "a.edit-bank-acc")
            self.driver.find_element(*self._link_edit_bank_loc).click()
            self.check_visible_element(By.ID, "acc_name")
            self.driver.find_element(*self._account_name_loc).clear()
            self.driver.find_element(*self._account_name_loc).send_keys(acc_name)
            self.driver.find_element(*self._account_no_loc).clear()
            self.driver.find_element(*self._account_no_loc).send_keys(acc_numb)

            self.driver.find_element(*self._link_edit_bank_list_loc).click()
            self.driver.find_element(*self._input_bank_loc).send_keys(bank_name)
            self.driver.find_element(*self._button_search_bank_loc).click()
            time.sleep(5)
            self.driver.find_element(*self._radio_choose_bank_loc).click()
            time.sleep(3)
            self.driver.find_element(*self._branch_name_loc).clear()
            self.driver.find_element(*self._branch_name_loc).send_keys(bank_branch)
            self.driver.find_element(*self._send_otp_loc).click()
            time.sleep(30)

            self.driver.find_element(*self._password_bank_loc).clear()
            self.driver.find_element(*self._password_bank_loc).send_keys(pwd)
            self.driver.find_element(*self._submit_edit_bank_account_loc).click()
            time.sleep(3)
        except Exception as inst:
            print(inst)

    def delete_bank_account(self):
        try:
            time.sleep(1)
            self.driver.find_element(*self._link_delete_bank_loc).click()
            self.check_visible_element(By.XPATH, '//*[@id="delete-address"]/div[2]/button[2]')
            self.driver.find_element(*self._submit_delete_bank_loc).click()
        except Exception as inst:
            print(inst)

    def set_default_bank_account(self):

        driver = self.driver
        click_it = BasePage(driver)

        try:
            time.sleep(1)
            try:
                self.driver.find_element(*self._link_set_default_bank_loc).click()
                self.check_visible_element(By.CSS_SELECTOR, 'div.dialog-footer button.btn.btn-action')
                time.sleep(2)
                click_it.click_on_javascript(self.driver.find_element(*self._submit_set_default_bank_loc))
                #self.driver.find_element(*self._submit_set_default_bank_loc).click()
                #print("> ::You have MORE THAN ONE bank account::")
            except:
                print("> ::Sorry! You have ONLY ONE bank account::")
        except Exception as inst:
            print(inst)

