from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .forms import CommentCreatForm
from .models import Product, Comment


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
            comment.user = request.user
            comment.product = product
            comment.title = cd['title']
            comment.body = cd['body']
            recommend_value = request.POST.get('recommend')
            if recommend_value is not None:
                comment.is_recommended = bool(int(recommend_value))
            else:
                comment.is_recommended = False
            comment.save()
            return redirect('ProductApp:detail', slug=product.slug)
        messages.error(request, 'اطلاعات وارد شده معتبر نیست.')
        return self.get(request, *args, **kwargs)