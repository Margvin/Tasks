#   Условие
#   С начала суток прошло H часов, M минут, S секунд (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). По данным числам H, M, S
#   определите угол (в градусах), на который повернулаcь часовая стрелка с начала суток и выведите его в виде
#   действительного числа.

#   Импорт
import math

#   Получаем данные
H = int(input())
M = int(input())
S = int(input())

#   Выдаем ответ
print(H * 30 + M / 2 + S * 0.0083333)
