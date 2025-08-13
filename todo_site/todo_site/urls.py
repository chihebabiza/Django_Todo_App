from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.home, name='home'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('clear/', views.clear_all_tasks, name='clear_all_tasks'),
]
