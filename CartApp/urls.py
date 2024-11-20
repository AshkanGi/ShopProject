from django.urls import path
from . import views

app_name = 'CartApp'

urlpatterns = [
    path('cart_detail', views.CartDetail.as_view(), name='cart_detail'),
    path('add/<int:pk>', views.CartAdd.as_view(), name='add_product'),
    path('remove/<str:id>', views.CartRemove.as_view(), name='remove_product'),
    path('remove_basket/<str:id>', views.CartRemoveBasket.as_view(), name='remove_product_basket'),
    path('cart_shipping', views.CartShipping.as_view(), name='cart_shipping'),
    path('cart_payment', views.CartPayment.as_view(), name='cart_payment'),
    path('order_creat', views.OrderCreation.as_view(), name='order_creat'),
    path('cart_clear', views.CartClear.as_view(), name='cart_clear'),

]