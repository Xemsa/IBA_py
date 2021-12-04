#10.2
#pizza

class PizzaError(Exception):
   def __init__(self, pizza='uncknown', message = ''):
      self.pizza = pizza
      Exception.__init__(self, message)

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uncknown', cheese = '>100', message=''):
        self.cheese = cheese
        PizzaError.__init__(self, pizza, message)


class Calzone_Error(PizzaError):
    def __init__(self, pizza='uncknown', message=''):
        self.message = message
        PizzaError.__init__(self, pizza, message)

        
class Pizza():
    def __init__(self, pizza=[]):
        self.__pizza_menu = pizza

    def check_pizza(self, pizza, cheese):
        if pizza not in  self.__pizza_menu: 
            raise PizzaError(pizza, "no such pizza in menu") 
        if cheese > 100:
            raise  TooMuchCheeseError(pizza, cheese, "too much cheese")
        if pizza == 'calzone':
            raise Calzone_Error(pizza=pizza , message='calzone is not a pizza')
        return True

    def make_pizza(self, pizza, cheese):
        if self.check_pizza(pizza, cheese):
            print("Pizza ready!") 
    

pizza_obj = Pizza(['margherita','capricciosa','calzone','pepperoni'])

for (pz, ch) in [('calzone', 0),('pepperoni', 90),('margherita', 110), ('mafia', 20)]:
    try:
        pizza_obj.make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese,)
    except Calzone_Error as cal:
        print(cal.message)
    except PizzaError  as  pe:
        print(pe.pizza,"- ", pe)