from django.urls import path
from .views import TodoListView, todo_create
from .views import TodoListView, TodoCreateView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('create/', todo_create, name='todo_create'),
    path('create/', TodoCreateView.as_view(), name='todo_create'),
]