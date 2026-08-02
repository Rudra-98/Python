class BankAccount:
    def __init__(self):
        self.name = 'chandu'



class SavingsAccount(BankAccount):
    def get_balance(self):
        print(self.name)
        return 10000



obj = BankAccount()

s_obj = SavingsAccount()

print(s_obj.get_balance())


print(obj.name) ## private
