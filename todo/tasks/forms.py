from django.forms import ModelForm
from django.forms.widgets import Input
from .models import Task

class TaskForm(ModelForm):
  class Meta:
    model = Task
    fields = '__all__'
    widgets = {
      'title': Input(attrs={'class': 'input',})
    }