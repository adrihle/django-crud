from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.TodoList.as_view(), name='index'),
    path('new/', views.new_todo, name='new'),
    path('<int:todo_id>/delete', views.delete_todo, name='delete')
]
