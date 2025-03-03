from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('toggle_done/<int:todo_id>/', views.toggle_done, name='toggle_done'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]
