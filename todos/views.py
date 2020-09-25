from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.urls import reverse

from .models import Todo

class TodoList(ListView):
    template_name = 'todos/todos.html'
    context_object_name= 'todos'

    # Lo que devuelve esta funcion se añade al context object name
    def get_queryset(self):
        return Todo.objects.all()

def new_todo(request):
    new = Todo(
        todo_title=request.POST['title'],
        todo_text=request.POST['task'],
        todo_date=timezone.now()
    )
    new.save()
    return HttpResponseRedirect(reverse('todos:index'))

def delete_todo(request, todo_id):
    try:
        completed = request.POST['completed']
        if completed:
            deleted = Todo.objects.get(pk=todo_id)
            deleted.delete()
    except:
        pass
        
    
    return HttpResponseRedirect(reverse('todos:index'))





    



