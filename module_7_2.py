import os


def custom_write(file_name, strings):
    strings_positions = {}
    number_string = 1
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            pass  # создаем пустой файл, если его нет
    file = open(file_name, 'a', encoding='utf-8')
    for new_string in strings:
        strings_positions[(number_string, file.tell())] = new_string
        file.write(f'{new_string}\n')
        number_string += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
