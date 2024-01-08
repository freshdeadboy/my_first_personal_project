# notes.py

import json
import os
from prettytable import PrettyTable
from colorama import Fore, Style

class Notes:
    def __init__(self, file_path='data/notes.json'):
        self.file_path = file_path
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_notes(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.notes, file, indent=2)

    def add_note(self, text, tags=None):
        note = {
            'text': text,
            'tags': tags or []
        }
        self.notes.append(note)
        self.save_notes()

    def display_notes(self, notes=None):
        if notes is None:
            notes = self.notes

        table = PrettyTable()
        table.field_names = [
            f"{Fore.RED}#", 
            f"{Fore.GREEN}Текст", 
            f"{Fore.BLUE}Теги{Style.RESET_ALL}"
        ]

        for index, note in enumerate(notes, start=1):
            table.add_row([
                f"{Fore.RED}{index}", 
                f"{Fore.GREEN}{note['text']}", 
                f"{Fore.BLUE}{', '.join(note['tags'])}{Style.RESET_ALL}"
            ])

        print(table)

    def search_notes(self, keyword):
        results = []

        for index, note in enumerate(self.notes, start=1):
            note_info = f"{note['text']} {', '.join(note['tags'])}"
            if keyword.lower() in note_info.lower():
                results.append(note)

        return results

    def sort_notes_by_tag(self, tag):
        sorted_notes = [note for note in self.notes if tag.lower() in [t.lower() for t in note['tags']]]
        return sorted_notes

    def edit_note(self, index, new_text, new_tags=None):
        if 1 <= index <= len(self.notes):
            note = self.notes[index - 1]
            note['text'] = new_text
            note['tags'] = new_tags or note['tags']
            self.save_notes()
            print(f"Нотатку #{index} відредаговано!")
        else:
            print("Невірний індекс нотатки.")

    # Додана функція get_user_input
    def get_user_input(self):
        text = input("Введіть текст нотатки: ")
        tags = input("Введіть теги (через кому): ").split(',')
        return text, [tag.strip() for tag in tags]

# Приклад використання:
if __name__ == "__main__":
    notes = Notes()

    while True:
        print("\n1. Додати нотатку")
        print("2. Показати список нотаток")
        print("3. Пошук нотаток за словом або тегом")
        print("4. Сортувати нотатки за тегом")
        print("5. Редагувати нотатку")
        print("6. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            text, tags = notes.get_user_input()
            notes.add_note(text, tags)
            print("Нотатку додано!")
        elif choice == '2':
            print("Список нотаток:")
            notes.display_notes()
        elif choice == '3':
            keyword = input("Введіть слово або тег для пошуку: ")
            search_results = notes.search_notes(keyword)
            if search_results:
                print("Результати пошуку:")
                notes.display_notes(search_results)
            else:
                print("Нічого не знайдено.")
        elif choice == '4':
            tag = input("Введіть тег для сортування: ")
            sorted_notes = notes.sort_notes_by_tag(tag)
            if sorted_notes:
                print(f"Сортовані нотатки за тегом '{tag}':")
                notes.display_notes(sorted_notes)
            else:
                print(f"Нічого не знайдено за тегом '{tag}'.")
        elif choice == '5':
            index = int(input("Введіть номер нотатки для редагування: "))
            new_text = input("Введіть новий текст нотатки: ")
            new_tags = input("Введіть нові теги (через кому): ").split(',')
            notes.edit_note(index, new_text, [tag.strip() for tag in new_tags])
        elif choice == '6':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")