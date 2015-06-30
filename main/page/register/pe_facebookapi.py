import os,sys, time
from selenium import webdriver
from main.page.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class FacebookLoginPage(BasePage):

	_pl='facebook_login.pl'

	_email_or_phone_loc = (By.ID, 'email')
	_password_loc = (By.ID, 'pass')
	_keep_me_login_check_loc = (By.ID, 'persist_box')
	_login_loc = (By.NAME, 'login')
	_fb_popup_cancel_loc = (By.NAME, '__CANCEL__')
	#_fb_popup_cancel_loc = (By.XPATH, '//*[@id="platformDialogForm"]/div[2]/table/tbody/tr/td[2]/button[1]')
	#_fb_popup_cancel_loc = (By.CLASS, '_42ft _4jy0 layerConfirm uiOverlayButton _4jy3 _517h _51sy')
	_fb_popup_okay_loc = (By.NAME, '__CONFIRM__')
	#_login_loc = (By.XPATH, '//*[@id="u_0_1"]')

	"""def get_url(self):
		fb_login_url = site + self._pl
		return fb_login_url"""

	def open(self, site, pl=""):
		self.open(site, self._pl)

	def input_email_or_hp(self, userinput):
		self.find_element(*self._email_or_phone_loc).send_keys(userinput)

	def input_password(self, passwd):
		self.find_element(*self._password_loc).send_keys(passwd)

	def check_keep_login(self, userinput):
		if userinput == "yes":
			self.find_element(*self._keep_me_login_check_loc).click()
		else:
			pass
	def login(self):
		self.find_element(*self._login_loc).click()


	def fb_cancel(self, driver):
		try:
			WebDriverWait(driver, 15).until(EC.presence_of_element_located(self._fb_popup_cancel_loc))
			self.find_element(*self._fb_popup_cancel_loc).click()
		except TimeoutException:
			print("Cancel button not found")

	def fb_okay(self, driver):
		try:
			WebDriverWait(driver, 15).until(EC.presence_of_element_located(self._fb_popup_okay_loc))
			self.find_element(*self._fb_popup_okay_loc).click()
		except TimeoutException:
			print("Okay button not found")
