# Assistant

Це консольний асистент, який включає в себе адресну книгу, нотатки та менеджер файлів.

## Встановлення

Для встановлення та використання цього проєкту за допомогою консольного терміналу, скористайтеся наступними кроками:

1. **Встановіть аситстент з репозиторія:**
    ```bash
    pipenv install git+https://github.com/freshdeadboy/my_first_personal_project.git
    ```

2. **Активуйте віртуальне середовище:**
    ```bash
    pipenv shell
    ```

3. **Запустіть асистента в віртуальному середовищі:**
    ```bash
    my_project_console
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

## Встановлення "Персональний помічник" та запуск як окремий додаток в окремому контейнері за допомогою Docker.    

1. **Перейдіть в директорію з вашим Dockerfile і проєктом**
cd /шлях/до/вашого/проєкту

2. **Побудуйте Docker-образ**
docker build -t my_personal_assistant .

3. **Запустіть контейнер**
docker run my_personal_assistant
