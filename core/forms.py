from django import forms
from django.core.exceptions import ValidationError
from .models import Note, NoteCategory
class NoteAddForm(forms.Form):
    date = forms.DateField(label='Дата')
    text = forms.CharField(label='Текст', widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=NoteCategory.objects.all(),
                                      label='Категория'
                                      )
class NoteAddModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

class NoteFilterForm(forms.Form):
    category = forms.ModelMultipleChoiceField(
        queryset=NoteCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Категории',
        required=False)

    order = forms.ChoiceField(
        choices=[('new', 'новые'), ('old', 'старые')],
        label='Сортировка',
        required=False)
