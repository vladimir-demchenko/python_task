# Написать функцию palindrom, которая определяет является ли заданное число палиндромом
# (читается одинаково слева направо и справа налево)
#
# Пример:
# palindrom(1234321) ==> True

import traceback


def palindrom(number):
    number = str(number) # преобразуем входящее число в строку, чтобы можно было ее удобно развернуть
    reverse_number = number[::-1] # разворачиваем полученную строку через срез
    if number == reverse_number: # проверям сходятся ли данное число и перевернутое
        return True
    else:
        return False


# Тесты
try:
    assert palindrom(0) == True
    assert palindrom(1233221) == False
    assert palindrom(1000010) == False
    assert palindrom(5555555) == True
    assert palindrom(1234554321) == True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
