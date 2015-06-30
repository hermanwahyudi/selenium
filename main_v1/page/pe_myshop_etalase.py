#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base import BasePage
from random import randint
import os, sys, time

class MyshopEtalasePage(BasePage):
	
	# instance variable
	_pl_page = "myshop-etalase.pl"
	_btn_add_loc = (By.XPATH, "//*[@id='btn-section']")
	_ename_loc = (By.XPATH, "//*[@id='e-name']")
	_submit_loc = (By.CSS_SELECTOR, "button.btn-action")
	_link_edit_loc = (By.CSS_SELECTOR, "a.edit-etalase")
	_link_delete_loc = (By.CSS_SELECTOR, "a.delete-etalase")
	_src_drag_loc = (By.CSS_SELECTOR, "i.icon-move")
	_dst_drag_loc = (By.CSS_SELECTOR, "li.li-711848")
	_submit_del_loc = (By.XPATH, "//button[@name='submit']")

	# test case input
	list_in = ['', 'a', 'ما تم تؤكل', '什么被吃掉', 'វបានគេបរិភោគ', '131231']

	# dictionary url
	dict_url = {
		"url_1" : "https://www.tokopedia.com/",
		"url_2" : "https://test.tokopedia.nginx/",
		"url_3" : "https://www.tokopedia.dev/"
	}

	def go(self):
		self.driver.get(self.dict_url["url_1"] + self._pl_page)
		time.sleep(3)

	def do_validation(self):
		try:
			for i in range(2):
				for x in self.list_in:
					if i == 0:
						self.add_etalase(x)
					elif i == 1:
						self.edit_etalase(x)
					time.sleep(1)
					self.driver.refresh()
		except Exception as inst:
			print(inst)
	def act_n_times(self, flag, N):
		try:
			print("Action " + str(flag) + " " + str(N) + " kali.")
			i = 0
			while(i < N):
				r = self.list_in[randint(0, len(self.list_in)-1)]
				if(flag == "add"):
					self.add_etalase(r)
					print("Tambah Etalase ke-"+str(i+1))
				if(flag == "edit"):
					self.edit_etalase(r)
					print("Edit Etalase ke-"+str(i+1))
				if(flag == "delete"):
					self.delete_etalase()
					print("Hapus Etalase ke-"+str(i+1))
				self.driver.refresh()
				i += 1
		except Exception as inst:
			print(inst)

	def drag_etalase(self):
		try :
			print("Drag and Drop")
			time.sleep(2)
			src = self.driver.find_element(*self._src_drag_loc)
			dst = self.driver.find_element(*self._dst_drag_loc)
			ActionChains(self.driver).drag_and_drop(src, dst).perform()
		except Exception as inst:
			print(inst)

	def add_etalase(self, input1):
		try:
			time.sleep(1)
			self.driver.find_element(*self._btn_add_loc).click()
			time.sleep(2)
			self.driver.find_element(*self._ename_loc).send_keys(input1)
			self.driver.find_element(*self._submit_loc).click()
		except Exception as inst:
			print(inst)
			
	def edit_etalase(self, input1):
		try:
			time.sleep(1)
			self.driver.find_element(*self._link_edit_loc).click()
			time.sleep(2)
			self.driver.find_element(*self._ename_loc).clear()
			self.driver.find_element(*self._ename_loc).send_keys(input1)
			self.driver.find_element(*self._submit_loc).click()
		except Exception as inst:
			print(inst)

	def delete_etalase(self, N):
		try:
			time.sleep(1)
			self.driver.find_element(*self._link_delete_loc).click()
			time.sleep(1)
			self.driver.find_element(*self._submit_del_loc).click()
		except Exception as inst:
			print(inst)

	def __str__(self):
		return "Page " + self.driver.title