#   Условие
#   В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

#   Получаем данные
a = input().split()

#   Выдаем ответ
for i in range(len(a)):
    a[i] = int(a[i])
min = a.index(min(a))
max = a.index(max(a))
a[max], a[min] = a[min], a[max]

for i in range(len(a)):
    print(a[i], end=' ')
