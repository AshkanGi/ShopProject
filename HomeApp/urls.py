from django.urls import path
from . import views

app_name = 'HomeApp'
urlpatterns = [
    path('', views.HomeView.as_view(), name='Home'),
    path('rules', views.RulesView.as_view(), name='rules'),
]