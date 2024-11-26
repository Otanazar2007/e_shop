from django.contrib import admin
from .models import Product, CategoryProduct, UserCart
# Register your models here.
admin.site.register(CategoryProduct)
admin.site.register(Product)
admin.site.register(UserCart)