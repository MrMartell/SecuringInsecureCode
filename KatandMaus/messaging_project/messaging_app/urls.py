from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_messages, name='list_messages'),
    path('compose/', views.compose_message, name='compose_message'),
]
