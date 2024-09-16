# Category/Views.from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Category, Product


def home(request):
    data = {
        "title": "Farmers' Direct Market Access",
        "categories": Category.objects.all(),
        "products": Product.objects.all()
    }
    return render(request, "categories/home.html", data)

def popularproduct(request):
    data = {
        "products": Product.objects.all()
    }
    return render(request, "categories/popularproducts.html", data)