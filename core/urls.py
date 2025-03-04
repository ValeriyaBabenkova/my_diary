from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.notes, name='notes'),
    path('notes/<int:note_id>/edit', views.note_edit, name='note_edit'),
]
