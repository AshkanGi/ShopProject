from django.contrib import admin
from .models import Product, Size, Color, GalleryImage, TopMaterial, SoleMaterial, InsoleModel
from . import models


class IntroductionAdmin(admin.StackedInline):
    model = models.Introduction


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price')
    inlines = (IntroductionAdmin,)


admin.site.register(Color)
admin.site.register(Size)
admin.site.register(GalleryImage)
admin.site.register(TopMaterial)
admin.site.register(SoleMaterial)
admin.site.register(InsoleModel)

