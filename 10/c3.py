class O:
    def m_O(self):
        print("O")

class A(O):
    def m_A(self):
        print("A")

class B(O):
    def m_A(self):
        print("B")

class C(O):
    def m_A(self):
        print("C")

class D(O):
    def m_A(self):
        print("D")

class E(O):
    def m_A(self):
        print("E")

class K1(A,B,C):
    def m_K(self):
        print("K1")

class K2(D,B,E):
    def m_K(self):
        print("K2")

class K3(A,B,C):
    def m_K(self):
        print("K3")

class Z(K1,K2,K3):
    def m_Z(self):
        print("Z")

def pr(t,nest = 0):
    if nest > 1:
        print(nest)

obj = Z()
obj.m_Z()
obj.m_K()
obj.m_A()
obj.m_O()