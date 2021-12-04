#10.1
#Queue

class QueueError(Exception):
    def __init__(self, mes="очередь пуста"):
        self.mes=mes
        super().__init__(self, self.mes)
   
class Queue:
    def __init__(self):
        self.__quy = []
    
    def put(self, val):
        self.__quy.insert(0,val)
    
    def get(self):
        if self.__quy != []:
            val = self.__quy[-1]
            del self.__quy[-1]
            return val
        else:
            raise QueueError("Очередь пуста")

q=Queue()
q.put(1)
q.put('dog')
q.put(False)
try:
    for i in range(4):
        print(q.get())
except QueueError as qe:
    print(qe.mes)
    print("Queue error")