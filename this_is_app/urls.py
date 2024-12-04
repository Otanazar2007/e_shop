from tkinter.font import names

from django.urls import path
from this_is_app import views

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
]