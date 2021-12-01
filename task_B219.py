# Написать функцию century, которая получает получает на вход год и возвращает к какому веку этот год относится. 
# Окончания согласно правилам английского языка.
#
# Примеры:
# century("1999") ==> "20th"
# century("2011") ==> "21st"


import traceback


def century(year):
    # Тело функции
    a = int(year)
    b= str(int(a/100) + 1) + 'st'
    return b


# Тесты
try:
    assert century("2011") == "21st"
    assert century("2154") == "22nd"
    assert century("2259") == "23rd"
    assert century("1234") == "13th"
    assert century("1023") == "11th"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
