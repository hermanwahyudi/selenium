from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import os, time, sys
from main.page.base import BasePage
import subprocess


class peoplePage(BasePage):
	# locator variable tab
	_tab_personal_profile_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/ul/li[1]/a")
	_tab_address_list_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/ul/li[2]/a")
	_tab_bank_accounts_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/ul/li[3]/a")
	_tab_notification_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/ul/li[4]/a")
	_tab_privacy_settings_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/ul/li[5]/a")
	#--

	#locator tab 1 personal profile
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

	#locator tab 1 edit photo
	_upload_image_loc = (By.ID, 'pickfiles')
	#--

	# locator tab 1 edit password
	_edit_password_loc = (By.XPATH, '//*[@id="img-profile"]/div[2]/button')
	_old_password_loc = (By.ID, "oldpassword")
	_new_password_loc = (By.ID, "newpassword")
	_confirmation_password_loc = (By.ID, "confpassword")
	_save_password_loc = (By.XPATH, '//*[@id="edit-contact"]/div[4]/button[2]')
	#--

	#locator tab 2 address list
	_add_new_address_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/div/div[1]/div/div[2]/small/a")
	#--

	#instance tab 2 add new address
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

	#instance tab 2 edit address
	_link_edit_loc = (By.CSS_SELECTOR, "a.edit-address")
	_submit_edit_address_loc = (By.XPATH, '//*[@id="edit-address"]/div[10]/button[2]')
	_link_delete_loc = (By.CSS_SELECTOR, "a.delete-address")
	_submit_delete_address_loc = (By.XPATH, '//*[@id="delete-address"]/div[2]/button[2]')
	_link_set_default_loc = (By.CSS_SELECTOR, "a.set-default")
	_submit_set_default_address_loc = (By.XPATH, '//*[@id="set-default-address"]/div[2]/button[2]')
	#--

	#instance tab 2 sorting address
	_search_address_loc = (By.ID, 'siteSearchBox')
	_button_search_loc = (By.XPATH, '//*[@id="siteSearchSubmit"]')
	_sorting_address_loc = (By.ID, 'address-order-by')
	#--

	#instance tab 3 bank accounts list
	_add_bank_account_loc = (By.XPATH, '//*[@id="content-container"]/div[5]/div/div[2]/div/div[1]/small/a')
	#--

	#instance tab 3 bank accoounts add new bank accounts
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

	#instance tab 3 edit bank accounts
	_link_edit_bank_loc = (By.CSS_SELECTOR, "a.edit-bank-acc")
	_link_edit_bank_list_loc = (By.ID, "edit-bank")
	_link_delete_bank_loc = (By.CSS_SELECTOR, "a.delete-bank-acc")
	_submit_delete_bank_loc = (By.XPATH, '//*[@id="delete-address"]/div[2]/button[2]')
	_link_set_default_bank_loc = (By.CSS_SELECTOR, "a.set-default-acc")
	_submit_set_default_bank_loc = (By.XPATH, '//*[@id="set-default-bank-acc"]/div[2]/button[2]')
	_submit_edit_bank_account_loc = (By.XPATH, '//*[@id="edit-bank-acc"]/div[7]/button[2]')
	#--

	#instance tab 4 notification
	_notice_newsletter_loc = (By.ID, 'f-notice-news-letter')
	_notice_review_loc = (By.ID, 'f-notice-review')
	_notice_talk_loc = (By.ID, 'f-notice-talk-product')
	_notice_pm_loc = (By.ID, 'f-notice-pm')
	_notice_pm_admin_loc = (By.ID, 'f-notice-pm-from-admin')
	_button_save_notification_loc = (By.XPATH, '//*[@id="frm_notification"]/button')
	#--

	#instance tab 5 privacy settings
	_setting_birthdate_loc = (By.XPATH, "//select[@id='setting_flag_birthdate']/option")
	_setting_email_loc = (By.XPATH, "//select[@id='setting_flag_email']/option")
	_button_save_privacy_settings_loc = (By.XPATH, '//*[@id="frm_privacy"]/button')
	#--

	# current page
	_pl = 'people/' + '2395339'
	#--

	def open(self, site=""):
		self._open(site, self._pl)

	def go_to_edit_people_page(self):
		self.driver.find_element(By.XPATH,
								 "//*[@id='content-container']/div[5]/div[1]/div/div/div/div[2]/div/div/a").click()

	def go_to_personal_profile_tab(self):
		self.driver.find_element(*self._tab_personal_profile_loc).click()

	def go_to_address_list_tab(self):
		self.driver.find_element(*self._tab_address_list_loc).click()

	def go_to_bank_accounts_tab(self):
		self.driver.find_element(*self._tab_bank_accounts_loc).click()

	def go_to_notification_tab(self):
		self.driver.find_element(*self._tab_notification_loc).click()

	def go_to_privacy_settings_tab(self):
		self.driver.find_element(*self._tab_privacy_settings_loc).click()

	def edit_personal_profile(self):
		try:
			self.driver.find_element(*self._name_loc).click()
			self.choose_date_of_birth()
			self.driver.find_element(*self._gender_male_loc).click()
			self.driver.find_element(*self._hobbies_loc).clear()
			self.driver.find_element(*self._hobbies_loc).send_keys("Sepakbola")
			self.driver.find_element(*self._messenger_loc).clear()
			self.driver.find_element(*self._messenger_loc).send_keys("muhajirin.imam")
			self.driver.find_element(*self._password_loc).clear()
			self.driver.find_element(*self._password_loc).send_keys("imtokopedia91")
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


	def edit_password(self):
		try:
			time.sleep(5)
			self.driver.find_element(*self._edit_password_loc).click()
			time.sleep(5)
			self.driver.find_element(*self._old_password_loc).send_keys("imtokopedia91")
			self.driver.find_element(*self._new_password_loc).send_keys("imtokopedia91")
			self.driver.find_element(*self._confirmation_password_loc).send_keys("imtokopedia91")
			self.driver.find_element(*self._save_password_loc).click()
			time.sleep(2)
		except Exception as inst:
			print(inst)


	def edit_photo(self):
		try:
			time.sleep(3)
			self.driver.find_element(*self._upload_image_loc).click()
			time.sleep(2)
			subprocess.Popen(r"C:\autoit\upload-image.exe")
			time.sleep(2)
		except Exception as  inst:
			print(inst)

	def add_new_address(self):
		try:
			time.sleep(2)
			self.go_to_address_list_tab()
			self.driver.find_element(*self._add_new_address_loc).click()
			self.driver.find_element(*self._address_as_loc).send_keys("Alamat Rumah")
			self.driver.find_element(*self._receiver_name_loc).send_keys("Imam Muhajirin")
			self.driver.find_element(*self._address_loc).send_keys(
				"Graha Handaya Unit R, S, T Jalan Raya Perjuangan No 12A, Kebon Jeruk, Jakarta Barat 11530")
			self.driver.find_element(*self._postal_code_loc).send_keys("11530")
			self.choose_province()
			self.choose_regency()
			self.choose_district()
			self.driver.find_element(*self._phone_address_loc).send_keys("085640226509")
			self.driver.find_element(*self._submit_new_address_loc).click()
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

	def edit_address(self):
		try:
			time.sleep(2)
			self.go_to_address_list_tab()
			self.driver.find_element(*self._link_edit_loc).click()
			self.driver.find_element(*self._address_as_loc).clear()
			self.driver.find_element(*self._address_as_loc).send_keys("Alamat Rumah")
			self.driver.find_element(*self._receiver_name_loc).clear()
			self.driver.find_element(*self._receiver_name_loc).send_keys("Imam Muhajirin")
			self.driver.find_element(*self._address_loc).clear()
			self.driver.find_element(*self._address_loc).send_keys(
				"Graha Handaya Unit R, S, T Jalan Raya Perjuangan No 12A, Kebon Jeruk, Jakarta Barat 11530")
			self.driver.find_element(*self._postal_code_loc).clear()
			self.driver.find_element(*self._postal_code_loc).send_keys("11530")
			self.choose_province()
			self.choose_regency()
			self.choose_district()
			self.driver.find_element(*self._phone_address_loc).clear()
			self.driver.find_element(*self._phone_address_loc).send_keys("085640226509")
			self.driver.find_element(*self._password_address_loc).clear()
			self.driver.find_element(*self._password_address_loc).send_keys("imtokopedia91")
			self.driver.find_element(*self._submit_edit_address_loc).click()
			time.sleep(3)
		except Exception as inst:
			print(inst)


	def delete_address(self):
		try:
			time.sleep(2)
			self.go_to_address_list_tab()
			self.driver.find_element(*self._link_delete_loc).click()
			self.driver.find_element(*self._submit_delete_address_loc).click()
		except Exception as inst:
			print(inst)

	def set_default_address(self):
		try:
			time.sleep(2)
			self.go_to_address_list_tab()
			self.driver.find_element(*self._link_set_default_loc).click()
			self.driver.find_element(*self._submit_set_default_address_loc).click()
		except Exception as inst:
			print(inst)


	def action_address(self, flag, N):
		try:
			print("Action " + str(flag) + " " + str(N) + " kali.")
			i = 0
			while (i < N):
				if (flag == "add"):
					print("Tambah Address ke-" + str(i + 1))
					self.add_new_address()
				if (flag == "edit"):
					print("Edit Address ke-" + str(i + 1))
					self.edit_address()
				if (flag == "delete"):
					self.delete_address()
					print("Hapus Address ke-" + str(i + 1))
				if (flag == "default"):
					self.set_default_address()
					print("Set Default Address ke-" + str(i + 1))
				self.driver.refresh()
				i += 1
		except Exception as inst:
			print(inst)

	def search_address(self):
		try:
			time.sleep(2)
			self.go_to_address_list_tab()
			self.driver.find_element(*self._search_address_loc).send_keys("SADIS")
			self.driver.find_element(*self._button_search_loc).click()
			time.sleep(5)
		except Exception as inst:
			print(inst)

	def choose_sorting(self):
		try:
			time.sleep(2)
			self.go_to_address_list_tab()
			self.driver.execute_script("document.getElementById('address-order-by').style.display = '';")
			list_sorting = self.driver.find_elements(By.XPATH, "//select[@id='address-order-by']/option")
			i = randint(1, len(list_sorting))
			list_sorting[i].click()
		except Exception as inst:
			print(inst)

	def add_bank_account(self):
		try:
			time.sleep(2)
			self.go_to_bank_accounts_tab()

			self.driver.find_element(*self._add_bank_account_loc).click()

			self.driver.find_element(*self._account_name_loc).send_keys("Imam Muhajirin")
			self.driver.find_element(*self._account_no_loc).send_keys("00123456789")

			self.driver.find_element(*self._choose_bank_loc).click()
			self.driver.find_element(*self._input_bank_loc).send_keys("BCA")
			self.driver.find_element(*self._button_search_bank_loc).click()
			self.driver.find_element(*self._radio_choose_bank_loc).click()

			self.driver.find_element(*self._branch_name_loc).send_keys("Kebon Jeruk")
			self.driver.find_element(*self._send_otp_loc).click()
			time.sleep(30)

			self.driver.find_element(*self._password_bank_loc).send_keys("imtokopedia91")
			self.driver.find_element(*self._submit_new_bank_account_loc).click()
		except Exception as inst:
			print(inst)

	def edit_bank_account(self):
		try:
			time.sleep(2)
			self.go_to_bank_accounts_tab()
			self.driver.find_element(*self._link_edit_bank_loc).click()

			self.driver.find_element(*self._account_name_loc).clear()
			self.driver.find_element(*self._account_name_loc).send_keys("Imam Muhajirin")
			self.driver.find_element(*self._account_no_loc).clear()
			self.driver.find_element(*self._account_no_loc).send_keys("98765432100")

			self.driver.find_element(*self._link_edit_bank_list_loc).click()
			self.driver.find_element(*self._input_bank_loc).send_keys("BCA")
			self.driver.find_element(*self._button_search_bank_loc).click()
			self.driver.find_element(*self._radio_choose_bank_loc).click()

			self.driver.find_element(*self._branch_name_loc).clear()
			self.driver.find_element(*self._branch_name_loc).send_keys("Kedoya")
			self.driver.find_element(*self._send_otp_loc).click()
			time.sleep(30)

			self.driver.find_element(*self._password_bank_loc).clear()
			self.driver.find_element(*self._password_bank_loc).send_keys("imtokopedia91")
			self.driver.find_element(*self._submit_edit_bank_account_loc).click()
		except Exception as inst:
			print(inst)

	def delete_bank_account(self):
		try:
			time.sleep(2)
			self.go_to_bank_accounts_tab()
			self.driver.find_element(*self._link_delete_bank_loc).click()
			self.driver.find_element(*self._submit_delete_bank_loc).click()
		except Exception as inst:
			print(inst)

	def set_default_bank_account(self):
		try:
			time.sleep(2)
			self.go_to_bank_accounts_tab()
			self.driver.find_element(*self._link_set_default_bank_loc).click()
			self.driver.find_element(*self._submit_set_default_bank_loc).click()
		except Exception as inst:
			print(inst)

	def action_bank_account(self, flag, N):
		try:
			print("Action " + str(flag) + " " + str(N) + " kali.")
			i = 0
			while (i < N):
				if (flag == "add"):
					print("Tambah Bank Account ke-" + str(i + 1))
					self.add_bank_account()
				if (flag == "edit"):
					print("Edit Bank Account ke-" + str(i + 1))
					self.edit_bank_account()
				if (flag == "delete"):
					self.delete_bank_account()
					print("Hapus Bank Account ke-" + str(i + 1))
				if (flag == "default"):
					self.set_default_bank_account()
					print("Set Default Bank Account ke-" + str(i + 1))
				self.driver.refresh()
				i += 1
		except Exception as inst:
			print(inst)

	def set_notification(self):
		try:
			time.sleep(2)
			self.go_to_notification_tab()
			i = 1
			while (i < 2):
				self.driver.find_element(*self._notice_newsletter_loc).click()
				self.driver.find_element(*self._notice_review_loc).click()
				self.driver.find_element(*self._notice_talk_loc).click()
				self.driver.find_element(*self._notice_pm_loc).click()
				self.driver.find_element(*self._notice_pm_admin_loc).click()
				i += 1
				self.driver.find_element(*self._button_save_notification_loc).click()
		except Exception as inst:
			print(inst)

	def set_privacy_settings(self):
		try:
			time.sleep(2)
			self.go_to_privacy_settings_tab()
			self.set_birthdate_settings()
			self.set_email_settings()
			self.driver.find_element(*self._button_save_privacy_settings_loc).click()
		except Exception as inst:
			print(inst)

	def set_email_settings(self):
		try:
			time.sleep(2)
			self.driver.execute_script("document.getElementById('setting_flag_email').style.display = 'block';")
			list_select = self.driver.find_elements(*self._setting_email_loc)
			list_select[1].click()
		except Exception as inst:
			print(inst)

	def get_people_ID(self):
		url = self.driver.current_url
		print (url)
		ID = url.strip('https://www.tokopedia.com/people/')
		return(ID)
