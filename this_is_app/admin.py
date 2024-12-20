from django.contrib import admin
from .models import Product, CategoryProduct, UserCart, Favorites, BankCart
# Register your models here.
admin.site.register(CategoryProduct)
admin.site.register(Product)
admin.site.register(UserCart)
admin.site.register(Favorites)
admin.site.register(BankCart)