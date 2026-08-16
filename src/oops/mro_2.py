class A:
    def greet(self):
        print("A's greet")

class B:
    pass

class C(B,A):   # diamond: D → B → A, D → C → A
    def greet(self):
        super().greet()
        print("C's greet")

obj = C()
obj.greet()
