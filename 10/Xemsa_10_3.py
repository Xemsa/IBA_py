#10.3
#Weeker
class WeekDayError(Exception):
    def __init__(self, day="", message="не в силах"):
        self.message=message
        self.day = str(day)
        super().__init__(self)

class Weeker:
    def __init__(self,day) -> None:
        self.__alldl = ['Sun','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        self.__alldd = {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}
        if day not in self.__alldl:
            raise WeekDayError(day,"не в силах понять день")
        self.__dayn = self.__alldd[day]
        self.__day = self.__alldl[self.__dayn]

    def __str__(self) -> str:
        self.__day = self.__alldl[self.__dayn]
        return  str(self.__day)
        
    def add_days(self, days):
        if days < 0:
            self.subtract_days(days*(-1))
        else:        
            self.__dayn = (self.__dayn + days) % 7
            if self.__dayn == 0:
                self.__dayn = 7

    def subtract_days(self, days):
        self.__dayn = (self.__dayn - days) % 7
        if self.__dayn == 0:
            self.__dayn = 7


try:
    wd=Weeker('Mon')
    print(wd)
    wd.add_days(11)
    print(wd)
    wd.subtract_days(3)
    print(wd)
    wd=Weeker('Monday')
except WeekDayError as wde:
    print(wde.message + ": " + wde.day)
