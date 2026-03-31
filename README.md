# Образовательный тренажер для изучение иностранного языка
Концепция: языковой тренажёр с карточками
Пользователь может:
- просматривать списки карточек по темам;
- добавлять и редактировать карточки (слово, перевод, иллюстрация);
- проходить квиз на запоминание слов;
- видеть статистику своих результатов.

## Запуск проекта

- Клонировать репозиторий и перейти в него в командной строке.
- Установите и активируйте виртуальное окружение c учетом версии Python 3.9.10:

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

```bash
python -m pip install --upgrade pip
```

```bash
В корневом каталоге создайте файл .env
SECRET_KEY=django-insecure-5mt(gh29+ab8@3t5x+9iy5d6oxk+2a$ql%x)b1fi49-sz=vni
ALLOWED_HOSTS=127.0.0.1
```

- Затем нужно установить все зависимости из файла requirements.txt

```bash
cd languageflash
```

```bash
pip install -r requirements.txt
```

- Выполняем миграции:

```bash
python manage.py migrate
```

- Создаем суперпоьзователя для работы с админ зоной:

```bash
python manage.py createsuperuser
```

- Запускаем проект:

```bash
python manage.py runserver
```
