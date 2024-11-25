from django.views.generic.list import ListView
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"
    context_object_name = "todo_list"
