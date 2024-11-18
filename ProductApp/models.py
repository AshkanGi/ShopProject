import random
from slugify import slugify
from django.db import models
from AccountApp.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Color(models.Model):
    color = models.CharField(max_length=25, verbose_name='رنگ')

    def __str__(self):
        return self.color


class Size(models.Model):
    size = models.CharField(max_length=25, verbose_name='سایز')

    def __str__(self):
        return self.size


class ProductGallery(models.Model):
    image = models.ImageField(upload_to='product/gallery', verbose_name='گالری')
    alt_text = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.alt_text


class TopMaterial(models.Model):
    top_material = models.CharField(max_length=15, verbose_name='جنس رویه')

    def __str__(self):
        return self.top_material


class SoleMaterial(models.Model):
    sole_material = models.CharField(max_length=15, verbose_name='جنس کفی')

    def __str__(self):
        return self.sole_material


class InsoleModel(models.Model):
    insole_model = models.CharField(max_length=15, verbose_name='جنس داخل')

    def __str__(self):
        return self.insole_model


class OpenClose(models.Model):
    open_close = models.CharField(max_length=20, verbose_name='نحوه باز و بسته شدن')

    def __str__(self):
        return self.open_close


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='نام محصول')
    color = models.ManyToManyField(Color, 'product', verbose_name='رنگ')
    size = models.ManyToManyField(Size, 'product', verbose_name='سایز')
    air_circulation = models.BooleanField(default=False, verbose_name='گردش هوا')
    waterproof = models.BooleanField(default=False, verbose_name='ضد اب')
    capsule_in_heel = models.BooleanField(default=False, verbose_name='کپسول فشار در قسمت پاشنه')
    capsule_in_claw = models.BooleanField(default=False, verbose_name='کپسول فشار در قسمت پنجه ')
    top_material = models.ManyToManyField(TopMaterial, 'product', verbose_name='جنس رویه')
    sole_material = models.ManyToManyField(SoleMaterial, 'product', verbose_name='جنس زیره')
    insole_model = models.ManyToManyField(InsoleModel, 'product', verbose_name='جنس کفی')
    open_close = models.ManyToManyField(OpenClose, 'product', verbose_name='نحوه باز و بسته شدن')
    main_image = models.ImageField(upload_to='product/main', verbose_name='عکس اصلی')
    gallery_image = models.ManyToManyField(ProductGallery, related_name='product', verbose_name='گالری')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True, allow_unicode=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='قیمت')
    discount_percentage = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        default=0,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name='تخفیف (%)'
    )

    @property
    def discounted_price(self):
        price = self.price * (1 - self.discount_percentage / 100)
        if self.discount_percentage:
            return format(price).rstrip('0').rstrip('.')
        return price

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name, allow_unicode=True)
            number = random.randint(10000, 99999)
            slug = f'{base_slug}-{number}'
            while Product.objects.filter(slug=slug).exists():
                number = random.randint(10000, 99999)
                slug = f'{base_slug}-{number}'
            self.slug = slug
        super().save()

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=40, null=True, blank=True)
    body = models.TextField()
    is_recommended = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.full_name} : {self.title}'