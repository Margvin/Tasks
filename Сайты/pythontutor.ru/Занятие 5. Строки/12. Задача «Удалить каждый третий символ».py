#   Условие
#   Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

#   Получаем данные
s = input()

#   Выдаем ответ
l = len(s)
for i in range(0, l):
    if i % 3 == 0:
        print(s[i].replace(s[i], ''), sep='', end='')
    else:
        print(s[i], sep='', end='')
