# Написать функцию break_camel_case, которая разбивает слова написанные CamelCase,
# используя в качестве разделителя пробел
#
# Примеры:
# break_camel_case("BreakCamelCase") ==> "Break Camel Case"

import traceback


def break_camel_case(str):
  # Тело функции

  words = [[str[0]]]

  

  for c in str[1:]:

      if words[-1][-1].islower() and c.isupper():

          words.append(list(c))

      else:

          words[-1].append(c)

  r = [''.join(word) for word in words]
  res = ' '.join(x for x in r)

  return res


# Тесты
try:
    assert break_camel_case("BreakCamelCase") == "Break Camel Case"
    assert break_camel_case("helloWorld") ==  "hello World"
    assert break_camel_case("helloWorld BreakCamelCase") == "hello World Break Camel Case"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
