from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"
    context_object_name = "todo_list"

def todo_create(request):
    return HttpResponse("Página de criação de tarefas.")

from django.views.generic.edit import CreateView
from .models import Todo
from django.urls import reverse_lazy

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'deadline']
    template_name = "todo_form.html"
    success_url = reverse_lazy('todo_list')
