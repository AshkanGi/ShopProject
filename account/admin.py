from .models import User, OTP
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ["username", "full_name", "phone", "email", "date_joined", "last_login", "is_admin"]
    readonly_fields = ["date_joined", "last_login"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["username", "password"]}),
        ("Personal info", {"fields": ["full_name", "phone", "email", "date_joined", "last_login"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    add_fieldsets = [(None, {"classes": ["wide"], "fields": ["username", "password1", "password2"]}),]
    search_fields = ["username", "full_name", "phone", "email"]
    ordering = ["username"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.register(OTP)
admin.site.unregister(Group)
