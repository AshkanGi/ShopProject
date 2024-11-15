from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'HomeApp/index.html'


class RulesView(TemplateView):
    template_name = 'HomeApp/rules-and-terms.html'