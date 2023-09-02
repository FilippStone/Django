from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
]
