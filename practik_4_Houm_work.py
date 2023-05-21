# lists = 'a a a b c a a d c d d'.split()
# print(lists)
#
# lists_2 = []
# counts = {}
#
# for i in lists:
#     if i not in counts:
#         counts[i] = 1
#         lists_2.append(i)
#     else:
#         s = i + '_' + str(counts[i])
#         counts[i] += 1
#         lists_2.append(s)
#
# print(lists_2)

# numbers = '+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890'.split()
# dict_numbers = {}
#
# for i in range(len(numbers)):
#     # print(numbers[i][0:2])
#     if numbers[i][0:2] not in dict_numbers:
#         dict_numbers[numbers[i][0:2]] = [numbers[i]]
#     else:
#         dict_numbers[numbers[i][0:2]].append(numbers[i])
# print(dict_numbers)


# a, b = map(int, input('Введите 2 числа длинн массива через пробел: ').split())
# num1 = set()
# num2 = set()
# print(f'Введите {a} чисел первого массива')
# print()
# for i in range(1, a + 1):
#     num1.add(int(input(f'Введите {i} число: ')))
# print(f'Введите {b} чисел второго массива')
# print()
# for i in range(1, b + 1):
#     num2.add(int(input(f'Введите {i} число: ')))
# print('Пересекаемые числа: ', *sorted(num1 & num2))


N = int(input())
berri = list(map(int, input().split()))

max_sum = 0
for i in range(N):
    curr_sum = berri[i] + (berri[i - 1] if i > 0 else 0) + (berri[i + 1] if i < N - 1 else 0)
    max_sum = max(max_sum, curr_sum)

print(max_sum)
