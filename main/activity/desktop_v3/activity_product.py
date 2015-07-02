__author__ = 'QC1'

import os, time, sys
from main.page.desktop_v3.inbox_price_alert.pe_inbox_price_alert import *
from main.page.desktop_v3.shop.pe_shop import *
from main.page.desktop_v3.product.pe_product import *
from main.page.desktop_v3.index.pe_index import *
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

class ProductActivity():

	def setObject(self, driver):
		self.inbox_price_alert = PriceAlertPage(driver)
		self.shop = ShopPage(driver)
		self.product = ProductPage(driver)
		self.index = IndexPage(driver)

	def edit_product_price(self, driver, site, domain):
		shop_page = ShopPage(driver)
		prod = ProductPage(driver)

		print("Heading toward the destination domain at: ", site, domain)
		shop_page.domain(site, domain)
		shop_page.choose_product_manual("Samsung Galaxy S4")
		time.sleep(3)
		prod.edit_price_product()

	def move_product_to_warehouse(self, site, domain):
		#self.index.click_shop_name_at_panel_left()
		self.shop.domain(site, domain)
		self.shop.choose_product()
		time.sleep(1)
		self.product.click_move_to_warehouse_button()
		time.sleep(1)
		self.product.click_move_to_warehouse_submit_button()
		time.sleep(5)
		print('Checking element visibility ...')
		other_product = self.product.is_other_product_in_etalase_visible()
		dink_it_button = self.product.is_dink_it_button_visible()
		dink_it_ads = self.product.is_check_dink_it_ads_visible()
		move_to_warehouse_button = self.product.is_move_to_warehouse_button_visible()
		move_to_etalase_button = self.product.is_move_to_etalase_button_visible()
		if other_product==0 and dink_it_button==0 and dink_it_ads==0 and move_to_warehouse_button==0 and move_to_etalase_button==1:
			print('Product is successfully moved to warehouse')
		else:
			raise('Some elements are missing, or product is not moved to warehouse')


	def move_product_to_etalase(self, site, domain):
		self.product.domain(site, domain)
		self.product.go_to_warehouse()
		time.sleep(2)
		self.product.choose_product_in_warehouse()
		time.sleep(3)
		self.product.click_move_to_etalase_button()
		time.sleep(2)
		self.product.choose_etalase()
		self.product.click_move_to_etalase_submit_button()
		time.sleep(4)
		print('Checking element visibility ...')
		other_product = self.product.is_other_product_in_etalase_visible()
		dink_it_button = self.product.is_dink_it_button_visible()
		dink_it_ads = self.product.is_check_dink_it_ads_visible()
		move_to_warehouse_button = self.product.is_move_to_warehouse_button_visible()
		move_to_etalase_button = self.product.is_move_to_etalase_button_visible()
		if other_product==1 and dink_it_button==1 and dink_it_ads==1 and move_to_warehouse_button==1 and move_to_etalase_button==0:
			print('Product is successfully moved to etalase')
		else:
			raise('Some elements are missing, or product is not moved to etalase')


	def is_talk_deleted_from_product(self, talk_ID):
		self.product.go_to_talk()
		isTalkFound = self.product.search_talk_ID_in_list(talk_ID)
		if isTalkFound == 1:
			raise('ERROR! Talk[' + talk_ID + '] is not deleted from product after deletion from inbox')
		elif isTalkFound == 0:
			print('Talk[' + talk_ID + '] is successfully deleted from product after deletion from inbox')