#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import os, time, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/'))

class addProduct():
	
	
	# dictionary
	dict = {
		"index_url" : "http://www.tokopedia.com/",
		"email" : "tkpd.qc+18@gmail.com",
		"password" : "imtokopedia91"
	}

	def __init__(self, payment):
		self.browser = webdriver.Chrome("chromedriver")
		self.payment = payment
	
	def open(self, url):
		self.browser.get(url)
		time.sleep(2)

	def do_login(self):
		try:
			self.browser.find_element_by_link_text("Masuk").click()
			self.browser.find_element_by_name("email").send_keys(self.dict['email'])
			self.browser.find_element_by_name("pwd").send_keys(self.dict['password'])
			self.browser.find_element_by_class_name("btn-login-top").click()
			self.browser.implicitly_wait(5)
		except Exception as inst:
			print(inst)

	def go_to_add(self):
		self.open(self.dict['index_url'] + 'product-add.pl')
	
	def add_to_product(self):
		self.go_to_add()
		try:
			self.browser.find_element(By.ID, "p-name").send_keys("Product AB")
			self.choose_category()
			
		except Exception as inst:
			print(inst)
		
	def choose_category(self):
		try:
			self.browser.execute_script("document.getElementById('p-dep-1').style.display = '';")
			time.sleep(4)
			list_category_first = self.browser.find_elements(By.XPATH, "//select[@id='p-dep-1']/option")
			print (list_category_first)
			i = 0
			while i < len(list_category_first):
				if i == 6:
					list_category_first[i].click()
					break
				i += 1
				print (list_category_first[i].get_attribute('value'))
			time.sleep(1)
		except Exception as inst:
			print(inst)



# main
if(__name__ == "__main__"):
	obj = addProduct("Product")
	obj.open(obj.dict['index_url'])
	obj.do_login()
	obj.go_to_add()
	obj.add_to_product()
	i = 0
	while i < 20: 

		i += 1