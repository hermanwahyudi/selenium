from utils.lib.balance_info import *

class Environment(object):
    def __init__(self,environment=""):
        self.current_environment = environment

    def getEnv(self):
        return self.current_environment

    def setEnv(self,environment):
        self.current_environment = environment



class User(object):
    def __init__(self,username="", user_id="", default_bank="",phone=""):
        self.username = username
        self.user_id = user_id
        self.default_bank = default_bank
        self.phone_number = phone

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getUserID(self):
        return self.user_id

    def setUserID(self, user_id):
        self.user_id = user_id

    def getDeposit(self):
        print("My current Deposit Amount : %s " %(self.balance))
        return self.balance

    def setDeposit(self, balance):
        self.balance = balance

    def setDefaultBankAccount(self, default_bank):
        self.default_bank = default_bank

    def getDefaultBankAccount(self):
        return self.default_bank

    def setPhone(self, phone_number):
        self.phone_number = phone_number

    def getPhone(self):
        return self.phone_number




