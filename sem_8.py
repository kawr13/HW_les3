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
	field = input('Выберите поле для редактирования (fam, nam, ot, numb, txt): ').lower()
	if field in contact:
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
	txt = input('Введите текст: ').lower()
	if 'contact'not in dict:
		dict['contact'] = []
	dict['contact'].append({'fam': fam, 'nam': nam, 'ot': ot, 'numb': numb, 'txt': txt})
	print('Контакт успешно добавлен.')

def search_contact(dict):
	com_2 = input('Введите all(1)(все контакты), search(2)(Поиск по фамилии): ')
	if com_2 == '1':
		for key, value in dict.items():
			if value == []:
				print('Контактов не найдено')
				continue
			else:
				print(f"{key.title()}")
				for contact in value:
					print(
						f"{contact['fam'].title()} {contact['nam'].title()} {contact['ot'].title()}\nномер: {contact['numb']}\nописание: {contact['txt']}")
					print()

	elif com_2 == '2':
		fam = input('Введите фамилию / имя / отчество: ').lower()
		found_contact = False  # Флаг для обозначения, найден ли контакт
		for key, value in dict.items():
			for contact in value:
				if fam in contact['fam'] or fam in contact['nam'] or fam in contact['ot']:
					# Устанавливаем флаг в True, если найден хотя бы один контакт
					found_contact = True
					print(f"{contact['fam'].title()} {contact['nam'].title()} {contact['ot'].title()}\nномер: {contact['numb']}\nописание: {contact['txt']}")
		if not found_contact:
			print('Контакт не найден')

def main(dict):
	running = True
	while running:
		comm = input('Введите команду (add(1), print(2), show(3), delete(4), edit(5), exit(6): ').lower()
		if comm == '1':
			add_contact(dict)
			writ_con(dict)
		elif comm == '2':
			print(dict)
		elif comm == '3':
			dict = read_con()
			search_contact(dict)
		elif comm == '4':
			delete_contact(dict)
			writ_con(dict)
		elif comm == '5':
			fam = input('Введите фамилию контакта для редактирования: ').lower()
			for value in dict.values():
				for contact in value:
					if fam in contact['fam']:
						edit_contact(contact)
						writ_con(dict)
						break
					else:
						print('Контакт не найден.')
		elif comm == '6':
			print('Программа завершена.')
			running = False
		else:
			print('Некорректная команда.')

try:
	dict = read_con()
	main(dict)
except FileNotFoundError:
	print('Файл не найден.')
finally:
	dict = {}
	writ_con(dict)
	main(dict)


