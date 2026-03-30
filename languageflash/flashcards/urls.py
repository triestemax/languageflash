from django.urls import path
from . import views

app_name = 'flashcards'

urlpatterns = [
    path('', views.index, name='index'),
    path('cards/', views.cards_list, name='cards_list'),
    path('add-card/', views.add_card, name='add_card'),
    path('quiz/', views.quiz, name='quiz'),
    path('stats/', views.stats, name='stats'),
]
