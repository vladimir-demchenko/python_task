# Создать список (библиотека книг), состоящий из словарей (книги). Словари должны содержать как минимум 5 полей
# (например, номер, название, год издания...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# library = [{"id" : 123456, "title" : "Война и мир", "author" : "Толстой",...} , {...}, {...}, ...]
# Реализовать функции:
# – вывода информации о всех книгах;
# – вывода информации о книге по введенному с клавиатуры номеру;
# – вывода количества книг, старше введённого года;
# – обновлении всей информации о книге по введенному номеру;
# – удалении книги по номеру.
# Провести тестирование функций.
library = [{"id": 123456, "title": "Война и мир", "author": "Толстой", "year": "1888", "binding": "Жесткий"},
{"id": 123457, "title": "Война и мир", "author": "Толстой", "year": "Книжка", "binding": "Мягкий"},
{"id": 123458, "title": "Сказки", "author": "Сказочник", "year": "1919", "binding": "Жесткий"},
{"id": 123454, "title": "Водичка", "author": "Родничков", "year": "1999", "binding": "Жесткий"},
{"id": 123455, "title": "Линейка и кривинейка", "author": "Мистер Пи", "year": "2000", "binding": "Жесткий"},
{"id": 123479, "title": "Эй ты кто такой?", "author": "Давайдосвидания", "year": "2000", "binding": "Жесткий"},
{"id": 123459, "title": "Война и мир", "author": "Непростой", "year": "1777", "binding": "Жесткий"},
{"id": 123466, "title": "Война и рим", "author": "Толстой", "year": "1899", "binding": "Жесткий"},
{"id": 123467, "title": "Коза", "author": "Козёл", "year": "1987", "binding": "Мягкий"},
{"id": 123465, "title": "Ай фон", "author": "Андройд", "year": "1988", "binding": "Жесткий"}]
 
 
 
def marketAll(): 
 [[print(i, _.get(i)) for i in _.keys()] for _ in library] 
 
 
def marketID(): 
 a = int(input('Введите ID: ')) 
 for i in library: 
  if i['id'] == a: 
    [print(_, i.get(_)) for _ in i.keys()] 
 
 
def department(): 
 a = str(input('Введите год: ')) 
 b = 0 
 for i in library: 
  if i['year'] == a: 
    b = b + 1 
 print(b) 
 
 
def updateProduct(): 
 a = int(input('Введите ID книги, который хотите изменить: ')) 
 for i in library: 
  if i['id'] == a: 
    name = str(input("Введите новое название: ")) 
    departmentName = str(input("Введите автора: ")) 
    priseName = str(input("Введите год: ")) 
    dataName = str(input("Введите переплет: ")) 
    i2 = {"id": i['id'], "title": name, "author": departmentName, "year": priseName, "binding": dataName} 
    i.update(i2) 
 [print(_, i.get(_)) for _ in i.keys()] 

def popByNums(id,lib):
    for i, book in enumerate(lib):
        if id == book['id']:
            lib.pop(i)
            return lib
marketAll()
marketID()
department()
updateProduct()
x_in = int(input())
print(popByNums(x_in,library))
