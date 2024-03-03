num = int(input('Введите пятизначное число: '))
a = num % 10
num //= 10
b = num % 10
num //= 10
c = num % 10
num //= 10
d = num % 10
num //= 10
e = num % 10
com = a * b * c * d * e
print("Произведение цифр числа " + str(a) + str(b) + str(c) + str(d) + str(e) + ": " + str(com))
arith_mean = com / 5
print("Среднее арифметическое: " + str(arith_mean))
