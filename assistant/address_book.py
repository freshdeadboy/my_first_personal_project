# address_book.py

import json
import os
from datetime import datetime, timedelta
import re
from prettytable import PrettyTable
from colorama import Fore, Style
from dateutil import parser


class AddressBook:
    def __init__(self, file_path='data/contacts.json'):
        self.file_path = os.path.abspath(file_path)
        self.contacts = self.load_contacts()
        self.create_file_if_not_exists()
        
    def create_file_if_not_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)    

    def load_contacts(self):
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_contacts(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.contacts, file, indent=2)

    def add_contact(self, name, address, phone, email, birthday):
        contact = {
            'name': name,
            'address': address,
            'phone': phone,
            'email': email,
            'birthday': birthday
        }
        self.contacts.append(contact)
        self.save_contacts()

    def display_contacts(self):
        table = PrettyTable()
        table.field_names = [
            f"{Fore.RED}#", 
            f"{Fore.GREEN}Ім'я", 
            f"{Fore.BLUE}Адреса", 
            f"{Fore.YELLOW}Телефон", 
            f"{Fore.MAGENTA}Email", 
            f"{Fore.CYAN}День народження{Style.RESET_ALL}"
        ]

        for index, contact in enumerate(self.contacts, start=1):
            table.add_row([
                f"{Fore.RED}{index}", 
                f"{Fore.GREEN}{contact['name']}", 
                f"{Fore.BLUE}{contact['address']}", 
                f"{Fore.YELLOW}{contact['phone']}", 
                f"{Fore.MAGENTA}{contact['email']}", 
                f"{Fore.CYAN}{contact['birthday']}{Style.RESET_ALL}"
            ])

        print(table)

    def display_upcoming_birthdays(self, days):
        today = datetime.now()

        upcoming_birthdays = []

        for contact in self.contacts:
            try:
                birthday_date = datetime.strptime(contact['birthday'], '%Y-%m-%d')
            except ValueError:
                print(f"Помилка: Невірний формат дати для контакту {contact['name']}.")
                continue

            next_birthday = datetime(today.year, birthday_date.month, birthday_date.day)

            if today > next_birthday:
                next_birthday = datetime(today.year + 1, birthday_date.month, birthday_date.day)

            days_until_birthday = (next_birthday - today).days

            if 0 < days_until_birthday <= days:
                upcoming_birthdays.append(contact)

        if upcoming_birthdays:
            print(f"\nКонтакти з днем народження через {days} днів:")
            table = PrettyTable()
            table.field_names = [
                f"{Fore.GREEN}Ім'я", 
                f"{Fore.BLUE}Адреса", 
                f"{Fore.YELLOW}Телефон", 
                f"{Fore.MAGENTA}Email", 
                f"{Fore.CYAN}День народження{Style.RESET_ALL}"
            ]

            for contact in upcoming_birthdays:
                table.add_row([
                    f"{Fore.GREEN}{contact['name']}", 
                    f"{Fore.BLUE}{contact['address']}", 
                    f"{Fore.YELLOW}{contact['phone']}", 
                    f"{Fore.MAGENTA}{contact['email']}", 
                    f"{Fore.CYAN}{contact['birthday']}{Style.RESET_ALL}"
                ])

            print(table)
        else:
            print(f"\nНемає контактів з днем народження через {days} днів.")

    def edit_contact(self, index, name, address, phone, email, birthday):
        contact = {
            'name': name,
            'address': address,
            'phone': phone,
            'email': email,
            'birthday': birthday
        }
        self.contacts[index] = contact
        self.save_contacts()

    def search_contacts(self, keyword):
        results = []

        for contact in self.contacts:
            contact_info = f"{contact['name']} {contact['address']} {contact['phone']} {contact['email']} {contact['birthday']}"
            if keyword.lower() in contact_info.lower():
                results.append(contact)

        return results

# Змінений консольний інтерфейс для введення даних та редагування
def get_user_input():
    name = input("Ім'я: ")
    while not name:
        print("Поле пусте. Будь ласка, введіть ім'я.")
        name = input("Ім'я: ")

    address = input("Адреса: ")
    while not address:
        print("Поле пусте. Будь ласка, введіть адресу.")
        address = input("Адреса: ")

    while True:
        try:
            phone = input("Номер телефону: ")
            if not re.match(r'^\+[0-9]+$', phone):
                raise ValueError("Невірний формат телефону. Введіть у міжнародному форматі, наприклад, +123456789.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            email = input("Email: ")
            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                raise ValueError("Невірний формат Email. Введіть у форматі example@example.com.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            birthday = input("Дата народження (рік-місяць-день): ")
            parsed_birthday = parser.parse(birthday)
            break
        except ValueError:
            print("Невірний формат дня народження. Спробуйте ще раз.")

    return name, address, phone, email, parsed_birthday.strftime('%Y-%m-%d')

# Приклад використання:
if __name__ == "__main__":
    address_book = AddressBook()

    while True:
        print("\n1. Додати контакт")
        print("2. Показати список контактів")
        print("3. Вивести контакти з днем народження через задану кількість днів")
        print("4. Редагувати контакт")
        print("5. Пошук контактів за словом або датою")
        print("6. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            name, address, phone, email, birthday = get_user_input()
            address_book.add_contact(name, address, phone, email, birthday)
            print("Контакт додано!")
        elif choice == '2':
            print("Список контактів:")
            address_book.display_contacts()
        elif choice == '3':
            try:
                days = int(input("Введіть кількість днів: "))
                address_book.display_upcoming_birthdays(days)
            except ValueError:
                print("Невірний формат кількості днів. Будь ласка, введіть ціле число.")
        elif choice == '4':
            try:
                index = int(input("Введіть номер контакту для редагування: ")) - 1
                if 0 <= index < len(address_book.contacts):
                    name, address, phone, email, birthday = get_user_input()
                    address_book.edit_contact(index, name, address, phone, email, birthday)
                    print("Контакт відредаговано!")
                else:
                    print("Невірний номер контакту.")
            except ValueError:
                print("Невірний формат номера контакту.")
        elif choice == '5':
            keyword = input("Введіть слово або дату для пошуку: ")
            search_results = address_book.search_contacts(keyword)
            if search_results:
                print("Результати пошуку:")
                table = PrettyTable()
                table.field_names = [
                    f"{Fore.RED}#", 
                    f"{Fore.GREEN}Ім'я", 
                    f"{Fore.BLUE}Адреса", 
                    f"{Fore.YELLOW}Телефон", 
                    f"{Fore.MAGENTA}Email", 
                    f"{Fore.CYAN}День народження{Style.RESET_ALL}"
                ]

                for index, contact in enumerate(search_results, start=1):
                    table.add_row([
                        f"{Fore.RED}{index}", 
                        f"{Fore.GREEN}{contact['name']}", 
                        f"{Fore.BLUE}{contact['address']}", 
                        f"{Fore.YELLOW}{contact['phone']}", 
                        f"{Fore.MAGENTA}{contact['email']}", 
                        f"{Fore.CYAN}{contact['birthday']}{Style.RESET_ALL}"
                    ])

                print(table)
            else:
                print("Нічого не знайдено.")
        elif choice == '6':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
