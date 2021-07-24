#   Условие
#   Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы в
#   этот момент. Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
#   Учтите, что число n может быть больше, чем количество минут в сутках.

#   Получаем кол-во минут
n = int(input())

#   Вычисляем минуты и часы
Chas = (n // 60) % 24
Min = n % 60

#   Выдаем ответ
print(Chas, Min)