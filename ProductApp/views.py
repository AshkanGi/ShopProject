from django.shortcuts import redirect
from django.views.generic import DetailView
from ProductApp.models import Product, Comment
from .forms import CommentCreatForm


class ProductView(DetailView):
    template_name = 'ProductApp/product-detail.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentCreatForm()
        return context

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        form = CommentCreatForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            comment = Comment()
            comment.product = product
            comment.user = request.user
            comment.title = cd['title']
            comment.body = cd['body']
            recommend_value = request.POST.get('recommend')
            if recommend_value is not None:
                comment.is_recommended = bool(int(recommend_value))
            else:
                comment.is_recommended = False
            comment.save()
            return redirect('ProductApp:detail', pk=product.pk)
        return self.get(request, *args, **kwargs)



