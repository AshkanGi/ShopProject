from CartApp.cart_module import Cart
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'HomeApp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context


class RulesView(TemplateView):
    template_name = 'HomeApp/rules-and-terms.html'