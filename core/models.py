from django.db import models
class NoteCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.title
class Note(models.Model):
    date = models.DateField(verbose_name='Дата')
    text = models.TextField(verbose_name='Текст заметки', blank=True, null=True)
    category = models.ForeignKey(NoteCategory, blank=True, null=True, on_delete=models.SET_NULL,
                                 verbose_name='Категория')
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
    def __str__(self):
        return self.text

# Create your models here.
