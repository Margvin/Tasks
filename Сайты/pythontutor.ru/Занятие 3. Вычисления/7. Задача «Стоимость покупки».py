#   Условие
#   Пирожок в столовой стоит a рублей и b копеек. Определите, сколько рублей и копеек нужно заплатить за n пирожков.
#   Программа получает на вход три числа: a, b, n, и должна вывести два числа: стоимость покупки в рублях и копейках.

#   Импорт
import math

#   Получаем данные
a = int(input())
b = int(input())
n = int(input())

#   Выдаем ответ
print(str(a * n + (b * n) // 100), str((b * n) % 100))
