from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HomeApp.urls')),
    path('user/', include('AccountApp.urls')),
    path('profile/', include('ProfileApp.urls')),
]