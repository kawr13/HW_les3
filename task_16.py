# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X


n = int(input("Введите количество элементов в массиве: "))
count = 0
# Вводим элементы массива
arr = []
for i in range(n):
    arr.append(int(input('Введите элемент массива: ')))

# Вводим число X, к которому нужно найти самый близкий элемент
x = int(input("Введите число X: "))

for i in range(n):
    if arr[i] == x:
        count += 1

print(f'{x} встречается {count} раз')