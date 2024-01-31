# main.py

from assistant.address_book import AddressBook, get_user_input as address_book_get_user_input
from assistant.notes import Notes
from assistant.file_manager import FileManager
import os  # Додано імпорт os

def main():
    print("Вітаємо в консольному помічнику!")

    while True:
        print("\nОберіть опцію:")
        print("1. Адресна книга")
        print("2. Нотатки")
        print("3. Менеджер файлів")
        print("4. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            address_book_menu()
        elif choice == '2':
            notes_menu()
        elif choice == '3':
            file_manager_menu()
        elif choice == '4':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

def address_book_menu():
    # Додано імпорт PrettyTable, Colorama та Style
    from prettytable import PrettyTable
    from colorama import Fore, Style

    address_book = AddressBook()

    while True:
        print("\nОберіть опцію для Адресної книги:")
        print("1. Додати контакт")
        print("2. Показати список контактів")
        print("3. Вийти в попереднє меню")

        choice = input("Ваш вибір: ")

        if choice == '1':
            address_book_add_contact(address_book)
        elif choice == '2':
            address_book.display_contacts()
        elif choice == '3':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

def address_book_add_contact(address_book):
    name, address, phone, email, birthday = address_book_get_user_input()
    address_book.add_contact(name, address, phone, email, birthday)
    print("Контакт додано!")

def notes_menu():
    # Додано імпорт PrettyTable, Colorama та Style
    from prettytable import PrettyTable
    from colorama import Fore, Style

    notes = Notes()

    while True:
        print("\nОберіть опцію для Нотатків:")
        print("1. Додати нотатку")
        print("2. Показати список нотаток")
        print("3. Вийти в попереднє меню")

        choice = input("Ваш вибір: ")

        if choice == '1':
            notes_add_note(notes)
        elif choice == '2':
            notes.display_notes()
        elif choice == '3':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

def notes_add_note(notes):
    text = input("Введіть текст нотатки: ")
    tags = input("Введіть теги (через кому): ").split(',')
    notes.add_note(text, [tag.strip() for tag in tags])
    print("Нотатку додано!")

def file_manager_menu():
    file_manager = FileManager()

    while True:
        print("\nОберіть опцію для Менеджера файлів:")
        print("1. Показати файли у папці")
        print("2. Сортувати файли за категоріями")
        print("3. Вийти в попереднє меню")

        choice = input("Ваш вибір: ")

        if choice == '1':
            file_manager_show_files(file_manager)
        elif choice == '2':
            file_manager.sort_files_by_category()
        elif choice == '3':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

def file_manager_show_files(file_manager):
    print("Файли у папці:")
    files = os.listdir(file_manager.folder_path)
    for file in files:
        print(file)

if __name__ == "__main__":
    main()
