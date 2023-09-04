from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.landing, name='landing'),
    path('', views.main, name='main'),
]