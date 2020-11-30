from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    Title = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Add A new task'}))
    class Meta:
        model = Task
        fields = '__all__'
