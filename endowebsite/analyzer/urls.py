from django.urls import path

from . import views


app_name = 'analyzer'
urlpatterns = [
    path('analize/', views.analize, name='analize'),
]

