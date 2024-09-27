from random import randint

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views import View

from AccountApp.forms import RegisterForm, OtpVerifyForm, LoginForm
from AccountApp.models import User, OTP


class Register(View):
    def get(self, request):
        form = RegisterForm
        return render(request, 'AccountApp/register and login.html', {'form':form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            request.session['user_info'] = {
                'phone': cd['phone']
            }
            if User.objects.filter(phone=cd['phone']).exists():
                return redirect('AccountApp:login')
            code = randint(10000, 99999)
            print(code)
            OTP.objects.create(phone=cd['phone'], code=code)
            return redirect('AccountApp:verify_code')
        form.add_error('phone', 'شماره وارد شده معتبر نمیباشد.')
        return render(request, 'AccountApp/register and login.html', {'form': form})


class OtpVerify(View):
    def get(self, request):
        form = OtpVerifyForm
        return render(request, 'AccountApp/login-otp.html', {'form': form})

    def post(self, request):
        form = OtpVerifyForm(request.POST)
        user_session = request.session['user_info']
        phone = user_session['phone']
        code = OTP.objects.get(phone=phone)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code.code:
                user = User.objects.create(phone=phone)
                login(request, user)
                code.delete()
                return redirect('HomeApp:Home')
            form.add_error('code', 'کد وارد شده معتبر نمیباشد.')
        form.add_error('code',  'کد وارد شده معتبر نمیباشد.')
        return render(request, 'AccountApp/login-otp.html', {'form': form})


class Login(View):
    def get(self, request):
        form = LoginForm
        return render(request, 'AccountApp/login-password.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_info']
        phone = user_session['phone']
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=phone, password=cd['password'])
            login(request, user)
            return redirect('HomeApp:Home')
        form.add_error('password', 'رمز عبور معتبر نمیباشد.')
        return render(request, 'AccountApp/login-password.html')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('HomeApp:Home')