from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

def notes(request):
    notes = Note.objects.all()
    return render(request, 'main.html', {'notes': notes})

# Create your views here.
