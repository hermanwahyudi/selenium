import os, sys, time
from main.page.base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DepositPage(BasePage):

	_pl = "deposit.pl"

	#Detil Saldo / Deposit Summary
	_total_deposit_loc = (By.CSS_SELECTOR, 'div#deposit-summary.well.well-small.mt-10.mb-10 p.mb-0 strong#bruto-deposit') #total Saldo tokopedia Anda adalah [total_deposit_loc]
	_deposit_withdrawable_loc = (By.CSS_SELECTOR, 'div#deposit-summary.well.well-small.mt-10.mb-10 p.mb-0 strong span#deposit-all-1') #Saldo Tokopedia yang dapat Anda tarik sebesar [_deposit_withdrawable_loc]

	#Filters
	_start_date_loc = (By.CSS_SELECTOR, 'div.pull-left.deposit-filter form.pull-right input#start-date.input-small')
	_end_date_loc = (By.CSS_SELECTOR, 'div.pull-left.deposit-filter form.pull-right input#end-date.input-small')
	_search_button_loc = (By.CSS_SELECTOR, 'div.pull-left.deposit-filter form.pull-right button#filter-deposit-button.btn.btn-second')
	_export_button_loc = (By.CSS_SELECTOR, 'div.pull-left.deposit-filter form.pull-right.ml-10 button#btn-export.btn')

	#Get Deposit (Right panel)
	_usable_deposit_loc = (By.CSS_SELECTOR, 'div.pull-right.get-deposit div.pull-left h4.pull-left.mt-5 span#useable-deposit')
	_withdraw_button_loc = (By.CSS_SELECTOR, 'div.pull-right.get-deposit div.pull-left button#withdrawal-btn.btn.btn-action.pull-left.ml-10')

	#Deposit History Detail Box
	_deposit_detail_all_loc = (By.CSS_SELECTOR, 'div.clear-b div#change-property.clear-b table.table.table-bordered.table-striped tbody tr')
	_activity_datetime_loc = (By.CSS_SELECTOR, 'tr td.span7.word-break div small.muted') #date and time of deposit transaction activity
	_activity_name_loc = (By.CSS_SELECTOR, 'tr td.span7.word-break div:nth-child(2)') #activity name and transaction invoice
	_transaction_nominal_loc = (By.CSS_SELECTOR, 'tr td.span2 div span') #nominal of deposit transaction
	_deposit_per_activity_loc = (By.CSS_SELECTOR, 'tr td.span3 div strong') #deposit per activity


	#general functions

	def open(self, site=""):
		self._open(site, self._pl)

	#functions for SUMMARY
	def get_total_deposit_in_summary(self):
		total_deposit = self.find_element(*self._total_deposit_loc).text
		return(total_deposit)

	def get_usable_deposit_in_summary(self):
		usable_deposit = self.find_element(*self._deposit_withdrawable_loc).text
		return(usable_deposit)

	#functions for DEPOSIT HISTORY DETAILS
	def get_deposit_activity_list(self):
		activity_list = []
		try:
			activity_list = self.find_elements(*self._deposit_detail_all_loc)
			return(activity_list)
		except NoSuchElementException:
			return(activity_list)
			print('Tidak ada aktivitas transaksi deposit')

	def get_activity_datetime(self):
		datetime = self.find_element(*self._activity_datetime_loc).text
		return(datetime)

	def get_activity_name(self):
		activity_name = self.find_element(*self._activity_name_loc).text
		return(activity_name)

	def get_transaction_nominal(self):
		transaction_nominal = self.find_element(*self._transaction_nominal_loc).text
		return(transaction_nominal)

	def get_deposit_per_activity(self):
		deposit_per_activity = self.find_element(*self._deposit_per_activity_loc).text
		return(deposit_per_activity)

	def get_invoice(self):
		activity = str.split(self.get_activity_name(), ' - ')
		return(activity[1])

