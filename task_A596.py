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

library = [{"id": 12,\
            "title" : "В интересах революции",\
            "group" : "Агата Кристи"},\
            {"id": 13,\
            "title": "Серебро",\
            "group":"Би-2"},\
            {"id":14,\
            "title": "Люди на холме",\
            "group":"Наутилус Помпилиус"},\
            {"id": 15,\
            "title" : "Uselink",\
            "group": "Depeche Mode"}]

def listAll(x,lib):
    for i in range(len(library)):
        el = '{},{},{}'\
             .format( lib[i].get('id'),\
                      lib[i].get('title'),\
                      lib[i].get('group') )
        return el

def outByNums(x,lib):
    for i in range(len(library)):
        el_sym = lib[i].get('id')
        if int(x) is el_sym:
            el2 = '{},{},{}'\
                  .format( library[i].get('id'),\
                  lib[i].get('title'),\
                  lib[i].get('group') )
    return el2

def popByNums(id,lib):
    for i, book in enumerate(lib):
        if id == book['id']:
            lib.pop(i)
            return lib

x_in = int(input())
print(popByNums(x_in,library))
