"""Define URL patterns for learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Show all topics
    path('topics/', views.topics, name='topics'),
    path('topic/', views.topic, name='topic'),
    path('entries/', views.entries, name='entries'),
    path('entry/', views.entry, name='entry'),
]