import re
from utils.lib.user_data import *

def split_user_info(current_user):
    regex_type_1 = "^([a-zA-Z0-9]+)\[.+$"
    user_numb = re.findall(regex_type_1, current_user)
    return user_numb

a = user3

#b = "{0}['email']".format(a)
b = a['email']



print (b)
#print (split_user_info())