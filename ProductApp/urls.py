from django.urls import path
from . import views

app_name = 'ProductApp'
urlpatterns = [
    path('<int:pk>', views.ProductView.as_view(), name='detail'),
]