import re

regex = r'((?:(?:https?|ftp):\/\/){0,1}(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z0-9]+-?)*[a-z0-9]+)(?:\.(?:[a-z0-9]+-?)*[a-z0-9]+)*(?:\.(?:[a-z]{2,})))(?::\d{2,5})?(?:\/[^\s]*)?)'
flags = re.IGNORECASE

def link(x):
	test = re.findall(regex, x, flags)
	return(test)


def pattern_match(x):
	test2 = re.match(regex, x, flags)
	return(test2)

def is_link_in_whitelist(link, file_whitelist):
	word_clean = re.sub('[.]+', '', link)
	status = 0
	for j in file_whitelist:
		whitelist_ignorecase = j.lower()
		if whitelist_ignorecase in word_clean: #case whitelist
			status = 1 #true
			break
		else:
			pass
	return(status)
	
def is_link_in_blacklist(link, file_blacklist):
	domains = re.findall("(\.[A-Za-z]+)", link)
	status = 0
	for i in domains:
		for j in file_blacklist:
			blacklist_ignorecase = '.' + j.lower()
			if i==blacklist_ignorecase:
				status = 1 #true
				break
			else:
				pass
	return(status)

def check_if_link_censored(sent_message, received_message, file_blacklist, file_whitelist):
	flags = re.IGNORECASE
	if len(sent_message) ==  len(received_message):
		for word in sent_message:
			if pattern_match(word): #there word is link
				word_ignorecase = word.lower()
				wl = is_link_in_whitelist(word_ignorecase, file_whitelist)
				bl = is_link_in_blacklist(word_ignorecase, file_blacklist)
				if wl == 0 and bl == 0 : #not in white/blacklist
					idx = sent_message.index(word)
					if sent_message[idx]==word and received_message[idx]==word:
						print('Link tertangkap: ' + sent_message[idx])
						print('message diterima: ' + received_message[idx])
						print('Link is not censored\n')
					else:
						print('Link tertangkap: ' + sent_message[idx])
						print('message diterima: ' + received_message[idx])
						raise Exception('ERROR: The link must not be censored.')
				elif wl == 0 and bl == 1:
					idx = sent_message.index(word)
					censored_msg = link(sent_message[idx])[0]
					if sent_message[idx]==word and '[LINK]' in received_message[idx]: #true case
						print('Link tertangkap: ' + sent_message[idx])
						print('message diterima: ' + received_message[idx])
						print('Link censored: ' + censored_msg)
						print('Link is censored\n')     
					else: #if the domain is in blackist, but not converted to [LINK]
						print('Link tertangkap: ' + sent_message[idx])
						print('message diterima: ' + received_message[idx])
						print('Link censored: ' + censored_msg)
						raise Exception('ERROR: The link must be censored.')
				else:   
					idx = sent_message.index(word)
					if sent_message[idx]==word and received_message[idx]==word:
						print('Link tertangkap: ' + sent_message[idx])
						print('message diterima: ' + received_message[idx])
						print('Link is in whitelist\n')
					else:
						print('Link tertangkap: ' + sent_message[idx])
						print('message diterima: ' + received_message[idx])
						raise Exception('ERROR: The link must not be censored.')
			else:
				pass
	else:
		raise Exception('ERROR: Content of received message is different from sent message')