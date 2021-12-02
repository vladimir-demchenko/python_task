from waiter import Waiter
from cook import Cook

class Cafe:
  def __init__(self,name,address, lst_waiters = [], lst_cooks = []):
        self.name = name
        self.address = address
        self.waiter = lst_waiters
        self.cook = lst_cooks
 
    def waiters(self):
        return len(self.lst_waiters)
    
    def cooks(self):
      return len(self.lst_cooks)

    def get_employees(self, index):
      try:
          return self.lst_waiters[index], self.lst_cooks[index]
      except:
          return 'Not employees'
 
    def __str__(self):
        a = '\n'.join([f'{str(waiter)}\n{str(waiter.receipt)}' for waiter in self.waiter])
        b = '\n'.join([f'{str(cook)}\n{str(cook.dishes)}' for cook in self.cook])
        return f"Name: {self.name}\nAddres: {self.address}\nWaiter :\n{a}\nCook :\n{b}\n"

    def create_txt(self, filename): 
      f = open(filename, 'w') 
      f.write(self.__str__()) 
      f.close()        