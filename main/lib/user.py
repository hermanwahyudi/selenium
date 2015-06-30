from main.lib.balance_info import *


class UserInfo(BalanceStatus):

    def getUsername(self, name):
        self.name = name

    def getDeposit(self):
        print("My current Deposit Amount : %s " %(self.balance))
        return self.balance

    def setDeposit(self, balance):
        self.balance = balance





