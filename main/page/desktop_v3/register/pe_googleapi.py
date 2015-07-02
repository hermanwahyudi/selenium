import os,sys, time
from selenium import webdriver
from main.page.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class GooglePlusLoginPage(BasePage):

	#elements in google login
	_email_loc = (By.ID,'Email')
	_password_loc = (By.ID,'Passwd')
	_login_button_loc = (By.ID,'signIn')

	#elements in authentication page
	#_cancel_button_loc = (By.CSS_SELECTOR, 'div.connect_container form.connect_approve button.submit_deny_access')
	_accept_button_loc = (By.CSS_SELECTOR, 'div.connect_container form.connect_approve button.submit_approve_access')
	_cancel_button_loc = (By.ID,'submit_deny_access')
	_accept_button_loc = (By.ID,'submit_approve_access')

	def input_email(self, driver, email):
		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located(self._email_loc))
			self.find_element(*self._email_loc).send_keys(email)
			print('Input e-mail berhasil')
		except TimeoutException:
			print('Timeout. Elemen tidak ditemukan')

	def input_password(self, driver, password):
		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located(self._password_loc))
			self.find_element(*self._password_loc).send_keys(password)
			print('Input password berhasil')
		except TimeoutException:
			print('Timeout. Elemen tidak ditemukan')

	def login(self, driver):
		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located(self._login_button_loc))
			self.find_element(*self._login_button_loc).click()
			print('Klik tombol login berhasil')
		except TimeoutException:
			print('Timeout. Elemen tidak ditemukan')

	def click_accept(self, driver):
		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located(self._accept_button_loc))
			self.find_element(*self._accept_button_loc).click()
			print('Klik tombol accept berhasil')
		except TimeoutException:
			print('Tombol accept tidak ditemukan')

	def click_cancel(self, driver):
		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located(self._cancel_button_loc))
			self.find_element(*self._cancel_button_loc).click()
			print('Klik tombol cancel berhasil')
		except TimeoutException:
			print('Tombol cancel tidak ditemukan')