from django.contrib import admin
from . import models
from .models import Address


class OrderItemAdmin(admin.TabularInline):
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_paid')
    inlines = [OrderItemAdmin]


admin.site.register(Address)