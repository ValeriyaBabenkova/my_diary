from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Note, NoteCategory
from .forms import NoteAddForm, NoteAddModelForm, NoteFilterForm

def notes(request):
    notes = Note.objects.all()
    note_form = NoteAddModelForm()

    active_category = None
    note_filter_form = NoteFilterForm(request.GET)
    if note_filter_form.is_valid():
        category = note_filter_form.cleaned_data['category']
        order = note_filter_form.cleaned_data['order']

        if category:
            notes = notes.filter(category__in=category)

        if order == 'new':
            notes = notes.order_by('-date')
        if order == 'old':
            notes = notes.order_by('date')

    if request.method == 'POST':
        note_form = NoteAddModelForm(request.POST)
        print(note_form)

        if note_form.is_valid():
            note_form.save()
            return redirect('notes')

    return render(request, 'main.html', {'notes': notes,'note_form':note_form, 'note_filter_form': note_filter_form})

@login_required
def note_edit(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if not Note.objects.filter(profile=request.user.profile, id=note_id).exists():
        raise Http404

    note_form = NoteAddModelForm(instance=note)

    if request.method == 'POST':
        note_form = NoteAddModelForm(request.POST, request.FILES, instance=note)

        if note_form.is_valid():
            note_form.save()
            return redirect('profiles_home')

    return render(request, 'note_edit.html', {'note_form': note_form})

def notes1(request):
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
