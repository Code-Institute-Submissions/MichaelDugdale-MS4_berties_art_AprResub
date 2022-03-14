from django.shortcuts import render

from products.models import Product

def index(request):
    """ View to return the index page """

    products = Product.objects.all()[:6]

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)