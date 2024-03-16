import random

matrix = [[random.randint(-10,20) for x in range(3)] for y in range(4)]

count = 0
for d in matrix:
    for x in d:
        if x < 0:
            count += 1
        print(x, end="\t\t")
    print()
print("Количество отрицательных элементов: ", count)








