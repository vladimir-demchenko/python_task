# Написать функцию ips_between(start, end), которая возвращает
# количество ip адресов, начиная с start и до end, не считая его.
# Start и end представляют собой список из четырех целых чисел, например [10, 0, 0, 50]


import traceback

def ipToInt(ip):
    a, b, c, d = ip
    return (((((a << 8) + b) << 8) + c) << 8) + d

def ips_between(start, end):
    # Тело функции
    return ipToInt(end) - ipToInt(start)


# Тесты
try:
    assert ips_between([10, 0, 0, 0], [10, 0, 0, 50]) == 50
    assert ips_between([20, 0, 0, 10], [20, 0, 1, 0]) == 246
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
