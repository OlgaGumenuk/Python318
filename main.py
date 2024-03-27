# _name2_ = "Nikolay"
# print("Hello," + _name2_ + "!")
# first_name = "Olga"
# print("Hello," + first_name + "!")#комментарии
# import math
# a =  30
# b = "Hello"
# c = 2.5
# print(type(a))
# print(type(c))
# print(type(c))
# a = "Hello"
# print(a, type(a))

# b = 5
# print(b, type(b))
# print(a + str(b))

# a = 5
# print(a, id(a))
# b = 4
# print(b, id(b))
# a = b
# print(a, id(a))

# a = b = c = 5
# print(a, b, c)

# a, b, c = 5 , "Hello", 9.2
# print(a, b, c)

# PI = 3.14
# print(PI)
# PI = 2  # нарушение соглашения
# print(PI)

# a = 21
# b = 512
# print("a:", a)
# print("b:", b)
# a, b = b, a

# c = a #c=1
# a = b #a=2
# b = c #b=1
# print("a:", a)
# print("b:", b)

# print("строка символовстрокастрока символовстрока символовстрока символовстрока симво\
#  символов")
# print('строка \nсимволов')
#
# print("Документ \'file.txt\' находится по пути D:\\folser\\file.txt")
# экранируем чтобы
# вывести спецсимволы как текст

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!"
# print(s3)
# print(s1 * 5)

# print(68741365899655122334875)
# print(6.8741365899655122334875)

# print(6 + 2)
# print(6 ** 2)  # 36
# print(6 % 4)  # 2
# print(6 / 4)  # 1.5
# print(6 // 5)  # 1


# number = (6 + 4) * (5 ** 2 + 7)
# print(number)  # 113
#
# num = 10
# num += 5  # num = mum + 5
# print(num)  # 15
#
# num -= 3  # num = mum  - 3
# print(num)  # 12

# num = 4321
# #print(num)
# a = num % 10
# print("a", a)
# #
# num = num // 10
# print(num)
# b = num % 10
# print("b", b)

# #print(num)
# c = num % 10
# print("c", c)
# num = num // 10
# #print(num)
# d = num % 10
# print("d", d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321  #432
# print(num)
# res = num % 10 * 1000
# num //= 10  # num = num // 10
# #print(res)
# res += num % 10 * 100
# #print(res)
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# num1 = "2.5"
# num2 = 3
# # res = num1 + str(num2)  #23
# # print(res)
# res = float(num1) + num2  # 5
# print(res)

# print(int(2.5))
# print(round(2.51))
# print(round(2.519, 2))

# a = 2.519
# b = round(a)
# print(b, type(b))
# c = round(a, 2)
# print(c, type(c))


# name = "Виктор"
# age = 28
# print("Меня зовут ", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + "лет.")
# print("Меня зовут ", name, ". Мне", age, "лет.", sep="", end="\n\n")
# print("Hello")

# name = input("Введите имя: ")
# print("Hello,", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
#
# # num = int(num)
# # power = int(power)
#
# res = num ** power  # '5' ** '2'
# print("Число", num, "в степени", power, "равно", res)

# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# num3 = int(input("Введите число: "))
# num4 = int(input("Введите число: "))
# sum1 = num1 + num2
# sum2 = num3 + num4
# print(round((sum1 / sum2), 2))

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5 = 6
# print(b2 + 5)  # 0 + 5 = 5

# print(bool("python"))
# print(bool(""))  # False
# print(bool(""))  # True
# print(bool(888))  # True
# print(bool(-65888))  # True
# print(bool(-6.38))  # True
# print(bool(0.0))  # False
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10 - 3)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 5)
# print(8 <= 5)
# print("привет" > "ПРИВЕТ")  # 1087 > 1055

# print(2 < 4 < 9)  # True && True +> True
# print(2 * 5 > 7 >= 4 + 3)  # True && True >= True
# print(3 * 3 <= 7 >= 2)  # => False && True => False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 , 5, False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True : True => True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True : False => False
# print(5 - 3 > 2 and 1 + 3 < 4)  # False : True => False
# print(5 - 3 > 2 and 1 + 3 < 4)  # False : False => False
#
# print(5 - 3 == 2 or 1 + 3 == 4)  # True : True => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True : False =>
# print(5 - 3 > 2 or 1 + 3 < 4)  # False : True =>
# print(5 - 3 > 2 or 1 + 3 < 4) # False : False => False

# print(not 9 - 5)  # False
# print(not 9 - 9)  # True

# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свои возраст: "))
# if age >= 18:
#     print("Доступ на саит разрешен")
# else:
#     print("Доступ запрещен")
#
#     # pass
#     # ...

# a = 25
# b = 25
# if a > b:
#     print("a > b")
# if b > a:
#     print("b > a")
# if a == b:
#     print("b == a")

# a = 41
# b = 41
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# s1 = int(input("Введите первую сторону: "))
# s2 = int(input("Введите вторую сторону: "))
# s3 = int(input("Введите третью сторону: "))
# if s1 == s2 == s3:  # '10'=='10'=='10'
#     print('Треугольник равностороннии')
# elif s1 == s2 or s1 == s3 or s2 == s3:
#     print('Треугольник равнобедренныи')
# else:
#     print('Треугольник разностороннии')

# day = int(input('Введите день недели(цифрои): '))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочии день -", end=" ")
#     if day == 1:
#         print('понедельник')
#     if day == 2:
#         print('вторник')
#     if day == 3:
#         print('cреда')
#     if day == 4:
#         print('четверг')
#     if day == 5:
#         print('пятница')
# elif day == 6 or day == 7:
#     print("Выходнои день")
#     if day == 6:
#         print('Суббота')
#     if day == 7:
#         print('Суббота')
# else:
#     print('Дня не существует!')

# mon = int(input('Введите номер месяца: '))
# if 1 <= mon <= 12:
#     if 3 <= mon <= 5:
#         print('Весна')
#     if 6 <= mon <= 8:
#         print('Лето')
#     if 9 <= mon <= 11:
#         print('Осень')
#     else:
#         print("Зима")
# else:
#     print('Ошибка')

# 22января

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# как свич в явескпирт только оператор мэтч

# password = "werty"

# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Такого значения не существует")

# day = "Четверг"
# time = 15
# match day:
#     case 'Понедельник' | 'Вторник' | 'Среда' | 'Четверг' | 'Пятница' if 9 <= time <= 16:
#         print("Рабочии день")
#     case 'Суббота' | 'Воскресенье':
#         print("Выходнои день")
#     case _:
#         print("Такого дня не существует или нерабочее время")

# тернарные операторы
# a, b = 40, 20
# minim = a if a < b else b
# print(minim)

# a, b = 50, 60
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 35, 2
# print("Делить на ноль нельзя" if b == 0 else a / b)
# print(a / b)

# a = 5
# b = "2a"
# print(a / b)  # ошиб


# try:
#     n = int(input("Ведите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или Нельзя делить на ноль")
# else:  # отработает кгода в блоке try не возникло исключения
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполнится в любом случае
#     print("Конец программы")

# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
# try:
#     a = int(a)  # 9
#     b = int(b)
# except ValueError:
#     a = str(a)
# finally:
#     print(a + b)  #

# Циклы

# i = 0
# while i < 5:
#     print("i = ", i)
#     i += 1  # i = i = 1

# i = 10
# while i > 0:
#     print("i = ", i)
#     i -= 2

# i = 2
# while i < 21:
#     print("i = ", i)
#     i += 2

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i = ", i)
#     i += 1

# n = int(input("Введите количество символов: "))
# print(n * "*\n")  #выведет горизонтально без  \n  звездочки

# n = int(input("Введите количество символов: "))
# i = 0
# while i < n:
#     print("*")
#     i += 1

# n = int(input("Введите количество символов: "))
# while n > 0:
#     print("*")
#     n -= 1

# n = int(input("Введите количество символов: "))
# print(n * "+-")  # +-+-+
# print(n * "+" if n % 2 == 0 else n * "-")
#
# i = 0
# while i < n:
#     print("+" if i % 2 == 0 else "-", end="")
#     # if i % 2 == 0:
#     #     print("+", end="")
#     # else:
#     #     print("-", end="")
#     i += 1

# n = int(input("Введите начало диапазона: "))  # 1
# m = int(input("Введите конец диапазона: "))  # 5
# sum1 = 0
# while n <= m:  # 1 <= 5
#     if n % 2:  # n % 2 != 0
#         # print(n, end=" ")
#         sum1 += n
#     n += 1
# print(sum1)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число нецелое")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1  # без этого шага будет непрекращающиися цикл будет  возращать на проверку условия < 10
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# summ = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     summ *= n
# print(summ)

# i = 0
# while i < 10:
#     # if i == 5:
#     #     break
#     if i == 8:
#         print(5 / 0)
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен")
# print("Код ниже")


# i = 1
# while i < 5:
#     print("Внешнии цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутреннии цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:  # 0 < 0 false идем мимо влоденного
#         print("_", end="")
#         j += 1
#     print("*")
#     i += 1
# print()
# i = 0  # 5
# while i < 5:
#     print("-" * i, "*", sep="")
#     i += 1

# for i in collection:
#   print(element)

# for i in "Hello!":
#     print(i)
#
# for color in "red", "blue", "green":
#     print(color)

# print(range(9))
# range(start, stop, step), start = 0, step = 1
#
# a = 9
# for i in range(0, a + 1, 1):
#     print(i, end=" ")
#
# print()
#
# i = 0
# while i <= 9:
#     print(i, end=" ")
#     i += 1

# for i in range(100, 0, -10):
#     print(i, end=" ")

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):  # 23
#     # if i % 11 == 0:
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Конец цикла")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("----")


# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# d = [i for i in "Hello"]
# print(d)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Список
# nums = [8, 3, 9, 4, 1, "stroka", True]
# print(nums)
# print(type(nums))
# print(nums[-2])
# print(nums[6])
# print(nums[-7])
# nums[1] = 256
# nums[2] +=100
# print(nums)
# for i in nums:
#     print(i)
# print(len(nums))

# s = [1, 2, 3]
# print(s)
# print(type(s))
#
# s1 = list("Hello")
# print(s1)
# print(type(s1))
#
# s2 = s1 + s
# print(s2)
#
# s2 = s * 2
# print(s2)

# n = list(range(2, 10, 3))
# print(n)

# a = [0 for i in range(5)]
# print(a)
#
# a1 = [i ** 2 for i in range(1, 25)]
# print(a1)
#
# a2 = [i * 3 for i in "Python"]
# print(a2)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)  # [0, 0]
# for i in range(len(a)):
#     a[i] = int(input("->"))
# print(a)

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
#

# summ = 0
# a = [int(input("->")) for i in range(int(input("n = ")))]
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         summ += a[i]
# #второи способ
# for i in a:
#     if i < 0:
#         summ += i
# print(summ)


# s = list(range(10, 100, 10))
# print(s)
#
# for i in range(len(s)):  # 0 1 2 3 4 5 6 7 8
#     print(s[i], end=" ")
# print()
# for i in s:
#    print(i, end=" ")

# n = list(range(21, 41))
# print(n)
# count = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         s += n[i]
# второи вариант
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         s += i
# print("Количество четных элементов списка: ", count)
# print("Сумма нечетных элементов: ", s)

# n = list(range(21, 41, 3))
# print(n)
#
# a = 2
# print(n[a])
# print(n[a - 1])

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")
# второи вариант
# for i in a:
#     if i > i - 1:
#         print(i, end=" ")

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# s = count = 0
# for i in range(len(a)):
#     s += a[i]
#     if a[i] != 0:
#         count += 1
# print(s / count)

# a = [7, 9, 2, 1, 17]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# Срез = список у которого можем передать от[start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# print(s)
# print(s[1:3])  # не включая последнии индекс
# print(s[:3])
# print(s[3:])
# print(s[:])  # от начало и до конца
# print(s[::-1])
# print(s[3:1:-1])
# print(s[1:3:-1])  #  не сработает
# print(s[5:0:-1])  #стоп будет идти до этого элемента невозьмет нулевои элемент
# print(s[6:])
# print(s[::-1], id(s[::-1]))
# print(s[6:22], id(s[6:22]))

# lst = list(range(1,8))
# print(lst[:])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[6:])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# st = "Hello"
# print(st)
# print(st[0:3])
# print(st[::-1])

# a = 5789
# print(a[0])  # срезы не работают с числом
# for i in st:
#     print(i)

# Методы списков dir(list)
# s = [9, 5, 6, 3, 7, 4]
#
# print(s)
# #s.append(8)  # добавили элемент в конец списка
# s.append([8, 2])
# #
# # s.extend([20, 1, 2])
# # s.extend("add") # добавили  набор элементов в конец списка
# print(s)
# # добавляет элемент по заданному индексу второи параметр это значение а первыи это номер индекса элемента
# s.insert(3, 59)
# s.insert(-1, 222)
# print(s)

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
#
# s = []
# n = int(input("Введите кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     if x % 2 == 0:
#     s.append(x)
#     # s.insert(0, x)
# print(s)

# s = []
# n = int(input("Введите кол-во элементов списка: "))
# for _ in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)

# ищем область пересечения списков
# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = [] # [2, 1, 4, 3]
#
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
#
# # second variant
# s = []
# for el in a:
#     if el in b and el not in s:
#         s.append(el)  # [2, 1, 4, 3]
# print(s)


# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# # print(a + b)
# # if len(b) > len(a):
# if len(a) > len(b):
#     a, b = b, a
#     for i in range(len(a)):
#         c.append(a[i])  # 0 1 2 3 4
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])  # 0 1 2 3 4
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)  # [1, 11, 2, 22, 3, 33, 44, 55]


# a = [5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(a)
# a.remove(9)  # удаляет первое совпадение по значению
# print(a)
# last = a.pop()  # удаляет последнии эл-т списка и возвращает его же
# print(last)
# second = a.pop(0) # удаляет элемент по индексу
# print(second)
# print(a)
# a.clear()  # очистил список
# print(a)

# num = a.count(9)  # считает кол-во заданных значении в списке
# print(num)
# ind = a.index(8)  # возвращает индекс элемента по заданному значению
# print(ind)
# ind2 = a.index(9, 2, -1)  # ищет со 2-го индекса и до конца цифру 9
# print(ind2)

# num = 7
# if num in a:
#     print(a.index(num))

# a = [7, 9, 2, 9, 1, 17, 9]
# print(a)
# a.reverse()
# print(a)


# a = [1, 2, 3]
# b = a.copy()
# print("a=", a)
# print("b=", b)
# # a.append(4)
# b.append(120)
# print("a=", a)
# print("b=", b)
# метод еще посмотреь сорт

# пропустила занятие за 03 фквраля

# n = int(input("Введите количество символов: "))
# sim = input("Введите тип символа: ")
# orient = int(input("0 - горизонтальная \n1 - вертикальная \nориентация линии: "))
# i = 0
# while i < n:
#     if orient == 0:
#         print(sim, end=" ")
#     if orient == 1:
#         print(sim)
#     i += 1
# else:
#     print("Такои ориентации не предусмотрено")
#         # break
#     i += 1

# заятие 3 февраля

# sort - посмотреть
# a = [7, 9, 2, 9, 1, 17, 9]
# # print(a)
# a.sort()  # сортировка элементов по возрастанию
# # a.sort(reverse=True)  # сортировка элементов по убыванию
# print(a)
#
# s = ["Виталии", "Алескандр", "Алексеи", "Анна"]
# # print(s)
# # s.sort()
# # print(s)
# s.sort(key=len)  #сортировка по длине элемнтов списка отменьшего к больш.
# print(s)
# s.sort(key=len)
# s.sort(key=len, reverse=True)  #сортировка по алгоритму заданнои функции
# print(s)
# print(len(s))
# print(len(s[0]))

# a = [7, 9, 2, 9, 1, 17, 9]
# lst = sorted(s, key=len, reverse=True)
# print(lst)
# print(s)

# Генерация случаиных данных

# import random


# print(random.random())
# print(random.randint(0, 9))  # 9-включительно
# print(random.randrange(3, 9, 2))  # 9-не включительно
# print(round(random.uniform(10.5, 25.5), 2))

# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# print(s)
# random.shuffle(s)
# print(random.choice(s))
# print(random.choices(s, k=3))  #генерирует кол-во

# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)


# s = ['20', '30', '40', '50', '60', '70', '80', '90', '10']
# print(s)
# print(len(s))
# print(sum(s)) работает только с числовыми типами данных
# print(max(s))
# print(min(s))

# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# print(s)
# res = 0
# for i in s:
#     res += i
# print(res)
# print(sum(s))

# svitok = [random.randint(123, 184) for i in range(7)]
# print(svitok)
# big = max(svitok)
# print(big)
# svitok.insert(0, big)
# print(svitok)

# x = list('1a2b3c4d')
# print(x)
# print('b' not in x)
# print('l' not in x)
# s = 'c1'
# if s in x:
#     print("Такои элемент в списке присутствует")
# else:
#     print(s, "в списке отсутствует")

# lst = []
# # if not lst:  # lst == []  len(lst) == 0
# #     print("Список пустои")
#
# print(bool(lst))


# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первыи список: ", a)
# print("Второи список: ", b)
# c = a + b
# print(c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# # for i in range(len(b)):
# #     if b[i] not in c:
# #         c.append(b[i])
# print(c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print(c)
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# n1 = 10
# # a = [random.randint(0, 10) for i in range(n1)]
# a = []
# while len(a) != n1:
#     n = random.randrange(n1)  # от 0 до 10
#     if n not in a:
#         a.append(n)
# print(a)


# m = [
#     [1, 2, 3, 4, 55],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12, 44, 88]
# ]
# print(m, end="\n\n")
# # print(len(m))
# print(m[1][2])

# s = ["Hello", "World"]
# print(s[1][0])

# for row in range(len(m)):  # 0 1 2
#     print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# второи вариант записи без индексов
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#     print()
# print()
#
#
# for row in m:
#     for x in row:
#         print(x ** 2, end="\t\t")
#     print()


# w, h = 5, 3
# # matrix = [[random.randint(1,20) for x in range(w)] for y in range(h)]
# matrix = [[0 for x in range(w)] for y in range(h)]

# matrix = []  # [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# for y in range(h):  # 3
#     new_row = []
#     for x in range(w):  # 5
#         new_row.append(0)  # new_row = [0,0,0]
#     matrix.append(new_row)
#
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# распакoвка последовательностеи
# for x, y, z in [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4]]:
#     print(z, ") ", x, "+", y, " = ", x + y, sep="")

# for x in [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4]]:
#     print(x[2], ") ", x[0], " + ", x[1], " = ", x[0] + x[1], sep="")

# занятие 4 февраля
# задача вывести символов горизонально или вертикально
# n = int(input("Кол-во символов: "))
# sim = input("Тип символа: ")
# orient = int(input("0 - горизонтальная,\n1 - вертикальная,\nopиентация линии:"))
# i = 0
# while i < n:
#     if orient == 0:
#         print(sim, end=" ")
#     if orient == 1:
#         print(sim)
#     i += 1
# else:
#     print("Такого не предусмотрено")


# import math

# num1 = math.sqrt(4)
# num2 = math.pi
# num3 = math.ceil(3.2)
# num4 = math.floor(3.7)
# print(num1)
# print(num2)
# print(num3)
# print(num4)

# import math as m

# num3 = m.ceil(3.2)
# num4 = m.floor(3.7)
# print(num3)
# print(num4)

# from math import *
#
# num3 = ceil(3.2)
# num4 = floor(3.7)
#
# print(num3)
# print(num4)

# from math import ceil as c, floor as f
#
# num3 = ceil(3.2)
# num4 = f(3.7)
#
# print(num3)
# print(num4)

# from math import pi
#
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности: ", round(2 * pi * radius, 2))


# import time
# import locale
# locale.setlocale(locale.LC_ALL, "bel")

# second = time.time()
# print(second)
# s = 5478963211
# local_time = time.ctime()
# print(local_time)
#
# res = time.localtime()
# print(res)
# print("0" + str(res.tm_mday) if res.tm_mday < 10 else res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("%d/%m/%Y, %I:%M:%S", time.localtime(s)))
#
# print(time.strftime("Сегодня: %B %d, %Y"))

# import time
# start = time.monotonic()
# pause = 2.3
# print("Программа запущена...")
# time.sleep(pause)
# print("Пауза была", pause, "секунд")
# finish = time.monotonic()
# res = finish - start
# print(res)

# Функции

# def hello(name, age):
#     print("Мне", age, "Меня зовут", name)
#
#
# hello("Irina", 28)
# hello("Igor", 29)


# def get_sum(a, b):
#     print("Сумма: ", end="")
#     return a + b
#
#
# n = 2
# m = 5
# # print(get_sum(n, m))
# res = get_sum(n, m)  # 7
# print(res)
# print(res + 5 - 2)
# c = 7
# d = 10
# get_sum(c, d)

# get_sum(2, 5)
# get_sum("Hello ", "World!")


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two


# print(maximum(9, 6))  # 9
# print(maximum(9, 16))  # 16


# def maximum(a,b):
#     if a>b:
#         return a-b
#     else:
#         return a+b
#
# print(maximum(
#     a=int(input("Ввудите a:")),
#     b=int(input("Ввудите b:"))
# ))

# def change(lst):
#     #
#     lst.insert(0, lst[-1])
#     lst.pop(-1)
#     lst.append(lst[1])
#     lst.pop(1)
#     print(lst)
#
#
# change([1, 2, 3])
# change([9, 12, 33, 54, 105])
# change(['с', 'л', 'о', 'н'])

# def cub(a):
#     return a * a * a
#
#
# for i in range(21, 31):
#     print(i, "в кубе =", cub(i))


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     end = lst.pop()  # удалили последнии элемент из списка
#     start = lst.pop(0)  # удалили pervii элемент из спи
#     lst.insert(0, end)  # добавляем элементы в начало списка
#     lst.append(start)  # добавили в конец списка элемент
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с','л','о','н']))

# def maximum(one, two):
#     if one > two:
#         return True
#     else:
#         return False
#
#
# print(maximum(9, 6))  # True
# print(maximum(9, 16))  # False
#
# if maximum(9, 16):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")

# def check_password(password):
#     has_lower = False
#     has_upper = False
#     has_num = False
#
#     for ch in password:
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_lower and has_upper and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Надежныи пароль")
# else:
#     print("Ненадежныи пароль")

#
# from random import randint
#
# w, h = 3, 4
# matrix = [[randint(-20, 10) for y in range(w)] for x in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#         if x < 0:
#             count += 1
#     print()
# print(count)


# 10 02 24

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2,))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))

# def set_param(c=20, s="-"):
#     print(s * c, end="")
#     print()
#
#
#
# set_param()
# set_param(7)
# set_param(s="#")
# set_param(15,"+")
# set_param(s="*", c=10)


# def digits_sum(n, even=True):  # 9874023
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2:
#             s += cur_digit
#         # print(cur_digit)
#         # print(n)
#         n //= 10  # n = n //10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр:")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge", age)
#
#
# display_info("Irina", 23)
# display_info(23, "Irina")
# display_info(age=23, name="Irina")
# # display_info("Igor", age=23, name="Irina")


# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)
# a = a + "_new"
# print(a)
# print(id(a))
# print(id(b))

# lt1 = [1, 2, 3]
# print(lt1, id(lt1), id(lt1[0]), id(lt1[1]))
# lt1[1] = 50
# print(lt1, id(lt1), id(lt1[0]), id(lt1[1]))

# Неизменяемые типы данных - int,str,float,bool, tuple
# Uзменяемые типы данных - list

# Кортеж(Tuple) - неизменяемы список
#
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# #
# #
# print(tpl[2])
# print(type(tpl))

# a = ()
# print(a, type(a))
#
# b = tuple("Hello")
# print(b)
# b = tuple(["Hello", "World"])
# print(b, type(b))

# a = 5,
# print(a, type(a))


# from random import randint

# tpl = tuple(i for i in range(5))
# tpl = tuple(input("-> ") for i in range(5))
# tpl = tuple(randint(1, 100) for i in range(5))
# tpl = tuple(2 ** i for i in range(1, 13))
# print(tpl)

# t1 = tuple("Hello")
# t2 = tuple("World")
# # print(t1)
# # print(t2)
# t3 = t1 + t2
# print(t3 * 2)
# print(t3.count("l"))

# print(t3.index('l', 4, -2))
# sym = "o"
# if sym in t3:
#     print(t3.index(sym))
# else:
#     print("Такого символа нет")

# try:
#     print(t3.index(sym,4, -2))
# except ValueError:
#     print("Такого символа нет в заданном диапазоне")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()  # ()
#
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8)),
# print(slicer((1, 2, 8, 5, 1, 2, 9), 5)),


# t = (10, 11, [1, 2, 3], [4, 5, 6],["hello","world"])
# print(t, id(t))
# t[4][0] = "hi"
# t[4].append("new")
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа x, y, z = 1, 2, 3
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# first_name, year, married = get_user()  # first_name, year, married = name, age, is_married
# # user = get_user()
# # first_name, year, married = user
# # print(user[0])
# # print(user[1])
# # print(user[2])
# print(first_name, year, married)

# name = "Igor"
#
# if name:
#     print("Name ", name)
#     name = "Marina"
# else:
#     print("Else")
#
# print(name)


# for i in range(5):
#     print(i, end=" ")
#     name = "Marina"
#
# print()
# print(name)


# name = "Ifor"


# def func():
#     print("Hello")
#     name = "Marina"
#
#
# func()
# print(name)


# lst = [1, 2, 3, 4, 5]
# tpl = tuple(lst)
# print(tpl)
# lst2 = list(tpl)
# print(lst2)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326),("Гамбург", 1.718))),
#     ("Франция", 80.2, (("Париж", 15.26),("Марсель", 1.808))),
# )
# print(countries, end="\n\n")

# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ",country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("Город: ", city_name, ", население = ", city_population, sep="")


# МНОЖЕСТВА (set) - неупорядоченная коллекция,изменяемы тип данных,которая хранит только уникальные значения

# s = {"red","green","blue"}
# print(type(s))
# print(s)
# print(len(s))
#
# for i in s:
#     print(i)


# a = []
# print(a, type(a))

# a = set("hello")
# print(a, type(a))

# from random import randint
# # s = {x * x for x in range(10)}
# # s = {input("-> ") for x in range(3)}
# s = {randint(20, 50) for x in range(10)}
# print(s)


# s = {"red", "green", "blue"}
# print("green" in s)
# print("green" not in s)


# lst = ['ad_1', "ac_2", "bc_1", "bc_2"]
# # lt = [i for i in lst if 'a' in i]
# # lt = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst]
# lt = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c']
# print(lt)


# for i in lst:
#     if i[1] == 'c':
#         if i[0]  == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])


# s = {"red", "green", "blue"}
# print(s)
# s.add("black")  # добавление элемента во множества
# print(s)
# # s.remove("black")  # удаляет элемент по значению
# # print(s)
# # color = "pink"
# # if color in s:
# #     s.remove(color)  # KeyError
# # s.remove("pink")
# #
# # s.discard("green")  # удаляет элемент по значению,  не выбрасывает исключение если элемента не существует
# # print(s)
#
#
# color = s.pop()  # удаляет первыи элемент из множества
# print(s)
# print(color)
#
# s.clear()  #очищает множества
# print(s)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# a |= b

# print(a)
# c = a & b
# a &= b
# print(c)
# n = 5
# m = 6
# v = n + m
# print(v)
# n += m
# print(n)

# c = a - b
# a -= b
# c = a ^ b
# a ^= b
# print(c)
# print(a)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))


# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")


# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
# one_hobby = drawing ^ music
# print(one_hobby)
# both_hobbies = drawing & music
# print(both_hobbies)
# drawing = drawing - both_hobbies
# print(drawing)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a >= b)
# print(a < b)
# print(a > b)
# print(a != b)


# a = [9, 8, 9, 6, 5, 2, 5, 8, 3, 7, 8, 4, 7]
# print(a)
# s = set(a)
# print(s)
# a1 = list(s)
# print(a1)
#
#
# a = (9, 8, 9, 6, 5, 2, 5, 8, 3, 7, 8, 4, 7)
# print(a)
# s = set(a)
# print(s)
# a1 = tuple(s)
# print(a1)


# s = frozenset("Hello")
# s = frozenset(["Hello", "Hello"])
# s = frozenset([9, 6, 5, 2, 5, 8, 3, 7, 8])
# print(s)


# Словари (dict)


# lst = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# lst[1] = 200
# d["two"] = 200
# print(lst)
# print(d)


# d = {}
# print(d, type(d))
#
# d1 = dict()
# print(d1, type(d1))

# d = {"one": 1, "two": 2}
# print(d, type(d))
#
# d1 = dict(one=1, two=2)
# print(d1, type(d1))
#
# # a = ([("a", 1), ('b', 2)])
# a = [("a", 1), ('b', 2)]
#
# d2 = dict(a)
# print(d2, type(d2))

# 18 февраля
# ключи не должны повторяться
# ключом могут быть неизменяемые типы данных
# списки множества и словарь не могут быть ключами
# но могут быть значениями
# d = {0: "text", "one": 45, (1, 2.3): "Кортеж", "Список" : [2,3,5], True : 1, False : 0, 1 : "Один"}
# print(d)


# удаление значения  по ключу
# key = 45
# # if key in d:
# #     del d[key]
# print(d)

# удаление значения второи вариант
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + str(key) + " нет в словаре")
# print(d)

# d["ne"] = "Новое зачение"  # добавили ключ
# print(d)
# print("one" in d)
# print("ne" in d)

# for key in d:
#     print(key, ":", [key])

# виды ключеи
# print(d[0])
# print(d[(1, 2.3)])
# print(d[False])
# print(d[True])
# print(d[1])

# задача

# sl = {'x1' : 3, 'x2 : 7', 'x3' : 5, 'x4' : -1}
# a = 1
#
# for key in sl:
#     a *= sl[key]
#     #print(sl[key])
# print(a)

# задача

# d = dict()  # {}
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")

# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# задача

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400],
# }
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "зуб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] = count
#                     break
#                 except ValueError:
#                     print("Значение некорректно. Введите число")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
#
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "зуб", sep="")


# методы словару в консоли дир(дикт) поанглиски

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# for key, value in d.items():
#     print(key, "->", value)
# #словарь в список перобразовать
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy()
# print("D = ", d, id(d))
# print("D2 = ", d2, id(d2))
#
# d['b'] = 5
# d2['e'] = 7
# print(("D = ", d, id(d)))
# print("D2 = ", d2, id(d2))

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['b'])
# value = d.get('b', 'Такого ключа нет')
# print(value)
# item = d.setdefault('c')
# item = d.setdefault('c', 5)
# print(item)
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3}
# # item = d.pop('b', 5)
# # print(item)
# # print(d)
#
# item = d.pop('w', "Такого ключа нет")
# print(item)
# print(d)
# item2 = d.popitem()# удаляет последн ключи и значение и возвращает их в кортеже
# print(item2)
# print(d)
# d.clear()
# print(d)

# d = dict.fromkeys(['a', 'b'], 100)  #задаем значение для всех ключеи
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3}
# # d2 = [('r', 7), ('q', 9)]
# d2 = {'r': 7, 'q': 9}
# print(list(d2.items()))
# # # d.update(d2)
# d3 = d.copy()
# d3.update(d2)
# # d |= d2
# print(d3)


# d = {'name': 'Kelly', 'age': '25', 'salary': 8000, 'city': 'New York'}
# new_d = {}
#
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)


# d = {'name': 'Kelly', 'age': '25', 'salary': 8000, 'city': 'New York'}
# print(d)
#
# d['location'] = d.pop('city')
# print(d)


# #меняем местами ключи и значения
# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# # new_d = {value: key for key, value in d.items()}
# new_d = {key: value for key, value in d.items()}
# print(new_d)
# #задача
# new_d = {key: value for key, value in d.items() if value <= 2}
# print(new_d)

# задача
# sales = {
#     'John': {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     'Tom': {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     'Anne': {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     'Fiona': {"N": 3984, "S": 3643, "E": 8821, "W": 2451},
# }
# print(sales)
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print(y, ":", sales[x][y])

# решение
# sales = {
#     'John': {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     'Tom': {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     'Anne': {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     'Fiona': {"N": 3984, "S": 3643, "E": 8821, "W": 2451},
# }
# print(sales)
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print(y, ":", sales[x][y])
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])


# 24 february

# zip готовая функция

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# # c = (2.9, 3.7, 9.2)
# # # d = dict(zip(b, a))
# # d = list(zip(b))
# d = dict(zip(b, a))
# # d = set(zip(b, a))
# # d = tuple(zip(b, a, c))
# print(d)


# one = {'name': "Igor", 'surname': 'Doe', 'job': 'Consultant'}
# two = {'name': "Irina", 'surname': 'Smith', 'job': 'Manager'}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# распаков последов.
# lt = [('Dec', 12), ('Jan', 1), ('Feb', 2)]
# a, b = zip(*lt)
# print(a)
# print(b)

# a = (1, 2, 3)
# b = [4, *a, 5, 6]
# print(b)  # список внутри списка b
# print(len(b))


# паспаковка словаря как может рабоатать
# first = {'one': 1, 'two': 2}
# second = {'three': 3, 'flour': 4,'one': 11}
# print({**first, **second})  # общии словарь {'one': 1, 'two': 2, 'three': 3, 'flour': 4}
# for k, v in {**first, **second}.items():
#     print(k, "=>", v)


# colors = ['red', 'green', 'blue']
# # i = 1
# # for color in colors:
# #     print(i, ")", color, sep="")
# #     i += 1
# for num, val in enumerate(colors, 1):  # start=1
#     print(num, ")", val, sep="")

# задача

# studs = {}
# n = int(input("Кол-во студентов: "))
# s = 0
# for i in range(n):  # 0
#     name = input(str(i + 1) + "-и студент: ")  # "1"-и студент
#     point = int(input("Балл: "))
#     studs[name] = point  # создали словарь с ключами и значениями
#     # s += point
#       # или за пределами фора
# s = sum(studs.values())
# avg = s / n
# print(studs)
# print(s)
# print("Среднии балл: ", avg)
#
# for i in studs:  # i попало имена
#     if studs[i] > avg:  # балл
#         print("Cтуденты с балом выше среднего ",i)
#
# for k, v in studs.items():
#     if v > avg:
#         print(k)


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 6, 7, 8, "abc"))
# print(func())

# def summa(*params):
#     print(type(params))
#     print(*params)
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3))
# print(summa(1, 2, 3, 4, 5, 6, 7))


# def ch(*args):
#     avg = sum(args) / len(args)
#     print(avg)
#     res = []
#     for num in args:
#         if num < avg:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(5, 6, 7, 8, 9))
# s = 1, 2, 3, 4, 5, 6, 7, 8, 9
# print(s)
# print(type(s))


# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(1, 2, 3, "abc"))


# def print_scores(student, *scores):
#     print("Student name: ", student, end=", Oценки: ")
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores("Jonathan", 100, 65, 85, 96, 87)
# print_scores("Rick", 96, 20, 33, 66)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(one="один"))
# получим словари


# def intro(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#     print()
#
#
# intro(name="Irina", surname="Sharma", age=22)
# intro(name="Igor", surname="Wood", email="rei.mail.ru", country="Russia", age=22,phone=79598456541)


# def func(a, b, *args, y=0, x=0, **kwargs):
#     return a, b, args, kwargs, y, x
#
#
# print(func(5, 1, 2, 3, 4, 5, 6, 7, n=9, m=10, x=5, y=100))

# задача
# my_dict = {'one': 'first'}


# def ddictio(**kwargs):
#     my_dict.update(kwargs)
#
# print("my_dict = ", my_dict)
# ddictio(k1=22, k2=31, k3=11, k4=91)
# print("my_dict = ", my_dict)
# ddictio(name='Bob', age=31, weight=61, eyes_color='grey')
# print("my_dict = ", my_dict)

# name = "Tom"  # глобльная переменная
# surname = ""
#
# def hi():
#     global name, surname
#     name = "Sam"
#     surname = "Johnson"  # локальная переменная
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)


# sum = 5
#
# lst = [9, 8, 5, 6,]
# print(sum(lst))

# print = "Hello"
#
#
# print("Python")


# 03 march2024

# s = 0
#
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)


# def add(a):
#     x = 2
#
#     def outer():
#         # x = 3
#         print("x =", x)
#         return a + x
#
#     return outer()
#
#
# print(add(5))


# x = 25
# t = 0
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#
#
#     inner()
#     print('a = ', a)
#     t = a
#
#
# fn()
# c = x + t  # 25 + 30 = 55   # 25 + 35 = 60
# print(c)


# x = 5
#
# def fn1():
#     x = 25  # 2  # x = 55
#
#     def fn2():
#         # x = 33  # 4  # x = 55
#
#         def fn3():
#             nonlocal x
#             x = 55  # 6
#
#         fn3()  # 5
#         print("fn2.x", x)  # 7
#     fn2()  # 3
#     print("fn1.x", x)  # 8
#
#
# fn1()  # 1
# print(x)


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         print(a, b)
#
#     inner()  # перестает существовать после вызова
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]


# Замыкание - функция возвращает другую функцию, но не вызывает ее

# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(6)
# print(item2(10))

# print(outer(7)(10))
# def func(a):
#     return a * 2
#
#
# x = func(5)
# print(x)


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         # global a
#         c.append(4)
#         a = a + 1  # a += 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# задача

# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
# res2()
#
# res1()
# res1()
# res1()


# lambda - выражения
# print((lambda x, y: x + y)(1, 2))
# # print((lambda x, y: x + y)(10, 20))
#
# def func(x, y):
#     return x + y

# func = lambda x, y: x + y
# print(func(1, 5))

# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())
#
# print((lambda *args: args)(1, 2, 3, 4, 5, 6, 7, 8))
# print((lambda *args: args)(1, 2, 3))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
# for t in c:
#     print(t("abc_"))


# def inc1(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# func = inc1(10)
# print(func(5))


# def inc2(n):
#     return lambda x: n + x
#
#
# func2 = inc2(10)
# print((func2(5)))
#
#
# inc3 = (lambda n: (lambda x: n + x))
#
# func3 = inc3(10)
# print(func3(5))
#
# print((lambda n: (lambda x : n + x))(10)(5))


# print((lambda a: (lambda n: (lambda x: a + n + x)))(2)(4)(6))


# def func(i):
#     return i[1]
#
#
# d = {'a': 15, 'c': 10, 'b': 5}
# # lst = sorted(d.items(), key=lambda i: i[1])  # [('a', 15), ('b', 5), ('c', 10)]
# lst = list(d.items())
# # print(lst)
# # lst.sort(key=lambda i: i[1])
# lst.sort(key=func)
# print(lst)
# print(dict(lst))


# players = [
#     {'name': "Антон", "last_name": "Бирюков", "raiting": 9},
#     {'name': "Алексеи", "last_name": "Бодня", "raiting": 10},
#     {'name': "Федор", "last_name": "Сидоров", "raiting": 4},
#     {'name': "Михаил", "last_name": "Семенов", "raiting": 6},
# ]
#
# res = sorted(players, key=lambda item: item["last_name"])
# print(res)
#
# res = sorted(players, key=lambda item: item["raiting"], reverse=True)
# print(res)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(a[1](8, 3))
# print(a[0](8, 3))
# print(a[2](8, 3))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
# }
#
# d[6]() - должна быть вызвана функция лямбда
# from math import pi
#
# area = {
#     "Circle": lambda radius: pi * radius * radius,
#     "Rectangle": lambda a, b: a * b,
#     "Trapezoid": lambda a, b, h: (a + b) * h / 2
# }
#
# print("Площадь окружности", area["Circle"](2))
# print("Площадь прямоугольника", area["Rectangle"](10, 13))
# print("Площадь трапеции", area["Trapezoid"](7, 5, 3))


# print((lambda a, b: a if a > b else b)(5, 10))
# print((lambda a, b: a if a > b else b)(15, 10))


# задача нелокальная
# s = 0
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)


# def outer(a, b, c):
# s = 0
#
# def inner(i, j):
#     nonlocal s
#     s = i * j
#
#     inner(a, b)
#     inner(a, c)
#     inner(b, c)
#     return 2 * s
#
#
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)

# print("Вносим изменения")

# print("Данные переносим на GitHub")


# map(func, iterable), filter(func, iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# lst2 = list(map(lambda t: t * 2, lst))
#
# print(lst2)
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))

# t = (2.88, -1.75, 100.55)
#
# # t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
# print(t2)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5, 6, 7]
#
# res = list(map(lambda x, y: (x, y), num, st))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)

# def func(s):
#     return len(s) == 3


# t = ('adcf', 'jdhsncb', 'nhg', 'lsk', '')
#
# # t2 = tuple(filter(lambda s: len(s) == 3, t))
# # t2 = tuple(filter(func, t))
# t2 = tuple(filter(lambda s: s * 3, t))
# print(t2)


# b = [60, 90, 100, 75, 55, 45, 78, 68, 81]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# from random import randint

# lst = [randint(1, 40) for i in range(10)]
# print(lst)
#
# lst2 = list(filter(lambda t: 10 <= t <= 20, lst))
# print(lst2)


# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)
#
# m1 = [x ** 2 for x in range(10) if x % 2]
# print(m1)


# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def inner():
#         print("Code before")
#         func()
#         print("Code after")
#
#     return inner
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декарирующая функция
#     def inner():
#         print("*" * 40)
#         func()
#         print("=" * 40)
#
#     return inner
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# func_test()
#
# # вуаДОПИСАТЬТЬЬЬЬЬЬЬЬЬЬЬЬ
#
#
# print("Hello, I am func 'func_test'")


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# задача
# def cnt(fn):
#     count = 0
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные: ", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
# @args_decorator
# def print_full_name(name, surname):
#     print("Меня зовут", name, surname)
#
#
# print_full_name("Ирина", "Ветрова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:",args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Ирина", "Борис", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма ", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность ", "-")
# def sub(a, b):
#     print(a - b)
#
#
# @decor("Произведние ", "*")
# def mul(a, b):
#     print(a * b)
#
#
# n = 5
# m = 5
# summa(n, m)
# sub(n, m)
# mul(n, m)

# задача
# def multiply(arg):
#     def decor(fn):
#         def wrap(*args, **kwargs):
#             return arg * fn(*args, **kwargs)
#
#         return wrap
#     return decor
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# домаш1603


# def avg(fn):
#     def wrap(*args):
#         return fn(*args) / len(args)
#
#     return wrap
#
#
# @avg
# def summa(*args):
#     return sum(args)
#
#
# print(summa(2, 3, 3, 4))


# занятие 17 03 2024 строки - неизменемыи тип данных

# print(0b10)
# print(bin(18))  # 0b10010 => 0b => префикс двоичная система
# print(oct(18))  # 0o22 => 0o - восьмиричная система
# print(hex(18))  # 0x12 => 0x - шестнадцатеричная система
#
# print(0b10010 + 0o22)
# print(0o22 + 0x12)
# print(0x12 + 18)


# v = 'Pyt'
# w = 'hon'
# e = v + w
# print(e)  # Python +>
# print(e * 3)
# print("y" in e)
# print("l" in e)
# print(e[1])
# print(e[-1])
# print(e[1:4])
# print(e[1:4])
# print(e[:])
# print(e[::-1])
# e = e[:3] + 't' + e[4:]

# print(u"Привет")
# print("C:\\folder\\file.txt")
# print(r"C:\folder\file.txt")
# print(r"C:\folder\\"[:-1])
# print(r"C:\folder" + "\\")
# print("C:\\folder\\")

# name = "Дмитр"
# age = 25
# print("Ьеня зовут " + name + " . Мне" + str(age) + " лет.")
# a = f"Меня зовут {name}. Мне {age} лет."
# print(a)
# print(f"Число {round(12.23654, 2)}, {5 + 3}")
# print(f"Число: {12.23654:.3f}")

# x = 5
# y = 10
# print(f"{x = }, {y = }")
# print(f"{x} x {y} / 2 = {x * y / 2}")

# dir_name = "folder"
# file_name = "file.txt"
# # print(fr"home\{dir_name}\{file_name}")
# print("home" + "\\" + dir_name + "\\" + file_name)

# s = """Строка
# символов"""
# print(s)
# s1 = '''Строка
# имволов'''
# print(s1)
# s2 = ("Строка символов")
# print(s2)

# def suare(n):
#         """Принимает число n, возвращает число n"""
#     print("hello")
#     return n ** 2
#
#
# print(suare(5))

# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданнои высоты и радиуса основания.
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * (r + h)
#
#
# print(cylinder(5, 8))
# print(cylinder.__doc__)
# print(sum.__doc__)
# print(len.__doc__)
# print(int.__doc__)
# print(type.__doc__)

# print(ord('a'))
# print(ord('ш'))


# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# st = "Test string for me"
# arr = [ord(x) for x in st]
# print("ASCII коды: ", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифетическое", arr)
# arr += [ord(x) for x in input("->")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

#Домашнее за 17.03.2024

# arr = str("Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень хорошии язык программирования.")
# n = str("N")
# p = str("P")
# print(arr)
#
# arr2 = []
# for x in range(len(arr)):
#     if arr[x] != n:
#         arr2.append(arr[x])
#
#     else:
#         arr2.append(p)
# # print(arr2)
#
# print(''.join(str(el) for el in arr2))









# 24 марта 2024 занятие



#  пропустила первые 15 минут





# s = "hello, world! I am learn.PY."
# print(s)
#
# print(s.endswith("on."))  #  заканч-ся ли строка на заданную подстроку ->(true , false)
# print(s.startswith("I am", 14))  #  заканч-ся ли строка на заданную подстроку ->(true , false)
# print(s.find("I am"))


# a = input("Введите число: ")
# try:
#     a = int(a)
#     print(a ** 2)
# except ValueError:
#     print("Нужно ввести число")

# print('123'.isdigit())  # состоит ли строка только из чисел
# print('12a3'.isdigit())
#
# a = input("Введите число: ")
# b = 2
# if a.isdigit():
#     a = int(a)
#     print(a + b)
# else:
#     print(a + str(b))

#
# print("abc123!".isalnum())  # состоит ли строка из букв и цифр НО БЕЗ СПЕЦСИМВОЛОВ
# print("abcASD".isalpha())  # состоит ли только из букв

# print("abc".islower())  # состоит ли из нижнего регистра
# print("ВАП!;%".isupper())  # состоит ли из верхнего регистра

# print('py'.center(10))  # метод смещает
# print('py'.center(10, "-"))  # метод смещает  с символом заполнителем ----py----
# print('py'.center(2))  #

# print("   py    ".lstrip())
# print("   py    ".rstrip())
# print("   py    ".strip())

# print("https://www.pyhon.org".lstrip("/:pths"))
# print("https://www.pyhon.org".strip("/:pthsw"))
# print("https://www.pyhon.orgw".lstrip("/:pths").rstrip("w"))

# s = "hello, Python! I am learning Python. Python"
# print(s.replace("Python", "Java"))  # replace метод поиск и замена того что нашли

# преобразовыватель метод

# s = ""
# seg = ("a", "b", "c")
# print(s.join(seg))
#
# print("..".join(['1', '2']))  # объединяет итерируемыи объект в строку через символ разделитель
#
# print(":".join("Hello"))

# print("a b c".split())  # метод разбивает на элементы в виде списка
# print("www.python.org".split("."))  # метод разбивает подругому по символу
# print("www.python.org".split(".", 1))  #  с объединнением всего чтоосталось после этого
# print("www.python.org".rsplit(".", 1))  #  с объединнением всего чтоосталось после этого

# Регулярные выражения
# если какието совпадения то меняем

# import re

# s = "Я ищу совпадения в 2024 году. И я их наиду в 2 счёта."
# reg = r"\."
# print(re.findall(reg, s))  # возвращает список, содержащии все совпадения с шаблона
# print(re.search(reg, s))  # возвращает первое  совпадение с шаблона
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
#последние 4 метода будут выбрасывать исключения
# print(re.match(reg, s))  # поиск по шаблону в начале строки
# print(re.split(reg, s, 3))  # возвращает список в котором строка разбита по шаблону
# print(re.sub(reg, "!", s))  # поиск и замена
# print(re.sub(reg, "!", s, 1))  # поиск и замена

# s = r"Я ищу совпадени_я в 2024 году. \"И я их наиду\" в 2 счёта. [1398765]. Hel-lo"
# # reg = r"[204]"
# # reg = r"[2-4]"
# reg = r"[12][09][0-9][0-9]"  # 200[00]  19[00]  # 1103-1040
# print(re.findall(reg, s))
# print(ord("А"))  # 1040
# print(ord("Я"))  # 1071
# print(ord("а"))  # 1072
# print(ord("я"))  # 1103
# print(ord("ё"))  # 1105
# print(ord("Ё"))  # 1025
# print(chr(96))

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:65. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# pattern = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(pattern, st))


# часто применяется
# s = "Я ищу совпадения в 2024 году. И я их наиду в 2 счёта.Hel-lo 20000000"
# reg = r"\d"  # [0-9]
# reg = r"\D"  # [^0-9]
# reg = r"\s"  # [ ]
# reg = r"\S"  # [ ] поиск чего угодно кроме пробелов
# reg = r"\w"  # [0-9A-zА-я_]
# reg = r"\W"  # [^0-9A-zА-я_]
# reg = r"\АИя"
# reg = r"\году.Z"
# reg = r"\Bния"
# reg = r"\w+"
# reg = r"\d+"
# reg = r"20*"
# print(re.findall(reg, s))

# Количество повторении текущих элементов      квантификаторы
# + - от 1 до бесконечности
# * - от 0 до бесконечно
# ? - от 0 до одного повторения


# d = "Цифры: 7, +17, --42, 0013, 0.3456"
# print(re.findall(r"[+-]?\d+[.\d]*", d))

# st = "05-06-1987 # Дата рождения"

# print("Дата рождения:", re.sub(r"\s#.*", "", st))
# # Дата рождения: 05-06-1987 => Дата рождения: 05.06.1987
# print("Дата рождения:", re.sub(r"-", ".", re.sub(r"\s#.*", "", st)))


# st = "autor=Пушкин А.С.; title = Евгении Онегин; price = 200; year= 1831"
# # pattern = r"\w+\s*=\s*[\w\s.]+"
# pattern = r"\w+\s*=\s*[^;,]+"
# print(re.findall(pattern, st))

# s1 = "12 сентября 2024 года 4565412"
# reg1 = r"\d{1,4}"
# print(re.findall(reg1, s1))

# s = r"Я ищу совпадения в 2024 году. И я их наиду в 2 счё_та."
# # reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+\.$"
# print(re.findall(reg, s))

# def valid_login(name):
#     return re.findall("[A-Za-z0-9_-]{3,16}", name)
#
#
# print(valid_login("Python_master"))
# print(valid_login("Python"))
#
# print(re.findall(r"\w+", "12 + и"))
# print(re.findall(r"\w+", "12 + и", flags=re.ASCII))
#
# text = "Hello World"
# print(re.findall(r"\w+", text, re.DEBUG))

# s = r"Я ищу совпадения в 2024 году. И я их наиду в 2 счё_та."
# reg = "я"
# print(re.findalд(reg, s, re.IGNORECASE)

#

# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+  # part 1
# @         # @
# [a-z.-]+  # part 2
# """, "test@mail.ru", re.VERBOSE))



