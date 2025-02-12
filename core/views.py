from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note, NoteCategory
from .forms import NoteAddForm

def notes(request):
    notes = Note.objects.all()
    note_form = NoteAddForm()
    if request.method == 'POST':
        note_form = NoteAddForm(request.POST)
        print(note_form)

        if note_form.is_valid():
            date_data = note_form.cleaned_data['date']
            text_data = note_form.cleaned_data['text']
            category = note_form.cleaned_data['category']
            Note.objects.create(date=date_data, text=text_data, category=category)
            return redirect('notes')

    return render(request, 'main.html', {'notes': notes,'note_form':note_form})


def notesOld(request):
    # получить все записи
    notes = Note.objects.all()
    print(notes)

    category = request.GET.get('category')
    print(category)

    active_category = None
    print(active_category)

    # добавить новую задачу
    if request.method == 'POST':
        print(request.POST)
        date_data = request.POST.get('date')
        text_data = request.POST.get('text')
        category = request.POST.get('category')
        active_category = NoteCategory.objects.get(id=category)
        print(active_category)

        if date_data and text_data:
            Note.objects.create(date=date_data, text=text_data, category=active_category)

    categories = NoteCategory.objects.all()
    print(categories)

    return render(request, 'main.html', {'notes': notes, 'categories': categories})


# Create your views here.
