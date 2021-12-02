from person import Person

class Waiter:
  def __init__(self,name, surname, age, receipt):
    Person.__init__(self,name,surname,age)
    self.receipt = receipt
  
  def add_receipt(self, receipt, value):
    self.receipt[receipt] = value

  def get_receipt(self, receipt):
    try:
        return self.receipt[receipt]
    except:
        return 'Not receipt'
  
  def info_receipt(self):
    print(*[f'{key} {val}' for key, val in self.receipt.items()],sep ='\n')
 
  def __str__(self):
    return f'{self.get_name()}, age: {self.age}'