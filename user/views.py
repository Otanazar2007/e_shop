from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user.forms import UserRegisterForm, UserLoginForm
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
