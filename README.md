# Store - Онлайн магазин одежды

## Описание

python3.10 /
django3.2.13 /
postgres /
celery /
redis /
stripe

## Установка

1. Склонируйте репозиторий:
```
git clone https://github.com/eemptw/store
```

2. Создайте и активируйте новую виртуальную среду:
```
python3.9 -m venv ../venv
source ../venv/bin/activate
```

3. Установите пакеты:
```
pip install --upgrade pip
pip install -r requirements.txt
```

4. Запустите зависимости проекта, миграции, заполните базу данных фикстурами и т.д.:
```
./manage.py migrate
./manage.py loaddata <path_to_fixture_files>
./manage.py runserver 
```

5. Запустите сервер Redis:
```
redis-server
```

6. Запустите Celery:
```
celery -A store worker --loglevel=INFO
```


Для экспорта данных из базы данных Django в формате JSON используйте команду dumpdata:
```
./manage.py dumpdata <app_name>.<model_name> --indent 4 > <fixture_name>.json
```
