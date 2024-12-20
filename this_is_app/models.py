from django.db import models

# Create your models here.
class CategoryProduct(models.Model):
    category_name = models.CharField(max_length=50)
    category_descr = models.TextField(max_length=2000)
    category_photo = models.FileField(upload_to='category_image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    pr_name = models.CharField(max_length=50)
    pr_descr = models.TextField(max_length=3000)
    pr_count = models.IntegerField()
    pr_price = models.FloatField()
    pr_photo = models.FileField(upload_to='product_image')
    pr_category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pr_name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"

class UserCart(models.Model):
    username = models.CharField(max_length=30)
    user_id = models.IntegerField()
    pr_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    pr_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User Cart'
        verbose_name_plural = 'User Carts'

class Favorites(models.Model):
    username = models.CharField(max_length=30)
    pr_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pr_name.pr_name

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = 'Favorites'

class BankCart(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=5)
    cvv = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bank Cart'
        verbose_name_plural = 'Bank Carts'