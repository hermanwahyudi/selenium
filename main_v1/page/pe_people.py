from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from page.pe_product import *
import os, time, sys

class peoplePage(BasePage):

	# instance variable tab
	_tab_personal_profile_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/ul/li[1]/a")
	_tab_address_list_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/ul/li[2]/a")
	_tab_bank_accounts_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/ul/li[3]/a")

	# instance tab 1 variable personal profile
	_name_loc = (By.ID, "full-name")
	_birthday_date_dd_loc = (By.XPATH, "//select[@name='bday_dd']/option")
	_birthday_date_mm_loc = (By.XPATH, "//select[@name='bday_mm']/option")
	_birthday_date_yy_loc = (By.XPATH, "//select[@name='bday_yy']/option")
	_gender_male_loc = (By.ID, "gender-male")
	_gender_female_loc = (By.ID, "gender-female")
	_hobbies_loc = (By.ID, "hobbies")
	_messenger_loc = (By.ID, "messenger")
	_password_loc = (By.XPATH, "//*[@id='form-edit-profile']/div[8]/div[2]/div/input")
	_submit_loc = (By.XPATH, '//*[@id="form-edit-profile"]/div[9]/button')

	#instance tab 1 variable edit password
	_edit_password_loc = (By.XPATH, '//*[@id="img-profile"]/div[2]/button')
	_old_password_loc = (By.ID, "oldpassword")
	_new_password_loc = (By.ID, "newpassword")
	_conf_password_loc = (By.ID, "confpassword")
	_save_password_loc = (By.XPATH, '//*[@id="edit-contact"]/div[4]/button[2]')

	#instance tab 2 address list
	_add_new_address_loc = (By.XPATH, "//*[@id='content-container']/div[5]/div/div[2]/div/div[1]/div/div[2]/small/a")

	#instance tab 2 add new address
	_address_as_loc = (By.ID, "addr_name")
	_receiver_name_loc = (By.ID, "receiver_name")
	_address_loc = (By.ID, "alamat")
	_postal_code_loc = (By.ID, "postal_code")
	_province_loc = (By.XPATH, "//select[@id='provinsi']/option")
	_regency_loc = (By.XPATH, "//select[@id='kota']/option")
	_district_loc = (By.XPATH, "//select[@id='kec']/option")
	_phone_address_loc = (By.ID, "kontak")
	_submit_new_address_loc = (By.XPATH, '//*[@id="add-address"]/div[9]/button[2]')

	# _search_address_loc = (By.ID, 'siteSearchBox')	
	# _button_search_loc = (By.ID, 'siteSearchSubmit')	

	#dictionary
	dict_url = {
		"url_1" : "https://www.tokopedia.com/",
		"url_2" : "https://test.tokopedia.nginx/",
		"url_3" : "https://www.tokopedia.dev/"
	}

	def go_to_people_page(self):
		self.driver.get(self.dict_url['url_1'] + 'people/' + '1742391')

	def go_to_edit_people_page(self):
		self.driver.find_element(By.XPATH, "//*[@id='content-container']/div[5]/div[1]/div/div/div/div[2]/div/div/a").click()

	def go_to_personal_profile_tab(self):
		self.driver.find_element(*self._tab_personal_profile_loc).click()

	def go_to_address_list_tab(self):
		self.driver.find_element(*self._tab_address_list_loc).click()

	def go_to_bank_accounts_tab(self):
		self.driver.find_element(*self._tab_bank_accounts_loc).click()

	def edit_personal_profile(self):
		try:
			self.driver.find_element(*self._name_loc).click()
			time.sleep(4)
			self.choose_date_of_birth()
			self.driver.find_element(*self._gender_male_loc).click()
			self.driver.find_element(*self._hobbies_loc).clear()
			self.driver.find_element(*self._hobbies_loc).send_keys("Sepakbola")
			self.driver.find_element(*self._messenger_loc).clear()
			self.driver.find_element(*self._messenger_loc).send_keys("muhajirin.imam")
			self.driver.find_element(*self._password_loc).clear()
			self.driver.find_element(*self._password_loc).send_keys("imtokopedia91")
			self.driver.find_element(*self._submit_loc).click()
		except Exception as inst:
			print(inst)


	def choose_date_of_birth(self):
		try:
			time.sleep(1)
			self.driver.execute_script("document.getElementsByName('bday_dd')[0].style.display='block'")
			self.driver.execute_script("document.getElementsByClassName('span2 selectBox-dropdown')[0].style.display='none'")

			list_bday_dd = self.driver.find_elements(*self._birthday_date_dd_loc)
			i = 0
			while i < len(list_bday_dd):
				if i == randint(1, len(list_bday_dd)):
					list_bday_dd[i].click()
					break
				i += 1
			time.sleep(1)
			self.driver.execute_script("document.getElementsByName('bday_mm')[0].style.display='block'")
			self.driver.execute_script("document.getElementsByClassName('span4 selectBox-dropdown')[0].style.display='none'")

			list_bday_mm = self.driver.find_elements(*self._birthday_date_mm_loc)
			i = 0
			while i < len(list_bday_mm):
				if i == randint(1, len(list_bday_mm)):
					list_bday_mm[i].click()
					break
				i += 1
			time.sleep(1)
			self.driver.execute_script("document.getElementsByName('bday_yy')[0].style.display='block'")
			self.driver.execute_script("document.getElementsByClassName('span3 selectBox-dropdown')[0].style.display='none'")

			list_bday_yy = self.driver.find_elements(*self._birthday_date_yy_loc)
			i = 0   
			while i < len(list_bday_yy):
				if i == randint(1, len(list_bday_yy)):
					list_bday_yy[i].click()
					break
				i += 1
		except Exception as inst:
			print(inst)


	def edit_password(self):
		try:
			time.sleep(5)
			self.driver.find_element(*self._edit_password_loc).click()
			time.sleep(5)
			self.driver.find_element(*self._old_password_loc).send_keys("imtokopedia91")
			self.driver.find_element(*self._new_password_loc).send_keys("imtokopedia91")
			self.driver.find_element(*self._conf_password_loc).send_keys("imtokopedia91")
			self.driver.find_element(*self._save_password_loc).click()
			time.sleep(2)
		except Exception as inst:
			print(inst)

	def add_new_address(self):
		try:
			time.sleep(2)
			self.go_to_address_list_tab()
			self.driver.find_element(*self._add_new_address_loc).click()
			self.driver.find_element(*self._address_as_loc).send_keys("Alamat Rumah")
			self.driver.find_element(*self._receiver_name_loc).send_keys("Imam Muhajirin")
			self.driver.find_element(*self._address_loc).send_keys("Graha Handaya Unit R, S, T Jalan Raya Perjuangan No 12A, Kebon Jeruk, Jakarta Barat 11530")
			self.driver.find_element(*self._postal_code_loc).send_keys("11530")
			time.sleep(5)
			self.choose_province()
			time.sleep(5)
			self.choose_regency()
			time.sleep(5)
			self.choose_district()
			self.driver.find_element(*self._phone_address_loc).send_keys("085640226509")
			self.driver.find_element(*self._submit_new_address_loc).click()
		except Exception as inst:
			print(inst)

	def choose_province(self):
		try:
			WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self._province_loc))
			list_province = self.driver.find_elements(*self._province_loc)
			i = 0
			while i < len(list_province):
				if i == randint(1, len(list_province)):
					list_province[i].click()
					break
				i += 1
		except Exception as inst:
			print(inst)

	def choose_regency(self):
		try:
			WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self._regency_loc))
			list_regency = self.driver.find_elements(*self._regency_loc)
			i = 0
			while i < len(list_regency):
				if i == randint(1, len(list_regency)):
					list_regency[i].click()
					break
				i += 1
		except Exception as inst:
			print(inst)

	def choose_district(self):
		try:
			WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self._district_loc))
			list_district = self.driver.find_elements(*self._district_loc)
			i = 0
			while i < len(list_district):
				if i == randint(1, len(list_district)):
					list_district[i].click()
					break
				i += 1
		except Exception as inst:
			print(inst)


	# def search_address(self):
	# 	try:
	# 		time.sleep(1)
	# 		self.driver.find_element(*self._search_address_loc).send_keys("Rumah")
	# 		self.driver.find_element(*self._button_search_loc).click()
	# 		self.driver.find_element().send_keys("Test")
	# 	except Exception as inst:
	# 		print(inst)

