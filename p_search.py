from selenium import webdriver
from random import randint

class Search:
	def __init__(self):
		self.browser = webdriver.Firefox()
		self.browser.get("https://tokopedia.com/")
	
	def searchTkpd(self, sesuatu):
		for i in range(100):
			self.browser.find_element_by_name("search_keyword").send_keys(sesuatu)
			self.browser.find_element_by_css_selector("button.btn-search").click()
			self.browser.find_element_by_id("tab-shop").click()
			self.browser.get("https://tokopedia.com/")
# main

if(__name__ == "__main__"):
	obj = Search()
	obj.searchTkpd(randint(10000000, 100000000))
