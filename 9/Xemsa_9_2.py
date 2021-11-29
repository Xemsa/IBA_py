#9.2
#Timer

class Timer:

    def __init__(self,hours=0,minutes=0,seconds=0):
        self.__hh=hours
        self.__mm=minutes
        self.__ss=seconds
    
    def __str__(self):
        return "{:02}:{:02}:{:02}".format(self.__hh,self.__mm,self.__ss)

    def next_second(self):
        self.__ss += 1
        if self.__ss == 60:
            self.__ss = 0
            self.__mm += 1
            if self.__mm == 60:
                self.__mm = 0
                self.__hh += 1
                if self.__hh == 24:
                    self.__hh = 0

    def prev_second(self):    
        if self.__ss > 0:
            self.__ss -= 1   
        else:
            self.__ss = 59
            if self.__mm > 0:
                self.__mm -=1
            else:
                self.__mm = 59
                if self.__hh > 0:
                    self.__hh -=1
                else:
                    self.__hh = 23

timer = Timer(23,59,59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)