from django.db import models

# Create your models here.
class CategoryProduct(models.Model):
    category_name = models.CharField(max_length=50)
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