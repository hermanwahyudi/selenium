import os, sys, time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from main.page.desktop_v3.deposit.pe_deposit import *
from main.page.base import BasePage

class depositActivity():

	def check_deposit_details(self, driver, site):
		deposit = DepositPage(driver)
		deposit.open(site)
		deposit_summary = deposit.get_total_deposit_in_summary()
		print('total Saldo tokopedia Anda adalah: ' + deposit_summary)
		usable_deposit_summary = deposit.get_usable_deposit_in_summary()
		print('Saldo Tokopedia yang dapat Anda tarik sebesar: ' + usable_deposit_summary)
		print('List of Deposit Transaction')
		print('')
		try:
			activity_list = deposit.get_deposit_activity_list()
			print(activity_list)
			n = 1
			for i in activity_list:
				print('Transaksi ke-' + str(n))
				transaction_datetime = deposit.get_activity_datetime()
				print('Waktu dan Tanggal Transaksi : ' + str(transaction_datetime))
				activity_name = deposit.get_activity_name()
				print('Aktivitas Transaksi : ' + str(activity_name))
				invoice = deposit.get_invoice()
				print('Invoice : ' + str(invoice))
				transaction_nominal = deposit.get_transaction_nominal()
				print('Nominal Transaksi : ' + str(transaction_nominal))
				deposit_per_activity = deposit.get_deposit_per_activity()
				print('Saldo per Aktivitas Transaksi : ' + str(deposit_per_activity))
				print('\n')
				n+=1
		except:
			print('Tidak ada aktivitas deposit')
