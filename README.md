# Assistant

Це консольний асистент, який включає в себе адресну книгу, нотатки та менеджер файлів.

## Встановлення

Для встановлення та використання цього проєкту, скористайтеся наступними кроками:

1. **Клонуйте репозиторій:**
    ```bash
    git clone https://github.com/freshdeadboy/my_first_personal_project.git
    cd assistant
    ```

2. **Встановіть залежності:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Запустіть `setup.py`:**
    ```bash
    python setup.py install
    ```

4. **Запустіть асистента:**
    ```bash
    assistant
    ```

## Використання

1. **Адресна книга:**
    - Додавання контакту: `assistant address add`
    - Перегляд списку контактів: `assistant address list`
    - Виведення контактів з днем народження через X днів: `assistant address birthday`
    - Редагування контакту: `assistant address edit`
    - Пошук контактів за словом або датою: `assistant address search`

2. **Нотатки:**
    - Додавання нотатки: `assistant notes add`
    - Перегляд списку нотаток: `assistant notes list`
    - Пошук нотаток за словом або тегом: `assistant notes search`
    - Сортування нотаток за тегом: `assistant notes sort`
    - Редагування нотатки: `assistant notes edit`

3. **Менеджер файлів:**
    - Перегляд файлів у папці: `assistant file list`
    - Сортування файлів за категоріями: `assistant file sort`

## Ліцензія

Цей проєкт розповсюджується під ліцензією [MIT](LICENSE).
