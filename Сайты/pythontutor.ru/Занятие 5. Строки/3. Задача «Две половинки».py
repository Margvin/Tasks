#   Условие
#   Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, то длина
#   первой части должна быть на один символ больше). Переставьте эти две части местами, результат запишите в новую
#   строку и выведите на экран.

#   При решении этой задачи не стоит пользоваться инструкцией if.

#   Получаем данные
s = input()

#   Выдаем ответ
l = len(s)
l = (l + 1) // 2
print(s[l:] + s[:l])
