#   Условие
#   Определите среднее значение всех элементов последовательности, завершающейся числом 0.

#   Выдаем ответ
z = 0
x = 1
a = -1
while x != 0:
    x = int(input())
    z += x
    a += 1
print(z / a)
