from main.page.forgot_password.pe_forgot_password import *
from main.page.base import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class ForgotPasswordActivity():
	#locator path
	_site = "live"

	def goto_fpsw_page(self, driver, input_email):
		fgt = ForgotPassword (driver)
		fgt.open(self._site)
		fgt.ActionSendP(driver, input_email)