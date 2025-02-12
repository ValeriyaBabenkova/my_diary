from django import forms
from django.core.exceptions import ValidationError
from .models import Note, NoteCategory
class NoteAddForm(forms.Form):
    date = forms.DateField(label='Дата')
    text = forms.CharField(label='Текст', widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=NoteCategory.objects.all(),
                                      label='Категория'
                                      )
