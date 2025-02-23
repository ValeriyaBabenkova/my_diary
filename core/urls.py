from django.urls import path, include

from .views import *

urlpatterns = [
    path('', notes, name='notes'),
    path('profiles/', include('profiles.urls'))
]
