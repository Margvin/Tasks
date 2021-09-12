#   Условие
#   Даны три целых числа. Выведите значение наименьшего из них.

#   Получаем данные
a = int(input())
b = int(input())
c = int(input())

#   Выдаем ответ
if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)
