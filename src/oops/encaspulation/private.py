class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner            # public       -> accessible anywhere
        self._balance = balance       # protected    -> convention: internal use, but still accessible
        self.__pin = "1234"           # private      -> name-mangled, harder to access directly

    def get_balance(self):
        return self._balance

    def _internal_helper(self):
        # meant for internal/subclass use only, by convention
        return f"Processing account for {self.owner}"

    def __validate_pin(self, pin):
        # name-mangled, meant to be truly internal
        return pin == self.__pin

    def withdraw(self, amount, pin):
        if self.__validate_pin(pin) and amount <= self._balance:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        return "Failed: invalid PIN or insufficient funds"


acc = BankAccount("Riya", 1000)

# PUBLIC - works fine, no restriction
print(acc.owner)              # Riya

# PROTECTED - works, but a single underscore is a signal "don't touch this from outside"
print(acc._balance)           # 1000 (accessible, but considered bad practice)

# PRIVATE - this will fail
try:
    print(acc.__pin)
except AttributeError as e:
    print("Error:", e)        # AttributeError: 'BankAccount' object has no attribute '__pin'

# but it's not truly hidden - Python "name-mangles" it to _ClassName__attr
print(acc._BankAccount__pin)  # 1234  <- still technically accessible!

print(acc.withdraw(200, "1234"))   # Withdrew 200. New balance: 800