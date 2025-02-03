from django.views import View
from django.shortcuts import render
from CartApp.cart_module import Cart
from django.views.generic import TemplateView


class HomeView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        return render(request, 'core/home.html', {'cart': cart})


class RulesView(TemplateView):
    template_name = 'core/rules.html'