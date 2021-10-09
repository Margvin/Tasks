#   Условие
#   Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
#   ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
#   Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг
#   друга, выведите слово NO, иначе выведите YES.

#   Выдаем ответ
s = []
x = []
y = []
for i in range(8):
    a = input().split()
    for j in range(2):
        s.append(a[j])
for i in range(len(s)):
    s[i] = int(s[i])
for i in range(0, len(s), 2):
    x.append(s[i])
for i in range(1, len(s) + 1, 2):
    y.append(s[i])
o = 'NO'
if o != 'YES':
    for i in range(8):
        if x.count(x[i]) > 1:
            o = 'YES'
        if y.count(y[i]) > 1:
            o = 'YES'
if o != 'YES':
    for i in range(8):
        for j in range(i, 8):
            if i != j:
                if x[i] - y[i] == x[j] - y[j]:
                    o = 'YES'
if o != 'YES':
    for i in range(8):
        for j in range(i, 8):
            if i != j:
                if x[i] + y[i] == x[j] + y[j]:
                    o = 'YES'
print(o)
