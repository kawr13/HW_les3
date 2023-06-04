import json

def read_con():
	with open('contact.txt', 'r', encoding='utf-8') as file:
		content = file.read()
		if content:
			return json.loads(content)
		else:
			return {}


def writ_con(dict):
	with open('contact.txt', 'w', encoding='utf-8') as file:
		file.write(json.dumps(dict) + '\n')


def edit_contact(contact):
    field = input('Выберите поле для редактирования (fam, nam, ot, numb): ').lower()
    if field == 'fam':
        old_key = contact['fam'][0]
        new_value = input(f'Введите новое значение для поля {field}: ').lower()
        new_key = new_value[0]
        if old_key != new_key:
            dict[old_key].remove(contact)
            if not dict[old_key]:
                del dict[old_key]
            if new_key not in dict:
                dict[new_key] = []
            dict[new_key].append(contact)
        contact[field] = new_value
        print('Контакт успешно отредактирован.')
        writ_con(dict)  # Сохранение изменений в файле
    elif field in contact:
        new_value = input(f'Введите новое значение для поля {field}: ').lower()
        contact[field] = new_value
        print('Контакт успешно отредактирован.')
        writ_con(dict)  # Сохранение изменений в файле
    else:
        print('Некорректное поле. Редактирование отменено.')


def delete_contact(dict):
	fam = input('Введите фамилию: ').lower()
	for key, value in dict.items():
		dict[key] = [contact for contact in value if fam not in contact['fam']]

def add_contact(dict):
	fam = input('Введите фамилию: ').lower()
	nam = input('Введите имя: ').lower()
	ot = input('Введите отчество: ').lower()
	numb = input('Введите номер: ').lower()
	if fam[0] not in dict:
		dict[fam[0]] = []
	dict[fam[0]].append({'fam': fam, 'nam': nam, 'ot': ot, 'numb': numb})
	print('Контакт успешно добавлен.')

def search_contact(dict):
	com_2 = input('Введите all (все контакты), search (Поиск по фамилии): ')
	if com_2 == 'all':
		for key, value in dict.items():
			if value == []:
				continue
			else:
				print(f"{key.title()}")
				for contact in value:
					print(
						f"{contact['fam'].title()} {contact['nam'].title()} {contact['ot'].title()}\nномер: {contact['numb']}")
	elif com_2 == 'search':
		fam = input('Введите фамилию / имя / отчество: ').lower()
		for key, value in dict.items():
			for contact in value:
				if fam in contact['fam'] or fam in contact['nam'] or fam in contact['ot']:
					print(
						f"{contact['fam'].title()} {contact['nam'].title()} {contact['ot'].title()}\nномер: {contact['numb']}")
				else:
					print('Контакт не найден')


def main(dict):
	running = True
	while running:
		comm = input('Введите команду: ').lower()
		if comm == 'add':
			add_contact(dict)
			writ_con(dict)
		elif comm == 'print':
			print(dict)
		elif comm == 'show':
			dict = read_con()
			search_contact(dict)
		elif comm == 'delete':
			delete_contact(dict)
			writ_con(dict)
		elif comm == 'edit':
			fam = input('Введите фамилию контакта для редактирования: ').lower()
			if fam[0] in dict:
				contacts = dict[fam[0]]
				for contact in contacts:
					if contact['fam'] == fam:
						edit_contact(contact)
						writ_con(dict)
						break
				else:
					print('Контакт не найден.')
			else:
				print('Контакт не найден.')
		elif comm == 'exit':
			running = False

dict = read_con()
print(dict)
main(dict)