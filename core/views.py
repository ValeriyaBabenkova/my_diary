from django.shortcuts import render
from django.http import HttpResponse
from .models import Note, NoteCategory

def notes(request):
    # получить все записи
    notes = Note.objects.all()

    # добавить новую задачу
    if request.method == 'POST':
        date_data = request.POST['date']
        text_data = request.POST['text']
        category = request.POST.get('category')
        category = NoteCategory.objects.get(id=category)

        if date_data and text_data:
            Note.objects.create(date=date_data, text=text_data, category=category)

    return render(request, 'main.html', {'notes': notes})


# Create your views here.
