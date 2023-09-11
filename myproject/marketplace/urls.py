from django.urls import path
from . import views


urlpatterns = [
    path('client/', views.client, name='client'),
    path('order/', views.order, name='order'),
    path('product/', views.products, name='products'),
]