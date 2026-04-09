#Encapsulation is the concept of wrapping data and methods together as a single unit. It restricts direct access to some of the objects components.

#with getter and setter

#public , protected and private


class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner          # public — fine to read/write
        self._balance = balance     # protected — use via methods ideally
        self.__pin = pin            # private — internal only

    def return_pin(self):
        return self.__pin

    def verify_pin(self, entered):
        return entered == self.__pin  # accessible inside the class

class SavingsAccount(BankAccount):
    def show_balance(self):
        return self._balance        # protected: accessible in subclass
        # self.__pin would FAIL here — name mangling blocks it

acc = BankAccount("Alice", 1000, 9999)

sav_acc = SavingsAccount("Bob", 1000, 9999)


print(sav_acc.owner)

print(sav_acc.show_balance())

print(acc.owner)        # Works fine
print(acc._balance)
#
# print(acc.__pin)# Works, but discouraged
# # print(acc.verify_pin(9999))            # AttributeError!
# print(acc._BankAccount__pin)


print(acc.return_pin())# Works (but don't do this)



