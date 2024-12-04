from pickle import format_version

from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404

from this_is_app.models import Product, CategoryProduct, UserCart, Favorites
from user.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
import telebot
bot = telebot.TeleBot('8131551618:AAFiY4nVNUIx9KONOGsjbIwXD0fXlC0HR00')

# Create your views here.
def home_page(request):
    products = Product.objects.all()
    return render(request, 'this_is_app/home.html', {'products':products})

def product(request, pk):
    products = Product.objects.filter(id=pk)
    context = {
        'products':products
    }
    return render(request, 'this_is_app/product_page.html', context)

def category(request):
    categories = CategoryProduct.objects.all()
    return render (request, 'this_is_app/categories.html', {'categories':categories})

@login_required()
def about_us(request):
    return render(request, 'this_is_app/about.html', {'request':request})


@login_required()
def categories_page(request, pk):
    categories = CategoryProduct.objects.get(id=pk)
    products = Product.objects.filter(pr_category=categories).all()
    return render(request, 'this_is_app/categories_page.html', {'products':products,
                                                                        'categories':categories})

@login_required()
def add_to_cart(request, pk):
    if request.method == 'POST':
        checker = Product.objects.get(id=pk)
        if checker.pr_count >= int(request.POST.get('pr_count')):
            UserCart.objects.create(user_id = request.user.id,
                                    pr_name = checker,
                                    pr_count = int(request.POST.get('pr_count')))
            return redirect('user_cart')
        else:
            return redirect('home')

@login_required()
def user_cart(request):
    cart = UserCart.objects.filter(user_id=request.user.id).all()
    if request.method == 'POST':
        text = 'Новый заказ!'
        for c in cart:
            text += (f'\nID пользователя {c.user_id}'
                     f'\n Товар {c.pr_name.pr_name}')
            bot.send_message('-4592099015', text )
    return render(request, 'this_is_app/user_cart.html', {'cart':cart})

@login_required()
def add_to_favorite(request, pk):
    if request.method == "POST":
        fv_prod = Product.objects.get(id=pk)
        Favorites.objects.create(pr_name = fv_prod,
                                 username = request.user.username)
        favorites = Favorites.objects.filter(username=request.user.username)
        return render(request, 'this_is_app/favorites.html', {'favorites':favorites})
    else:
         return redirect('home')

@login_required()
def favorites(request):
    if request.method == 'GET':
        favorites = Favorites.objects.filter(username = request.user.username).all()
        return render(request, 'this_is_app/favorites.html', {'favorites':favorites})
    else:
        return redirect('home')