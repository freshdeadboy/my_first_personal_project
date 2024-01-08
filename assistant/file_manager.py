# file_manager.py

import os
import shutil

class FileManager:
    def __init__(self):
        self.folder_path = self.get_folder_path()
        self.create_folder_if_not_exists()

    def get_folder_path(self):
        folder_path = input("Введіть шлях до папки для сортування файлів: ")
        return os.path.abspath(folder_path)

    def create_folder_if_not_exists(self):
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def sort_files_by_category(self):
        files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]
        
        for file in files:
            category = self.get_file_category(file)
            category_folder = os.path.join(self.folder_path, category)

            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            file_path = os.path.join(self.folder_path, file)
            new_file_path = os.path.join(category_folder, file)

            shutil.move(file_path, new_file_path)
            print(f"Файл '{file}' був переміщений у папку '{category}'.")

    def get_file_category(self, filename):
        image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
        document_extensions = ['.doc', '.docx', '.pdf', '.txt']
        video_extensions = ['.mp4', '.avi', '.mkv', '.mov']

        _, file_extension = os.path.splitext(filename)

        if file_extension.lower() in image_extensions:
            return 'зображення'
        elif file_extension.lower() in document_extensions:
            return 'документи'
        elif file_extension.lower() in video_extensions:
            return 'відео'
        else:
            return 'інше'

# Приклад використання:
if __name__ == "__main__":
    file_manager = FileManager()

    while True:
        print("\n1. Показати файли у папці")
        print("2. Сортувати файли за категоріями")
        print("3. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            print("Файли у папці:")
            files = os.listdir(file_manager.folder_path)
            for file in files:
                print(file)
        elif choice == '2':
            file_manager.sort_files_by_category()
        elif choice == '3':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")