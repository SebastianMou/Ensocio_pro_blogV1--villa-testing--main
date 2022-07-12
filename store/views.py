from django.shortcuts import render, get_object_or_404
from .models import Category, Product, FerWidget, ComunicationsLinks
from django.core.paginator import Paginator

# Create your views here.
def catigories(request):
    return {
        'catigories':Category.objects.all() 
    }

def home(request):
    products = Product.objects.all()
    #set up pagination
    p = Paginator(Product.objects.all(), 6)
    page = request.GET.get('page')
    productsss = p.get_page(page)
    ferwidget = FerWidget.objects.all()
    comunicationslinks = get_object_or_404(ComunicationsLinks)
    return render(request, 'store/home.html', {'products':products, 'productsss':productsss ,'ferwidget':ferwidget, 'comunicationslinks':comunicationslinks})

def about(request):
    return render(request, 'store/about.html')

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    ferwidget = FerWidget.objects.all()
    comunicationslinks = get_object_or_404(ComunicationsLinks)
    return render(request, 'store/products/detail.html', {'product': product, 'ferwidget':ferwidget, 'comunicationslinks':comunicationslinks})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})