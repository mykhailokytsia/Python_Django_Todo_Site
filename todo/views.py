from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

def index(request):
    print("Index view called")
    item_list = Todo.objects.order_by("-date")
    print("Item list:", item_list)
    
    if request.method == "POST":
        print("POST request detected")
        form = TodoForm(request.POST)
        print("Form data:", request.POST)
        
        if form.is_valid():
            print("Form is valid")
            form.save()
            print("Form saved")
            return redirect('todo')
        else:
            print("Form is invalid:", form.errors)
    
    form = TodoForm()
    print("Empty form initialized")
    
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    print("Context prepared:", page)
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    print("Remove view called with item_id:", item_id)
    item = get_object_or_404(Todo, id=item_id)
    print("Item to be removed:", item)
    item.delete()
    print("Item deleted")
    messages.info(request, "Item removed!")
    return redirect('todo')
