from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.FloatField(null=True,blank=True)
    image_url =  models.CharField(max_length=2083,blank=True)
    follow_author = models.CharField(max_length=2083,blank=True)
    book_available = models.BooleanField()

    def __str__(self):
        return self.title
class Order(models.Model):
    product=models.ForeignKey(Book,max_length=200,null=True,blank=True,on_delete=models.SET_NULL)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.title
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    image_url = models.CharField(max_length = 2083, default=False)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
