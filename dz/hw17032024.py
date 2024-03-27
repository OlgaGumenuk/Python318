arr = str("Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень хорошии язык программирования.")
n = str("N")
p = str("P")
print(arr)

arr2 = []
for x in range(len(arr)):
    if arr[x] != n:
        arr2.append(arr[x])

    else:
        arr2.append(p)
# print(arr2)

print(''.join(str(el) for el in arr2))