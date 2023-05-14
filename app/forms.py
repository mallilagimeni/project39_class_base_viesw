from app.models import *
from django import forms
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'