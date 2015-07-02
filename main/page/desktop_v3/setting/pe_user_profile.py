from main.page.desktop_v3.setting.pe_user import *
from selenium.webdriver.common.by import By
from random import randint
import time, subprocess

class UserProfile(UserSetting):
    #tab locator for detail
    _name_loc = (By.ID, "full-name")
    _birthday_date_dd_loc = (By.XPATH, "//select[@name='bday_dd']/option")
    _birthday_date_mm_loc = (By.XPATH, "//select[@name='bday_mm']/option")
    _birthday_date_yy_loc = (By.XPATH, "//select[@name='bday_yy']/option")
    _gender_male_loc = (By.ID, "gender-male")
    _gender_female_loc = (By.ID, "gender-female")
    _hobbies_loc = (By.ID, "hobbies")
    _messenger_loc = (By.ID, "messenger")
    _password_loc = (By.XPATH, "//*[@id='form-edit-profile']/div[8]/div[2]/div/input")
    _submit_personal_profile_loc = (By.XPATH, '//*[@id="form-edit-profile"]/div[9]/button')
    #--

    #tab locator for change picture
    _upload_image_loc = (By.ID, 'pickfiles')
    #--

    #tab locator for change password
    _edit_password_loc = (By.XPATH, '//*[@id="img-profile"]/div[2]/button')
    _old_password_loc = (By.ID, "oldpassword")
    _new_password_loc = (By.ID, "newpassword")
    _confirmation_password_loc = (By.ID, "confpassword")
    _save_password_loc = (By.XPATH, '//*[@id="edit-contact"]/div[4]/button[2]')
    #--

    def edit_personal_profile(self, hobby, messenger, pwd):
        try:
            self.driver.find_element(*self._name_loc).click()
            self.choose_date_of_birth()
            self.driver.find_element(*self._gender_male_loc).click()
            self.driver.find_element(*self._hobbies_loc).clear()
            self.driver.find_element(*self._hobbies_loc).send_keys(hobby)
            self.driver.find_element(*self._messenger_loc).clear()
            self.driver.find_element(*self._messenger_loc).send_keys(messenger)
            self.driver.find_element(*self._password_loc).clear()
            self.driver.find_element(*self._password_loc).send_keys(pwd)
            time.sleep(2)
            self.driver.find_element(*self._submit_personal_profile_loc).click()
        except Exception as inst:
            print(inst)


    def choose_date_of_birth(self):
        try:
            time.sleep(1)
            self.driver.execute_script("document.getElementsByName('bday_dd')[0].style.display='block'")
            self.driver.execute_script(
                "document.getElementsByClassName('span2 selectBox-dropdown')[0].style.display='none'")

            list_bday_dd = self.driver.find_elements(*self._birthday_date_dd_loc)
            i = randint(1, len(list_bday_dd))
            list_bday_dd[i].click()

            time.sleep(1)
            self.driver.execute_script("document.getElementsByName('bday_mm')[0].style.display='block'")
            self.driver.execute_script(
                "document.getElementsByClassName('span4 selectBox-dropdown')[0].style.display='none'")

            list_bday_mm = self.driver.find_elements(*self._birthday_date_mm_loc)
            i = randint(1, len(list_bday_mm))
            list_bday_mm[i].click()

            time.sleep(1)
            self.driver.execute_script("document.getElementsByName('bday_yy')[0].style.display='block'")
            self.driver.execute_script(
                "document.getElementsByClassName('span3 selectBox-dropdown')[0].style.display='none'")

            list_bday_yy = self.driver.find_elements(*self._birthday_date_yy_loc)
            i = randint(1, len(list_bday_yy))
            list_bday_yy[i].click()

        except Exception as inst:
            print(inst)


    def edit_password(self, pwd, new_pwd):
        try:
            time.sleep(5)
            self.driver.find_element(*self._edit_password_loc).click()
            time.sleep(5)
            self.driver.find_element(*self._old_password_loc).send_keys(pwd)
            self.driver.find_element(*self._new_password_loc).send_keys(new_pwd)
            self.driver.find_element(*self._confirmation_password_loc).send_keys(new_pwd)
            self.driver.find_element(*self._save_password_loc).click()
            time.sleep(2)
        except Exception as inst:
            print(inst)


    def edit_photo(self):
        try:
            time.sleep(3)
            self.driver.find_element(*self._upload_image_loc).click()
            time.sleep(2)
            #Put the new image in folder C:\autoit and rename it with "FileUpload.jpg"
            subprocess.Popen(r"C:\autoit\upload-image.exe")
            time.sleep(2)
        except Exception as  inst:
            print(inst)