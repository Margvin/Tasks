#   Условие
#   Дано натуральное число. Найдите число десятков в его десятичной записи.

#   Импорт
import math

#   Получаем данные
h = int(input())

#   Выдаем ответ
print((h // 10) % 10)
