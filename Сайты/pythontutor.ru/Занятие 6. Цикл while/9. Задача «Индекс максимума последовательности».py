#   Условие
#   Последовательность состоит из натуральных чисел и завершается числом 0. Определите индекс наибольшего элемента
#   последовательности. Если наибольших элементов несколько, выведите индекс первого из них. Нумерация элементов
#   начинается с нуля.

#   Получаем данные
x = int(input())

#   Выдаем ответ
z = 0
c = 0
a = 0
while x != 0:

    if x > z:
        z = x
        c = a
    x = int(input())
    a += 1
print(c)
