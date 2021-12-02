from person import Person

class Cook:
  def __init__(self,name, surname, age, specialization, dishes):
    Person.__init__(self,name,surname,age)
    self.specialization = specialization
    self.dishes = dishes
  
  def add_dishes(self, param, values):
    self.dishes[param] = values
 
  def change(self, param, values):
    if param in self.specialization:
        self.specialization[param] = values
    else:
        print( 'Not param')
 
  def del_dishes(self, param):
    try:
        del self.dishes[param]
    except:
        print( 'Error, Not param')
  
   def __str__(self):
         return f"{self.get_name()}\nage: {self.age},\
specialization: {self.specialization}"
 