from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(available=True)[:4]
    context = {
        'categories': categories,
        'featured_products': featured_products,
    }
    return render(request, 'products/home.html', context)


def catalog(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    current_category = None

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    context = {
        'categories': categories,
        'products': products,
        'current_category': current_category,
    }
    return render(request, 'products/catalog.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    context = {
        'product': product,
    }
    return render(request, 'products/detail.html', context)