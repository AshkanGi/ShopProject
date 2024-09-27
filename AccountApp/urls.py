from django.urls import path
from . import views

app_name = 'AccountApp'
urlpatterns = [
    path('register', views.Register.as_view(), name='register'),
    path('verify_code', views.OtpVerify.as_view(), name='verify_code'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout')
]