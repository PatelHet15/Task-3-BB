from django.shortcuts import render
from .models import Products
from django.db.models import Q

def product_list(request):
    products = Products.objects.all()

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)

    return render(request, 'q/product_list.html', {'products': products})
