#   Условие
#   Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

#   Получаем данные
a = input().split()

#   Выдаем ответ
for i in range(1, len(a)):
    if int(a[i]) > int(a[i - 1]):
        print(a[i], end=' ')
