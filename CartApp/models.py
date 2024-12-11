from django.db import models
from AccountApp.models import User
from ProductApp.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.PositiveSmallIntegerField(default=0)
    creat_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    size = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    quantity = models.PositiveSmallIntegerField(default=0)
    price = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.product.name


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    National_code = models.CharField(max_length=10)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.TextField(max_length=150)
    license_plate = models.CharField(max_length=4)
    Unit = models.CharField(max_length=4)
    Postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user.username} -- {self.province}'


class DiscountCode(models.Model):
    name = models.CharField(max_length=20, unique=True)
    discount = models.PositiveSmallIntegerField(default=0)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.name} , {self.quantity}'
