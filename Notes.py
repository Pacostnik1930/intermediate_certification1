import json
import os

# Имя файла для хранения заметок
filename = "notes.json"

# Функция для создания файла, если он не существует
def create_file():
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump([], file)

# Функция для чтения заметок из файла
def read_notes():
    with open(filename, "r") as file:
        notes = json.load(file)
    return notes

# Функция для добавления новой заметки
def add_note():
    notes = read_notes()
    note_content = input("Введите содержимое заметки: ")
    notes.append(note_content)
    with open(filename, "w") as file:
        json.dump(notes, file)

# Функция для вывода списка заметок
def list_notes():
    notes = read_notes()
    for i, note in enumerate(notes):
        print(f"{i+1}. {note}\n")

# Функция для редактирования заметки
def edit_note():
    notes = read_notes()
    note_index = int(input("Введите номер заметки для редактирования: "))
    note_content = input("Введите новое содержимое заметки: ")
    notes[note_index-1] = note_content
    with open(filename, "w") as file:
        json.dump(notes, file)

# Функция для удаления заметки
def delete_note():
    notes = read_notes()
    note_index = int(input("Введите номер заметки для удаления: "))
    del notes[note_index-1]
    with open(filename, "w") as file:
        json.dump(notes, file)

# Создаем файл для хранения заметок, если он не существует
create_file()

# Бесконечный цикл для взаимодействия с пользователем
while True:
    print("Выберите действие:")
    print("1. Добавить заметку")
    print("2. Просмотреть список заметок")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти из программы")
    
    choice = input()

    if choice == "1":
        add_note()
    elif choice == "2":
        list_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("Неправильный выбор")
