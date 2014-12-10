from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By

class SendMessagePeople:
	def __init__(self):
		self.browser = webdriver.Chrome("chromedriver")
		self.browser.get("http://new.tkpdevel-pg.ryandy")
		self.doLogin()
		self.browser.implicitly_wait(1)
	
	def doLogin(self):
		self.browser.find_element_by_link_text("Masuk").click()
		self.browser.find_element_by_name("email").send_keys("razer+02@razer.com")
		self.browser.find_element_by_name("pwd").send_keys("gundam")
		self.browser.find_element_by_class_name("btn-login-top").click()

	def sendMsg(self):
		i = 0
		while i < 100:
			self.browser.get("http://new.tkpdevel-pg.ryandy/people/1385")
			rand01 = randint(10000000, 99999999)
			rand02 = randint(10000000000, 100000000000)
			self.browser.implicitly_wait(1)
			self.browser.find_element_by_id("send-inbox-1385").click()
			self.browser.implicitly_wait(7)
			self.browser.find_element_by_id("message-subject").send_keys(rand01)
			self.browser.find_element_by_id("message").send_keys(rand02)
			self.browser.find_element(By.XPATH, '//button[text()="Kirim"]').click()
			print("Kiriman ke-"+str(i))
			i += 1 

# main

if(__name__ == "__main__"):
	 obj = SendMessagePeople()
	 obj.sendMsg()
	 
	 # obj.deleteEtalase()