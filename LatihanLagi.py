from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class LatihanLagi(unittest.TestCase):

	def __init__(self):
		self.driver = webdriver.Chrome("chromedriver")
		self.driver.get("http://localhost/root/Test_Programming/")

	def test_search(self):
		a = self.driver.find_element(By.NAME, "search_posisi")
		for i in a.find_elements_by_tag_name("option"):
			print(i.get_attribute("value"))
		for j in self.driver.find_elements(By.TAG_NAME, "td"):
			print(j.text)
	def test_a(self):
		k = 1
		a = self.driver.find_element_by_tag_name("tbody")
		list1 = a.find_elements(By.TAG_NAME, "tr")
		for i in list1:
			for j in i.find_elements(By.TAG_NAME, "td"):
				print(j.text + str(k))
				k += 1

# main
if(__name__ == "__main__"):
	obj = LatihanLagi()
	#obj.test_search()
	obj.test_a()