from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
import time

class Talk:
	def __init__(self):
		self.browser = webdriver.Firefox()
		self.browser.get("https://test.tokopedia.nginx/")
		self.doLogin()
	
	def doLogin(self):
		self.browser.find_element_by_link_text("Masuk").click()
		self.browser.find_element_by_name("email").send_keys("tkpd.qc+13@gmail.com")
		self.browser.find_element_by_name("pwd").send_keys("1234asdf")
		self.browser.find_element_by_class_name("btn-login-top").click()
		self.browser.implicitly_wait(5)

	def inputTalk(self):
		i = 0
		while i < 1000:
			self.browser.get("https://test.tokopedia.nginx/tokoqc14/test-produk/talk")
			rand01 = randint(10000000, 99999999)
			rand02 = randint(10000000000, 100000000000)
			#self.browser.implicitly_wait(5)
			time.sleep(5)
			self.browser.find_element(By.XPATH, "//textarea[@id='']").send_keys("1" + str(rand01) + str(rand02))
			self.browser.find_element(By.XPATH, "//button[text()='Diskusi']").click()
			i += 1 

# main

if(__name__ == "__main__"):
	 obj = Talk()
	 obj.inputTalk()
	 
	 # obj.deleteEtalase()