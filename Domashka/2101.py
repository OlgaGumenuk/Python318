n = int(input("Введите число от 1 до 99: "))
if 1 <= n <= 99:
    if n == 1 or n == 21 or n == 31 or n == 41 or n == 51 or n == 61 or n == 71 or n == 81 or n == 91:
        print(n, "копеика")
    if 2 <= n <= 4 or 22 <= n <= 24 or 32 <= n <= 34 or 42 <= n <= 44 or 52 <= n <= 54 or 62 <= n <= 64:
        print(n, "копеики")
    if 72 <= n <= 74 or 82 <= n <= 84 or 92 <= n <= 94:
        print("копеики")
    if 5 <= n <= 20 or 25 <= n <= 30 or 35 <= n <= 40 or 45 <= n <= 50 or 55 <= n <= 60 or 65 <= n <= 70:
        print(n, "копеек")
    if 75 <= n <= 80 or 85 <= n <= 90 or 95 <= n <= 99:
        print(n, "копеек")
else:
    print("Ошибка ввода данных")