class A:
    def method(self):
        print("Method in class A")
    
class B(A):
    def method(self):
        print("Method in class B")
        super().method()  # Call the method from class A    

class C(A):
    def method(self):
        print("Method in class C")
        super().method()  # Call the method from class A

class D(B, C):
    pass

d = D()
d.method()
d.mro()