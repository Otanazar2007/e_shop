from tkinter.font import names

from django.urls import path
from this_is_app import views
from user.views import bank_cart, profile_view, change_profile

urlpatterns = [
    path('', views.home_page, name='home'),
    path('product/<int:pk>/', views.product),
    path('categories/', views.category),
    path('about/', views.about_us),
    path('category/<int:pk>/', views.categories_page),
    path('add_to_cart/<int:pk>/', views.add_to_cart),
    path('cart/',views.user_cart, name='user_cart'),
    path('add_to_favorite/<int:pk>', views.add_to_favorite),
    path('favorites/', views.favorites, name = 'favorites'),
    path('bank_cart/', bank_cart, name = 'bank_cart'),
    path('profile/', profile_view, name = 'profile' ),
    path('change_profile/', change_profile, name = 'change_profile')
#    path('bank_cart_right/', views.bank_cart_right, name = 'bank_cart_right')
]