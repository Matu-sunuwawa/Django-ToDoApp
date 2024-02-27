from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ToDoForm
from .models import ToDoApp

# Create your views here.

# def hello(request):
#     return HttpResponse("Hello World")

def lists(request):
    lists = ToDoApp.objects.all()

    context = {'lists':lists}
    return render(request, 'todoapp/lists.html', context)

def add_list(request):
    forms = ToDoForm()

    if request.method=="POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            new_item=form.save()
            return redirect('/todoapp/list')
    else:
        form = ToDoForm()
    
    context = {'form':forms}
    return render(request, 'todoapp/add_list.html', context)


def update_list(request, pk):
    list = ToDoApp.objects.get(id=pk)
    form = ToDoForm(instance=list) #indicate that this form is for "editing an existing object rather than creating a new one".

    if request.method=="POST":
        form = ToDoForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('/todoapp/list')
    else:
        form = ToDoForm(instance=list)

    context = {'form':form, 'list':list}
    return render(request, 'todoapp/update_lists.html', context)

def delete_list(request, pk):
    list = ToDoApp.objects.get(id=pk)

    if request.method=="POST":
        list.delete()
        return redirect('/todoapp/list')
    
    context = {'list':list}
    return render(request, 'todoapp/delete_list.html', context)

