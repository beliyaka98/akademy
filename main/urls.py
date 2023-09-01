from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.landing, name='landing'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('', views.main, name='main'),
]