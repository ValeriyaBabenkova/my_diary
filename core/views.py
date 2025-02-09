from django.shortcuts import render
from django.http import HttpResponse
from .models import Note, NoteCategory

def notes(request):
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
        category = request.POST.get('NoteCategory')
        active_category = NoteCategory.objects.get(id=category)
        print(active_category)

        if date_data and text_data:
            Note.objects.create(date=date_data, text=text_data, category=active_category)

    categories = NoteCategory.objects.all()
    print(categories)

    return render(request, 'main.html', {'notes': notes, 'categories': categories})


# Create your views here.
