from django.shortcuts import render

from this_is_app.models import Product


# Create your views here.
def home_page(request):
    products = Product.objects.all()
    return render(request, 'this_is_app/home.html', {'products':products})