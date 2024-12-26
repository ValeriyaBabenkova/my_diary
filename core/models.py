from django.db import models

class Note(models.Model):
    date = models.DateField(verbose_name='Дата')
    text = models.TextField(verbose_name='Текст заметки', blank=True, null=True)


    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.text

# Create your models here.
