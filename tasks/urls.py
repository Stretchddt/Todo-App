from django.urls import path
from .views import home_view, tasks_view, category_view, edit_task_view, delete_task_view

urlpatterns = [
    path('', home_view, name='home_page'),
    path('tasks/<str:category>/', tasks_view, name='tasks_page'),
    path('categories/', category_view, name='create_category'),
    path('edit-task/<str:pk>/', edit_task_view, name='edit_task'),
    path('delete-task/<str:pk>/', delete_task_view, name='delete_task'),
]