# Написать функцию missing, которое возвращает пропущенное число в строке (последовательность,
# объединенная в одну строку без пробелов). Если ничего не пропущено - вернуть -1.
#
# Пример:
# missing("123567") ==> 4 (последовательность: 1, 2, 3, 4, 5, 6, 7)
# missing("899091939495") ==> 92 (последовательность: 89, 90, 91, 92, 93, 94, 95)


import traceback


def missing(num):
    n = len(num)
    tm, i, res = '', 0, -1
    while i < n-1:
        tm += num[i]
        tmp = tm
        while  i + len(tmp) < n:
            t1 = int(tmp) + 1
            if num[i+1:].startswith(str(t1)):
                i += len(str(t1))
            elif num[i+1:].startswith(str(t1+1)) and res == -1:
                res = t1
            else:
                res = -1
                i = len(tmp) - 1
                break
            tmp = str(t1)
        i += 1
    return res


# Тесты
try:
    assert missing("123567") == 4
    assert missing("899091939495") == 92
    assert missing("9899101102") == 100
    assert missing("599600601602") == -1
    assert missing("8990919395") == -1
    assert missing("998999100010011003") == 1002
    assert missing("99991000110002") == 10000
    assert missing("979899100101102") == -1
    assert missing("900001900002900004900005900006") == 900003
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
