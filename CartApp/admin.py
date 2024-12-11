from django.contrib import admin
from .models import Address, OrderItem, Order, DiscountCode


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_paid')
    inlines = [OrderItemAdmin]


@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'discount')


admin.site.register(Address)