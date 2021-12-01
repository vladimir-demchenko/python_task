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
    b= int(a/100) + 1
    if b < 10:
      if b == 1:
        b = str(b) + 'st'
      elif b == 2:
        b = str(b) + 'nd'
      elif b == 3:
        b = str(b) + 'rd'
      else:
        b = str(b) + 'th'
    elif b >= 10 and b < 20:
      b = str(b) + 'th'
    elif b >= 20:
      if b % 10 == 1:
        b = str(b) + 'st'
      elif b % 10 == 2:
        b = str(b) + 'nd'
      elif b % 10 == 3:
        b = str(b) + 'rd'
      else:
        b = str(b) + 'th'
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
