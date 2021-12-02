class Person:
  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age

  def get_name(self):
    return f'Surname: {self.surname}, Name: {self.name}'

if __name__ == '__main__':
  person = Person('Bob', 'Morrel', 22)
  print(person.name)
  print(person.surname)
  print(person.age)
  print(person.get_name())