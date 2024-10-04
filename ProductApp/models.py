from django.db import models
from django.views import View

from AccountApp.models import User


class Size(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size


class Color(models.Model):
    color = models.CharField(max_length=15)

    def __str__(self):
        return self.color


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='product/gallery')


class TopMaterial(models.Model):
    top_material = models.CharField(max_length=15)

    def __str__(self):
        return self.top_material


class SoleMaterial(models.Model):
    sole_material = models.CharField(max_length=15)

    def __str__(self):
        return self.sole_material


class InsoleModel(models.Model):
    insole_model = models.CharField(max_length=15)

    def __str__(self):
        return self.insole_model


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    size = models.ManyToManyField(Size, 'product', null=True, blank=True)
    color = models.ManyToManyField(Color, 'product', null=True, blank=True)
    air_circulation = models.BooleanField(default=False)
    waterproof = models.BooleanField(default=False)
    capsule_in_heel = models.BooleanField(default=False)
    capsule_in_claw = models.BooleanField(default=False)
    price = models.CharField(max_length=10, default=1000000)
    discount = models.CharField(max_length=4, null=True, blank=True)
    price_after_discount = models.CharField(max_length=9, null=True, blank=True)
    top_material = models.ManyToManyField(TopMaterial, 'product', null=True, blank=True)
    sole_material = models.ManyToManyField(SoleMaterial, 'product', null=True, blank=True)
    insole_model = models.ManyToManyField(InsoleModel, 'product', null=True, blank=True)
    main_image = models.ImageField(upload_to='product',)
    gallery_image = models.ManyToManyField(GalleryImage, 'product')

    def __str__(self):
        return self.product_name


class Introduction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='introduction', null=True, blank=True)
    text = models.TextField(default=None)

    def __str__(self):
        return self.text[:30]


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=40, null=True, blank=True)
    body = models.TextField()
    is_recommended = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    creat_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.full_name} : {self.title}'
