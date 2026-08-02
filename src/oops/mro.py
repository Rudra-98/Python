class A:
    def greet(self):
        print("A's greet")

class B(A):
    def greet(self):
        print("B's greet")

class C(A):
    def greet(self):
        print("C's greet")

class D(B, C):   # diamond: D → B → A, D → C → A
    pass

obj = D()
obj.greet()
print(D.__mro__)




class A:
    def greet(self):
        print("A's greet")

class B(A):
    def greet(self):
        print("B's greet")
        super().greet()   # calls next in MRO, not necessarily "A" specifically

class C(A):
    def greet(self):
        print("C's greet")
        super().greet()

class D(B, C):
    def greet(self):
        print("D's greet")
        super().greet()

D().greet()


