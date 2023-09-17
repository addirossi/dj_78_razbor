from django.http import Http404
from django.shortcuts import render

from main.models import Product, Category


def products_list(request):
    products = Product.objects.all()
    price_from = request.GET.get('price_from', 0)
    if price_from:
        products = products.filter(price__gte=price_from)

    price_to = request.GET.get('price_to', 0)
    if price_to:
        products = products.filter(price__lte=price_to)
    template_name = 'main/list.html'
    return render(request, template_name, {'products': products})


def products_by_category(request, category_slug):
    if not Category.objects.filter(slug=category_slug).exists():
        raise Http404('Такой категории не существует')
    products = Product.objects.filter(category_id=category_slug)
    template_name = 'main/list.html'
    return render(request, template_name, {'products': products})
