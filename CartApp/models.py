from django.db import models
from AccountApp.models import User
from ProductApp.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    creat_at = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='item')
    size = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    quantity = models.SmallIntegerField()
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.product.name


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    meli_code = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=20)
    ostan = models.CharField(max_length=20)
    plak = models.CharField(max_length=4)
    vahed = models.CharField(max_length=4)
    code_posti = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username