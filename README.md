# WebDriver with Python

# Test Unit
----------
1. test_login : 
	a. test user untuk login (normal)
	b. test user untuk check validasi login -> input kosong(empty)
	c. test user untuk check validasi input email 
	d. test user untuk check validasi input password

2. test_reject_order :
	a. test untuk reject order -> single/multiple reject order


# Class
------
1. Login
2. Register
3. Inbox Message
4. Inbox Review
5. Inbox Talk
6. Myshop Order (Penjualan)
7. Tx Payment (Pembelian)


# Function
--------
di Base.py
1. get_page_loadtime -> fungsi untuk mengakses suatu halaman dan juga waktu proses loadtime nya

2. _click -> fungsi klik . memanggil fungsi 'timestamp'

3. check_visible_element -> fungsi untuk melakukan check kemunculan suatu element yang diinginkan. memanggil fungsi 'wait_visible_element'

4. click_on_javascript -> fungsi untuk melakukan klik suatu javascript. (masih percobaan)

5. mouse_hover_to -> fungsi untuk hover mouse ke element yang diinginkan.

6. find_element -> fungsi untuk cari element

7. find_elements -> fungsi untuk cari beberapa element (berupa list)


di main/function/general.py
1. wait_visible_element -> fungsi untuk menunggu sampai element yang diinginkan muncul.

2. timestamp_print -> fungsi untuk log print, dengan akses menggunakan get URL

3. timestamp_print_verify_url -> fungsi untuk log print, dengan akses menggunakan click URL


di main/function/driver.py
1. useDriver(args) -> fungsi untuk memanggil driver yang akan digunakan , masukkan "firefox"/"chrome" / "phantomjs" pada args
example : self.driver = useDriver("chrome")

# Created by Herman Wahyudi and Team
