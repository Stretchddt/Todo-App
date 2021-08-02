from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'