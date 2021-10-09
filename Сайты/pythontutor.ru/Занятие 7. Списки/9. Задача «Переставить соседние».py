#   Условие
#   Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то последний
#   элемент остается на своем месте.

#   Получаем данные
a = input().split()

#   Выдаем ответ
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(0, len(a), 2):
    if i < len(a) - 1:
        a[i], a[i + 1] = a[i + 1], a[i]
for i in range(len(a)):
    print(a[i], end=' ')
