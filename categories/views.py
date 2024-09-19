# Category/Views.from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import Category, Product


def home(request):
    data = {
        "title": "Farmers' Direct Market Access",
        "categories": Category.objects.all(),
        "products": Product.objects.all()
    }
    return render(request, "categories/home.html", data)

def switch_language(request, lang_code):
    # Validate the language code to ensure it's a supported language
    if lang_code in ['en', 'hi',]:  # List all your supported languages
        activate(lang_code)
       # request.session[LANGUAGE_SESSION_KEY] = lang_code

    # Get the URL of the page the user was on before switching the language
    # You might want to use `request.META.get('HTTP_REFERER')` to get the referring URL
    # or redirect to a specific URL if needed.
    next_url = request.META.get('HTTP_REFERER', '/')

    # Redirect back to the referring page or the home page
    return redirect(next_url)

def popularproduct(request):
    data = {
        "products": Product.objects.all()
    }
    return render(request, "categories/popularproducts.html", data)