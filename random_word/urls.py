from django.urls import path
from . import views


urlpatterns = [
    path('random_word', views.index),
    path('generate_word', views.generate_word),
]
