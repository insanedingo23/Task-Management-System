from django import forms
from .models import TasksModel, CategoryModel

class TasksModelForm(forms.ModelForm):
    class Meta:
        model = TasksModel
        fields = ['tname', 'cat', 'desc', 'tstatus']

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['cat']
