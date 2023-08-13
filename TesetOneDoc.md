# Started: 
![read](cheatsheet.png)

## Opened VS code and then creating the virtual environment
`put a full stop  at the end of the command point to the current directory`
```bash
python -m venv .
```

## activate the virtual environment
```bash
Scripts\activate
deactivate
```

## navigate to directory and isntall django
```bash
pip install django
py -3 -m django --version
```

## create a new Django project
`put a full stop  at the end of the command point to the current directory`
```bash
django-admin startproject projectname .
```
## runs servers
```bash
python manage.py runserver
```

## create a new app
`What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.`
```bash
py manage.py startapp playground
```

## now we need to register the app in the settings module
`
we write the app's name to the settings module under the *INSTALLED_APPS* after the comma between single qoutations ' '
`

## we will write a request/response function in the views.py file
```py
from django.http import HttpResponse

def say_hello(response):
    return HttpResponse('Hello World')
```

## we will then map it to the urls `3 ways but only will note of 2, you can learned third way from urls.py`
## 1)
`add this code to the urls.py file in main project. this will directly link urls and views`
```py
from playground import views
path('hello/', views.say_hello),
```
`http://127.0.0.1:8000/hello/ is the url`
## 2)
`create a urls.py file in the app directory and add this code to it to link views to it. `
```py
from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.say_hello),
]
```
`now we can link the created urls file to the main urls.py. we can see the path is empty here, if we add a path then we will have to include it in the browser`
```py
from django.urls import path,include
path('', include('playground.urls')),
```
`http://127.0.0.1:8000/hello/ is the url here`

## create templates and link it
`We will create a folder in the app directory inside it add a html file with html code`
`in views.py we will use the render function to render a template to return markup language to client`

`views.py page`
```py
def say_hello(request):
    return render(request, 'index.html', {'name': 'SaidMustafa'})
```
`index.html page`
```html
<h1>Hello html</h1>
<h2>welcome {{name}}</h2>
```

## installation of debug toolbar
[dejango debug toolbar installation](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

### Run the following command in the terminal to create the database tables based on the models you just defined:
```bash
python manage.py makemigrations
python manage.py migrate
```
