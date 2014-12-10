from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By

class SendMessageShop:
	def __init__(self):
		self.browser = webdriver.Firefox()
		self.browser.get("https://tokopedia.dev/")
		self.doLogin()
	
	def doLogin(self):
		self.browser.find_element_by_link_text("Masuk").click()
		self.browser.find_element_by_name("email").send_keys("tkpd.qc+13@gmail.com")
		self.browser.find_element_by_name("pwd").send_keys("rubikholic19")
		self.browser.find_element_by_class_name("btn-login-top").click()

	def sendMsg(self):
		self.browser.get("https://tokopedia.dev/tokoqc15")
		i = 0
		while i < 1000:
			rand01 = randint(10000000, 99999999)
			rand02 = randint(10000000000, 100000000000)
			self.browser.implicitly_wait(1)
			self.browser.find_element_by_id("s_send_pm").click()
			self.browser.find_element_by_id("message-subject").send_keys(rand01)
			self.browser.find_element_by_id("message").send_keys(rand02)
			self.browser.find_element(By.XPATH, '//button[text()="Kirim"]').click()
			self.browser.refresh()
			i += 1 

# main

if(__name__ == "__main__"):
	 obj = SendMessageShop()
	 obj.sendMsg()
	 
	 # obj.deleteEtalase()