"""
URL configuration for this_is_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from this_is_app import urls
from django.conf.urls.static import static
from django.conf import settings
from user.views import register_view, login_view, bank_cart
from this_is_app.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('this_is_app.urls'), name='home'),
    path('registration/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('about/',include('this_is_app.urls'), name='about_us'),
    path('bank_cart/', bank_cart, name = 'bank_cart'),
    path('logout/',logout, name = 'logout')
#    path('bank_cart/', include('this_is_app.urls'), name = 'bank_cart')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
