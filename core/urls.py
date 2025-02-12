from . import views
from django.urls import path

app_name = 'core'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('rules/', views.RulesView.as_view(), name='rules'),
]