#   Условие
#   Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из
#   моментов времени. Известно, что второй момент времени наступил не раньше первого. Определите, сколько секунд прошло
#   между двумя моментами времени.

#   Программа на вход получает три целых числа: часы, минуты, секунды, задающие первый момент времени и три целых числа,
#   задающих второй момент времени.

#   ыведите число секунд между этими моментами времени.

#   Импорт
import math

#   Получаем данные
c1 = int(input())
m1 = int(input())
s1 = int(input())
c2 = int(input())
m2 = int(input())
s2 = int(input())

#   Выдаем ответ
print(abs((c1 * 3600 + m1 * 60 + s1) - (c2 * 3600 + m2 * 60 + s2)))
