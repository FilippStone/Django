from django.urls import path
from .views import client, order, products, client_list, upload_product

urlpatterns = [
    path('client/', client, name='client'),
    path('order/', order, name='order'),
    path('product/', products, name='products'),
    path('clients/', client_list, name='client_list'),
    path('media/', upload_product, name='upload_product')
]
