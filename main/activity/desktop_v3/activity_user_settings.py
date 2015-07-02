from main.page.desktop_v3.setting.pe_user import *
from main.page.desktop_v3.setting.pe_user_profile import *
from main.page.desktop_v3.setting.pe_user_bank import *
from main.page.desktop_v3.setting.pe_user_address import *
from main.page.desktop_v3.header import *
from main.page.desktop_v3.setting.pe_user_notif import *

#dictionary validation
dict_valid = {
    'notif_changed_id': "Anda telah berhasil mengubah penerimaan Notifikasi Email.",
    'notif_changed_en': "You have successfully changed your email notification.",

    'pict_failed_id': "Unggah Gagal.",
    'pict_failed_en': "Upload Failed",

    'pass_changed_id': "Anda telah berhasil mengubah password.",
    'pass_changed_en': "You have successfully changed your password.",

    'profile_changed_id': "Anda telah berhasil mengubah profil.",
    'profile_changed_en': "You have successfully changed your profile.",

    'adrs_pass_id': "harus diisi.",
    'adrs_pass_en': "must be filled.",
    'adrs_error_id': "Maaf",
    'adrs_error_en': "Sorry",
    'adrs_search_id': "Tidak ada Data",
    'adrs_search_en': "No Data",

    'bank_error_id': "harus diisi",
    'bank_error_en': "must be filled",
    'bank_set_error_id': "Salah",
    'bank_set_error_en': "Wrong",
    'bank_sry_error_id': "Maaf",
    'bank_sry_error_en': "Sorry",
    'bank_no_error_id': "Tidak ada Data",
    'bank_no_error_en': "No Data"

}

class settingProfileActivity:

    def set_objects(self, driver):
        #Object Activity
        self.openTab= HeaderPage(driver)
        self.moveTab = UserSetting(driver)
        self.profileAct = UserProfile(driver)
        #--

        self.openTab.mouse_hover_to_user_bar()
        self.openTab.mouse_hover_to_setting()
        print("> ::Enter setting page::")
        self.moveTab.select_user_profile_tab()
        print("> ::Enter personal profile tab::")

    def profile_data(self, driver, hobby, messenger, pwd):
        self.set_objects(driver)
        self.profileAct.edit_personal_profile(hobby, messenger, pwd)
        time.sleep(1)
        try:
            assert dict_valid['profile_changed_en'] in driver.find_element_by_tag_name("body").text
            print("> ::Success to change the profile [English]::")
        except:
            try:
                assert dict_valid['profile_changed_id'] in driver.find_element_by_tag_name("body").text
                print("> ::Success to change the profile [Indonesian]::")
            except:
                print("> ::Failed to change the profile::")

    def profile_password(self, driver, pwd, new_pwd):
        self.set_objects(driver)
        self.profileAct.edit_password(pwd, new_pwd)
        time.sleep(1)
        try:
            assert dict_valid['pass_changed_en'] in driver.find_element_by_tag_name("body").text
            print("> ::Success to change the password [English]::")
        except:
            try:
                assert dict_valid['pass_changed_id'] in driver.find_element_by_tag_name("body").text
                print("> ::Success to change the password [Indonesian]::")
            except:
                print("> ::Failed to change the password::")

    def profile_picture(self, driver):
        self.set_objects(driver)
        self.profileAct.edit_photo()
        time.sleep(1)
        try:
            assert dict_valid['pict_failed_en'] in driver.find_element_by_tag_name("body").text
            print("> ::Failed to change the picture [English]::")
        except:
            try:
                assert dict_valid['pict_failed_id'] in driver.find_element_by_tag_name("body").text
                print("> ::Failed to change the picture [Indonesian]::")
            except:
                print("> ::Success to change the picture::")

class settingAddressActivity:

    def set_objects(self, driver):
        #Object Activity
        self.openTab= HeaderPage(driver)
        self.moveTab = UserSetting(driver)
        self.addressAct = UserAddress(driver)
        #--

        self.openTab.mouse_hover_to_user_bar()
        self.openTab.mouse_hover_to_setting()
        print("> ::Enter setting page::")
        self.moveTab.select_address_list_tab()
        print("> ::Enter address list tab::")

    def validation_address(self, driver, mark):
        time.sleep(2)
        try:
            assert dict_valid['adrs_error_en'] in driver.find_element_by_tag_name("body").text
            if mark == 0:
                print("> ::Failed to add a new address [English]::")
            elif mark == 1:
                print("> ::Failed to edit an address [English]::")
        except:
            try:
                assert dict_valid['adrs_error_id'] in driver.find_element_by_tag_name("body").text
                if mark == 0:
                    print("> ::Failed to add a new address [Indonesian]::")
                elif mark == 1:
                    print("> ::Failed to edit an address [Indonesian]::")
            except:
                try:
                    assert dict_valid['adrs_pass_en'] in driver.find_element_by_tag_name("body").text
                    if mark == 0:
                        print("> ::Failed to add a new address [English]::")
                    elif mark == 1:
                        print("> ::Failed to edit an address [English]::")
                except:
                    try:
                        assert dict_valid['adrs_pass_id'] in driver.find_element_by_tag_name("body").text
                        if mark == 0:
                            print("> ::Failed to add a new address [Indonesian]::")
                        elif mark == 1:
                            print("> ::Failed to edit an address [Indonesian]::")
                    except:
                        if mark == 0:
                            print("> ::Success to add a new address::")
                        elif mark == 1:
                            print("> ::Success to edit an address::")

    def address_add(self, driver, address_as, receiver_name, the_address, postal_code, phone_number):
        self.set_objects(driver)
        self.addressAct.add_new_address(address_as, receiver_name, the_address, postal_code, phone_number)
        self.validation_address(driver, 0)


    def address_edit(self, driver, address_as, receiver_name, the_address, postal_code, phone_number, pwd):
        self.set_objects(driver)
        self.addressAct.edit_address(address_as, receiver_name, the_address, postal_code, phone_number, pwd)
        self.validation_address(driver, 1)

    def address_delete(self, driver):
        self.set_objects(driver)
        self.addressAct.delete_address()
        time.sleep(2)
        try:
            assert dict_valid['bank_sry_error_en'] in driver.find_element_by_tag_name("body").text
            print("> ::Failed to delete a new bank account [English]::")
        except:
            try:
                assert dict_valid['bank_sry_error_id'] in driver.find_element_by_tag_name("body").text
                print("> ::Failed to delete a new bank account [Indonesia]::")
            except:
                print("> ::Success to delete a bank account::")

    def address_default(self, driver):
        self.set_objects(driver)
        self.addressAct.set_default_address()
        time.sleep(2)
        try:
            assert dict_valid['bank_sry_error_en'] in driver.find_element_by_tag_name("body").text
            print("> ::Failed to set default bank account [English]::")
        except:
            try:
                assert dict_valid['bank_sry_error_id'] in driver.find_element_by_tag_name("body").text
                print("> ::Failed to set default bank account [Indonesia]::")
            except:
                print("> ::Success to set default bank account::")

    def address_search(self, driver, keyword):
        self.set_objects(driver)
        self.addressAct.search_address(keyword)

        try:
            assert dict_valid['adrs_search_en'] in driver.find_element_by_tag_name("body").text
            print("> ::Search has no result [English]::")
        except:
            try:
                assert dict_valid['adrs_search_id'] in driver.find_element_by_tag_name("body").text
                print("> ::Search has no result [Indonesian]::")
            except:
                print("> ::Success to search the keyword::")

    def address_sorting(self, driver):
        self.set_objects(driver)
        self.addressAct.choose_sorting()
        print("> ::Success to sort addresses::")

class settingBankActivity:

    def set_objects(self, driver):
        #Object Activity
        self.openTab= HeaderPage(driver)
        self.moveTab = UserSetting(driver)
        self.bankAct = UserBank(driver)
        #--

        self.openTab.mouse_hover_to_user_bar()
        time.sleep(2)
        self.openTab.mouse_hover_to_setting()
        print("> ::Enter setting page::")
        self.moveTab.select_bank_accounts_tab()
        print("> ::Enter bank accounts tab::")

    def validation_bank(self, driver, mark):
        try:
            assert dict_valid['bank_error_en'] in driver.find_element_by_tag_name("body").text
            if mark == 1:
                print("> ::Failed to add a new bank account [English]::")
            elif mark == 0:
                print("> ::Failed to edit bank account [English]::")
        except:
            try:
                assert dict_valid['bank_error_id'] in driver.find_element_by_tag_name("body").text
                if mark == 1:
                    print("> ::Failed to add a new bank account [Indonesian]::")
                elif mark == 0:
                    print("> ::Failed to edit a bank account [Indonesian]::")
            except:
                try:
                    assert dict_valid['bank_set_error_id'] in driver.find_element_by_tag_name("body").text
                    if mark == 1:
                        print("> ::Failed to add a new bank account [Indonesian]::")
                    elif mark == 0:
                        print("> ::Failed to edit a bank account [Indonesian]::")
                except:
                    try:
                        assert dict_valid['bank_set_error_en'] in driver.find_element_by_tag_name("body").text
                        if mark == 1:
                            print("> ::Failed to add a new bank account [English]::")
                        elif mark == 0:
                            print("> ::Failed to edit a bank account [English]::")
                    except:
                        try:
                            assert dict_valid['bank_no_error_en'] in driver.find_element_by_tag_name("body").text
                            if mark == 1:
                                print("> ::Failed to add a new bank account [English]::")
                            elif mark == 0:
                                print("> ::Failed to edit a bank account [English]::")
                        except:
                            try:
                                assert dict_valid['bank_no_error_id'] in driver.find_element_by_tag_name("body").text
                                if mark == 1:
                                    print("> ::Failed to add a new bank account [Indonesia]::")
                                elif mark == 0:
                                    print("> ::Failed to edit a bank account [Indonesia]::")
                            except:
                                if mark == 1:
                                    print("> ::Success to add a new bank account::")
                                elif mark == 0:
                                    print("> ::Success to edit a bank account::")


    def bank_add(self, driver, acc_name, acc_numb, bank_name, bank_branch, pwd):
        self.set_objects(driver)
        time.sleep(2)
        self.bankAct.add_bank_account(acc_name, acc_numb, bank_name, bank_branch, pwd)
        time.sleep(2)
        self.validation_bank(driver, 1)

    def bank_edit(self, driver, acc_name, acc_numb, bank_name, bank_branch, pwd):
        self.set_objects(driver)
        time.sleep(2)
        self.bankAct.edit_bank_account(acc_name, acc_numb, bank_name, bank_branch, pwd)
        time.sleep(2)
        self.validation_bank(driver, 0)

    def bank_delete(self, driver):
        self.set_objects(driver)
        time.sleep(2)
        self.bankAct.delete_bank_account()
        time.sleep(2)
        try:
            assert dict_valid['bank_sry_error_en'] in driver.find_element_by_tag_name("body").text
            print("> ::Failed to delete a new bank account [English]::")
        except:
            try:
                assert dict_valid['bank_sry_error_id'] in driver.find_element_by_tag_name("body").text
                print("> ::Failed to delete a new bank account [Indonesia]::")
            except:
                print("> ::Success to delete a bank account::")

    def bank_default(self, driver):
        self.set_objects(driver)
        time.sleep(2)
        self.bankAct.set_default_bank_account()
        self.time(2)
        try:
            assert dict_valid['bank_sry_error_en'] in driver.find_element_by_tag_name("body").text
            print("> ::Failed to set default bank account [English]::")
        except:
            try:
                assert dict_valid['bank_sry_error_id'] in driver.find_element_by_tag_name("body").text
                print("> ::Failed to set default bank account [Indonesia]::")
            except:
                print("> ::Success to set default bank account::")

class settingNotificationActivity:

    def notif_setting(self, driver):
        #Object Activity
        openTab = HeaderPage(driver)
        moveTab = UserSetting(driver)
        notifAct = UserNotif(driver)
        #--

        openTab.mouse_hover_to_user_bar()
        openTab.mouse_hover_to_setting()
        print("> ::Enter setting page::")
        moveTab.select_notif_tab()
        print("> ::Enter notification tab::")
        notifAct.set_notification()

        try:
            assert dict_valid['notif_changed_en'] in driver.find_element_by_tag_name("body").text
            print("> ::Success to change the notifications [English]::")
        except:
            try:
                assert dict_valid['notif_changed_id'] in driver.find_element_by_tag_name("body").text
                print("> ::Success to change the notifications [Indonesian]::")
            except:
                print("> ::Failed to change the notifications::")