#   Условие
#   Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания. В этой
#   задаче можно обойтись без инструкции if.

#   Получаем данные
a = int(input())  # Ввели первое число
b = int(input())  # Ввели второе число

#   Выдаем ответ
for i in range(a, b - 1, -1):
    if i % 2 != 0:
        print(i, end=" ")
