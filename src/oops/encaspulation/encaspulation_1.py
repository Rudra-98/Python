class BankAccount:
    def __init__(self, owner, balance,pin):
        self.owner = owner #public
        self._balance = balance #protected
        self.__pin  = pin #private


    def get_pin(self):
        return self.__pin

class SavingAccount(BankAccount):
    def __init__(self,owner, balance,pin):
        super().__init__(owner, balance,pin)


    def get_balance(self):
        return self._balance


    def print_owner_name(self):
        print(self.owner)



custom = SavingAccount("John",500,"1234")

custom.print_owner_name()

print(custom.get_pin())

print(custom._SavingAccount__pin)









