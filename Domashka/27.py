# k = int(input("Введите количество символов: "))
# t = input("Введите тип символа: ")
# _ = int(input("0 - горизонтальная \n1 - вертикальная \nориентация линии: "))
# while _ < 2:
#     if _ == 0:
#         print((t + " ") * k, end=" ")
#         break
#     if _ == 1:
#         print((t + "\n") * k)
#         break
#     else:
#         print("Ошибка ввода данных")




#домашнее за 10 или 09 февраля
# from random import randint

# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))

#
# tpl1 = ran(0, 5)
# tpl2 = ran(-5, 0)
# print(tpl1)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 =", tpl3.count(0))


#домашнее за 18февраля
d = {
    "emp1": {"name": "John", "salary":  7500},
    "emp2": {"name": "Emma", "salary":  8000},
    "emp3": {"name": "Brad", "salary":  6500},
}

print(d['emp3'])
print(d['emp3']['salary'])
d['emp3']['salary'] = 8500

for i in d:
    print(i)
    for j in d[i]:
        print("\t", j, ":", d[i][j])
#второи способ
# for i in d:
#     print(i)
#     for j, v in d[i].items():
#         print("\t", j, ":", v)