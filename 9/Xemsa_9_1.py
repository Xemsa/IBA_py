#9.1
#__counter = 0

class Stack:
    def __init__(self):
        self.__stk = []
    
    def push(self, val):
        self.__stk.append(val)
    
    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

class CountStack(Stack):
    def __init__(self):
        super().__init__()
        self.__counter=0
    
    def get_counter(self):
        return self.__counter

    def pop(self):
        self.__counter+=1
        return super().pop()

stk = CountStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())