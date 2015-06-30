

class BalanceStatus(object):
    def __init__(self, balance):
        balance = balance.replace("Rp", "")
        balance = balance.replace(".", "")
        balance = balance.strip()
        self.balance = balance

