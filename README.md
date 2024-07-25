# Todo_Site

This is a simple Django-based TODO list web application that allows users to add, view, and remove tasks. The project structure and essential code snippets are provided below.

## Project Structure
```
todo_site/
├── manage.py
├── todo_site/
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
└── todo/
    ├── init.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations/
    ├── models.py
    ├── tests.py
    └── views.py
```


## Setup Instructions

### Step 1: Create and Setup Django Project and App
```bash
django-admin startproject todo_site
cd todo_site
python manage.py startapp todo
```

### Step 2: Create and Setup Django Project and App
Add todo to INSTALLED_APPS:
```bash
INSTALLED_APPS = [
    ...
    'todo',
]
```
Add templates directory:
```bash
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
```

### Step 3: Update urls.py
Add the following paths to urlpatterns:
```bash
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name="todo"),
    path('del/<str:item_id>', views.remove, name="del"),
]
```

### Models
#### models.py
Define the Todo model:
```bash
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```
### Forms
#### forms.py
Create a form for the Todo model:
```bash
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']
```

### Views
#### views.py
Handle requests and responses:
```bash
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

def index(request):
    item_list = Todo.objects.order_by("-date")
    
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    
    form = TodoForm()
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    item = get_object_or_404(Todo, id=item_id)
    item.delete()
    messages.info(request, "Item removed!")
    return redirect('todo')
```

### Templates
#### index.html
```bash
<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
    <meta charset="utf-8">
    <title>{{title}}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <style>
        .card {
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.5), 0 6px 20px 0 rgba(0, 0, 0, 0.39);
            background: lightpink;
            margin-bottom: 5%;
            border-radius: 25px;
            padding: 2%;
            overflow: auto;
            resize: both;
            text-overflow: ellipsis;
        }
        .card:hover {
            background: lightblue;
        }
        .submit_form {
            text-align: center;
            padding: 3%;
            background: pink;
            border-radius: 25px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.4), 0 6px 20px 0 rgba(0, 0, 0, 0.36);
        }
    </style>
</head>

<body class="container-fluid">
    {% if messages %}
    {% for message in messages %}
    <div class="alert alert-info">
        <strong>{{message}}</strong>
    </div>
    {% endfor %}
    {% endif %}

    <center class="row">
        <h1><i>__TODO LIST__</i></h1>
        <hr />
    </center>

    <div class="row">
        <div class="col-md-8">
            {% for i in list %}
            <div class="card">
                <center><b>{{i.title}}</b></center>
                <hr />
                {{i.date}}
                <hr />
                {{i.description}}
                <br />
                <br />
                <form action="/del/{{i.id}}" method="POST" style=" padding-right: 4%; padding-bottom: 3%;">
                    {% csrf_token %}
                    <button value="remove" type="submit" class="btn btn-primary" style="float: right;"><span class="glyphicon glyphicon-trash"></span> remove</button>
                </form>
            </div>
            {% endfor %}
        </div>
        <div class="col-md-1"></div>
        <div class="col-md-3">
            <div class="submit_form">
                <form method="POST">
                    {% csrf_token %}
                    {{forms}}
                    <center>
                        <input type="submit" class="btn btn-default" value="submit" />
                    </center>
                </form>
            </div>
        </div>
    </div>
</body>

</html>
```

### Running the Project
Apply migrations and run the server:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser to see the TODO list application in action.# Python_Django_Todo_Site
