# api-blog-weii-ink

blog use api


python 版本 `Python 3.7.4`
## install
```
pip install -r requirements.txt
```

## Migrate

```
python manage.py makemigrations
python manage.py makemigrations api
```

```
python manage.py migrate
```
or
```
python manage.py migrate --fake
```

## Start

```
python manage.py runserver 0.0.0.0:8003
```
