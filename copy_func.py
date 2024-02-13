def copy_row_to_file(file_name, new_file, row_number):
    file_data = read_file(file_name)
    if 1 <= row_number <= len(file_data):
        row_to_copy = file_data[row_number - 1]
        with open(new_file, 'a', encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Номер телефона'])
            f_writer.writerow(row_to_copy)
        print(f"Строка номер {row_number} скопирована из файла {file_name} в файл {new_file}")
    else:
        print("Некорректный номер строки")

# вставить вместо заглушки
copy_row_to_file(file_name, new_file, int(input("Введите номер строки для копирования: ")))