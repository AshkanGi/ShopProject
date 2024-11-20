from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Address
from .forms import AddAddressForm
from .cart_module import Cart
from ProductApp.models import Product
from .models import Order, OrderItem


class CartDetail(View):
    def get(self, request):
        cart = Cart(request)
        total_product = len(cart)
        return render(request, 'CartApp/checkout-cart.html', {'cart': cart, 'total_product': total_product})


class CartAdd(View):
    def post(self, request, pk):
        size, color, quantity = request.POST.get('size'), request.POST.get('color'), request.POST.get('quantity')
        product = get_object_or_404(Product, id=pk)
        cart = Cart(request)
        cart.add(product, quantity, color, size)
        return redirect('CartApp:cart_detail')


class CartRemove(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.remove(id)
        return redirect('CartApp:cart_detail')


class CartRemoveBasket(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.remove(id)
        return redirect('HomeApp:Home')


class CartClear(View):
    def get(self, request):
        cart = Cart(request)
        cart.clear()
        return redirect('CartApp:cart_detail')


class CartShipping(View):
    def get(self, request):
        cart = Cart(request)
        form = AddAddressForm()
        address = get_object_or_404(Address)
        total_product = len(cart)
        return render(request, 'CartApp/checkout-shipping.html', {'cart': cart, 'total_product': total_product, 'form': form, 'address': address})

    def post(self, request):
        form = AddAddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()

        return render(request, 'CartApp/checkout-shipping.html', {'form': form})


class CartPayment(View):
    def get(self, request):
        order = get_object_or_404(Order)
        cart = Cart(request)
        total_product = len(cart)
        return render(request, 'CartApp/checkout-payment.html', {'cart': cart, 'total_product': total_product, 'order':order})


class OrderCreation(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], color=item['color'], size=item['size'], quantity=item['quantity'], price=item['price'])

        return redirect('CartApp:cart_payment', order.id)