from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница с продуктами
    path('contacts/', views.contact, name='contacts'),  # Страница контактов
]
