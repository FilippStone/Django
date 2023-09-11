from django.shortcuts import render
from django.http.response import HttpResponse
from marketplace.models import Client, Product, Order


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
