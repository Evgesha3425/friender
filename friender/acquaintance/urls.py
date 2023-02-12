from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('hosts/', views.hosts, name='hosts'),
    path('guests/', views.guests, name='guests'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('grades/', views.grades, name='grades'),
]
