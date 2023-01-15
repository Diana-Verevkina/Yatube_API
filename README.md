## API Yatube
api_final_yatube

### Описание:
Программа представляет из себя API для социальной сети Yatube, с помощью 
которого можно публиковать и редактировать записи и 
просматривать посты других пользователей. Реализованы механизм комментариев 
к записям, возможность подписки на публикации интересующих авторов и 
регистрация пользователей.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:Diana-Verevkina/Yatube_API.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Документация:

http://127.0.0.1:8000/redoc/