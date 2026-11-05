from django import forms
from  .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('datetime',)

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('datetime',)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)

class UpdateTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
