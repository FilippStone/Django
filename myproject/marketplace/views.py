from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from marketplace.models import Client, Product, Order
from django.db.models import Sum


def client(request):
    res = Client.objects.all()
    res1 = ''
    for i in res:
        res1 += str(i) + '<br>'
    return HttpResponse(f'{res1}')


def products(request):
    products = Product.objects.all()
    r = ''
    for i in products:
        r += str(i) + '<br>'
    return HttpResponse(f'{r}')


def order(request):
    order = Order.objects.all()
    r = ''
    for i in order:
        r += str(i) + '<br>'
    return HttpResponse(f'{r}')


def client_list(request):
    clients = Client.objects.all()
    orders = Order.objects.all
    context = {
        'clients': clients,
        'orders': orders,
    }
    return render(request, 'orders_list.html', context)


