#   Условие
#   Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в
#   порядке убывания в противном случае.

#   Получаем данные
a = int(input())  # Ввели первое число
b = int(input())  # Ввели второе число

#   Выдаем ответ
if a < b:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    for i in range(a, b - 1, -1):
        print(i, end=" ")
