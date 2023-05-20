# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:

words = []
lang = input("Введите язык eng или ru: ").lower()
brush = 0

if lang == "eng":
    weights = {
        'AEIOULNSTR': 1,
        'DG': 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
        'QZ': 10
    }
else:
    weights = {
        'АВКИНОРСТ': 1,
        'ДКЛМПУ': 2,
        'БГЁЬЯ': 3,
        'ЙЫ': 4,
        'ЖЗХЦЧ': 5,
        'ШЭЮ': 8,
        'ФЩЪ': 10
    }

k = input("Введите слово: ").upper()
for i in range(len(k)):
    for keys, value in weights.items():
        if k[i] in keys:
            brush += value
            break

print("Количество очков: ", brush)

#
# lang = input("Введите язык eng или ru: ").title()
# brush = 0
# if lang == "Eng":
#     k = input("Введите слово: ").upper()
#     for i in range(len(k)):
#         if k[i] in 'AEIOULNSTR':
#             brush += 1
#         elif k[i]  in 'DG':
#             brush += 2
#         elif k[i]  in 'BCMP':
#             brush += 3
#         elif k[i]  in 'FHVWY':
#             brush += 4
#         elif k[i]  in 'K':
#             brush += 5
#         elif k[i]  in 'JX':
#             brush += 8
#         elif k[i]  in 'QZ':
#             brush += 10
# elif lang == "Ru":
#     k = input("Введите слово: ").upper()
#     for i in range(len(k)):
#         if k[i] in 'АВКИНОРСТ':
#             brush += 1
#         elif k[i] in 'ДКЛМПУ':
#             brush += 2
#         elif k[i] in 'БГЁЬЯ':
#             brush += 3
#         elif k[i] in 'ЙЫ':
#             brush += 4
#         elif k[i] in 'ЖЗХЦЧ':
#             brush += 5
#         elif k[i] in 'ШЭЮ':
#             brush += 8
#         elif k[i] in 'ФЩЪ':
#             brush += 10
# else:
#     print("Не выбран язык")
#     print('Досвиданье')
# print("Количество очков: ", brush)