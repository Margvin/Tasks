#   Условие
#   Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

#   Получаем данные
n = int(input())

#   Выдаем ответ
z = 2
while z <= n:
    if n % z == 0:
        print(z)
        z = n + 1
    z += 1
