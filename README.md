# VPS Manager

> [Техническое задание](./TASKS.md)

---

## Описание проекта

VPS Manager - сервис для управления виртуальными серверами. С помощью этого API пользователи могут:

- создавать виртуальные серверы,
- управлять характеристиками серверов:
    - процессоры;
    - оперативная память;
    - дисковое пространство.
- изменять статус серверов:
    - запущен - `started`;
    - заблокирован - `blocked`;
    - остановлен - `stopped`.
- фильтровать и сортировать серверы по параметрам.

---

## Стек технологий

- Python 3
- Django 4
- Django REST Framework (DRF)
- PostgreSQL
- Django Filter
- Simple JWT
- coverage

## Как запустить проект

Шаги для локального запуска проекта:

1. Клонировать репозиторий и перейти в директорию проекта:

```bash
git clone https://github.com/yuldashov10/vps_manager.git && cd vps_manager
```

2. Создать виртуальное окружение и активировать его:

    - **Windows (GitBash)**:

      ```bash
      python -m venv .venv
      source .venv\Scripts\activate
      ```

    - **MacOS/Linux**:

      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```

3. Установить зависимости:

    ```bash
    pip3 install -r requirements.txt
    ```

4. Настроить переменные окружения:

- Создайте файл `.env` и добавьте параметры из `.env.sample`.

5. Применить миграции базы данных:

    ```bash
    python3 manage.py migrate
    ```

6. Создать суперпользователя:

    ```bash
    python3 manage.py createsuperuser
    ```

7. Запустить сервер:

    ```bash
    python3 manage.py runserver
    ```

Сервис будет доступен по адресу: http://127.0.0.1:8000/

---

## Эндпоинты API

### Документация API

- Redoc - http://127.0.0.1:8000/redoc/
- Swagger - http://127.0.0.1:8000/swagger/

### Управление VPS:

- `GET /api/vps/` - получить список всех серверов;
- `GET /api/vps/?status=started` - получить список серверов с фильтрацией по статусу;
- `GET /api/vps/{uid}/` - получить информацию о конкретном сервере;
- `POST /api/vps/` - создать новый сервер;
- `PUT /api/vps/{uid}/` - обновить характеристики сервера;
- `DELETE /api/vps/{uid}/` - удалить сервер.

---

## Запуск тестов

- Для запуска тестов выполнить команду

```bash
coverage run --source='.' manage.py test
```

- Проверьте статус тестового покрытия проекта:

```bash
coverage report
```

---

## Автор

**Шохрух Юлдашов** | [Telegram](https://t.me/shyuldashov)
