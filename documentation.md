.\Scripts\Activate

deactivate

python manage.py createsuperuser

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

```sh
git add .

git commit -m " "

git push -u origin main

git status
```

```sh
python manage.py shell
```

```py
with open('script.py') as f:
    script_code = f.read()
exec(script_code)
```

