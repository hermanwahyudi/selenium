from main.page.header import *
from main.page.base import *
from selenium import webdriver
from main.page.product.pe_talk_product import *
from main.page.product.pe_product import *
from main.page.shop.pe_shop import *
from main.activity.activity_inbox_talk import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException



class talkProductActivity():


	def setObject(self, driver):
		self.shop = ShopPage(driver)
		self.prod = ProductPage(driver)
		self.talk = TalkProductPage(driver)
		self.inbox = inboxTalkActivity()

	#tulis (mulai) diskusi/talk -- potential buyer
	def test_input_talk(self, driver, site, target_shop, count):
		self.shop.domain(site, target_shop)
		print('Berhasil masuk toko')
		self.shop.choose_product()
		print('Berhasil pilih produk secara random')
		self.prod.go_to_talk() #enter discussion tab
		print('Berhasil masuk tab talk')
		time.sleep(1)
		total_message_old = self.talk.get_jumlah_message()
		print('jumlah talk lama: ' + str(total_message_old))
		self.talk.input_talk(count)
		try:
			"""WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.ajax-loader")))
			print('Loader displayed')
			WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.ajax-loader")))
			print('Exit loader')"""
			total_message_new = self.talk.get_jumlah_message()
			print('jumlah talk baru: ' + str(total_message_new))
			end_of_list = total_message_new - total_message_old
			print(end_of_list)
			list_new_msg = self.talk.list_new_message(end_of_list)
			return(list_new_msg)
		except TimeoutException:
			print ('Loading time too long. Test terminated.')
			return('none')
		except NoSuchElementException:
			print ('Element Not Found. Test terminated.')
			return('none')

	#cek inbox penerima, apakah pesan yang dikirimkan sampai
	def test_if_message_received(self, driver, site, new_ID_message):
		self.inbox.setObject(driver)
		self.inbox.is_message_received(site, new_ID_message)