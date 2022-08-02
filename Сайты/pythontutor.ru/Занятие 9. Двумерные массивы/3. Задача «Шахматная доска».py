#   Условие
#   Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном
#   порядке. В левом верхнем углу должна стоять точка.

v = input().split()
n, m = int(v[0]), int(v[1])
a = [['.'] * m for i in range(n)]
for i in range(len(a)):
    for j in range(len(a[i])):
        if i % 2 == 0:
            if j % 2 == 1:
                a[i][j] = '*'
        else:
            if j % 2 == 0:
                a[i][j] = '*'
for row in a:
    print(' '.join([str(elem) for elem in row]))
