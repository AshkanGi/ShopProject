from random import randint
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail
from AccountApp.models import User, OTP
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout
from AccountApp.forms import RegisterForm, OTPVerifyForm, LoginForm, ResetPasswordForm


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'AccountApp/register and login.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            request.session['username_info'] = {'username': cd['username']}
            if User.objects.filter(username=cd['username']).exists():
                return redirect('AccountApp:login')
            code = randint(10000, 99999)
            print(code)
            OTP.objects.filter(username=cd['username']).delete()
            OTP.objects.create(username=cd['username'], code=code)
            if '@' in cd['username']:
                send_mail(
                    'Welcome to Rotikala Shop',
                    f'Your OTP code is {code}',
                    'AshkanGhodrati01@gmail.com',
                    [cd['username']]
                )
            else:
                pass   # سامانه sms
            return redirect('AccountApp:verify_code')
        return render(request, 'AccountApp/register and login.html', {'form': form})


class VerifyCode(View):
    def get(self, request):
        form = OTPVerifyForm()
        return render(request, 'AccountApp/verify-otp.html', {'form': form})

    def post(self, request):
        form = OTPVerifyForm(request.POST)
        user_info = request.session.get('user_info', {})
        username = user_info.get('username')
        if not username:
            messages.error(request, "مشکلی در ارتباط با سرور به وجود آمد. لطفا مجدد تلاش کنید.")
            return redirect('AccountApp:Register')
        if form.is_valid():
            cd = form.cleaned_data
            try:
                otp_instance = OTP.objects.get(username=username)
            except OTP.DoesNotExist:
                messages.error(request, "مشکلی در ارتباط با سرور به وجود آمد. لطفا مجدد تلاش کنید.")
                return redirect('AccountApp:Register')
            if cd['code'] == otp_instance.code:
                user = User.objects.create(username=username)
                login(request, user)
                otp_instance.delete()
                del request.session['username_info']
                return redirect('HomeApp:Home')
            form.add_error('code', 'کد معتبر نمیباشد')
            form.data = form.data.copy()
            form.data['code'] = ''
        return render(request, 'AccountApp/verify-otp.html', {'form': form})


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'AccountApp/login-password.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        user_info = request.session.get('username_info', {})
        username = user_info.get('username')
        if not username:
            messages.error(request, "مشکلی در ارتباط با سرور به وجود آمد. لطفا مجدد تلاش کنید.")
            return redirect('AccountApp:register')
        if form. is_valid():
            cd = form.cleaned_data
            user = authenticate(username=username, password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('HomeApp:Home')
            form.add_error('password', 'رمز عبور معتبر نمیباشد.')
        return render(request, 'AccountApp/login-password.html', {'form': form})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('HomeApp:Home')


class Forget(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'AccountApp/forgot.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if User.objects.filter(username=cd['username']).exists():
                request.session['username_info'] = {'username': cd['username']}
                code = randint(10000, 99999)
                print(code)
                OTP.objects.filter(username=cd['username']).delete()
                OTP.objects.create(username=cd['username'], code=code)
                if '@' in cd['username']:
                    send_mail(
                        'Welcome Back to Rotikala Shop',
                        f'Your OTP code is {code}',
                        'AshkanGhodrati01@gmail.com',
                        [cd['username']]
                    )
                pass  # سامانه sms
                return redirect('AccountApp:forget_otp')
            else:
                form.add_error('username', 'شماره موبایل یا ایمیل وارد شده وجود ندارد.')
        return render(request, 'AccountApp/forgot.html', {'form': form})


class ForgetOTPVerify(View):
    def get(self, request):
        form = OTPVerifyForm()
        return render(request, 'AccountApp/verify-otp.html', {'form': form})

    def post(self, request):
        form = OTPVerifyForm(request.POST)
        username_forget = request.session.get('username_info', {})
        username = username_forget.get('username')
        if not username:
            messages.error(request, "مشکلی در ارتباط با سرور به وجود آمد. لطفا مجدد تلاش کنید.")
            return redirect('AccountApp:forget')
        if form.is_valid():
            cd = form.cleaned_data
            try:
                otp_instance = OTP.objects.get(username=username)
            except OTP.DoesNotExist:
                messages.error(request, "مشکلی در ارتباط با سرور به وجود آمد. لطفا مجدد تلاش کنید.")
                return redirect('AccountApp:forget')
            if cd['code'] == otp_instance.code:
                return redirect('AccountApp:reset_password')
            else:
                form.add_error('code', 'کد معتبر نمیباشد')
                form.data = form.data.copy()
                form.data['code'] = ''
        return render(request, 'AccountApp/verify-otp.html', {'form': form})


class ResetPassword(View):
    def get(self, request):
        form = ResetPasswordForm()
        return render(request, 'AccountApp/forgot-reset.html', {'form': form})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        username_forget = request.session.get('username_info', {})
        user = username_forget.get('username')
        if not user:
            messages.error(request, "مشکلی در ارتباط با سرور به وجود آمد. لطفا مجدد تلاش کنید.")
            return redirect('AccountApp:forget')
        try:
            user = User.objects.get(username=user)
        except User.DoesNotExist:
            messages.error(request, "مشکلی در دریافت اطلاعات به وجود آمده. لطفا مجدد تلاش کنید.")
            return redirect('AccountApp:register')
        if form.is_valid():
            cd = form.cleaned_data
            password = cd['password']
            confirm_password = cd['confirm_password']
            if password == confirm_password:
                user.password = make_password(password)
                user.save()
                del request.session['username_info']
                return redirect('AccountApp:register')
            else:
                form = ResetPasswordForm
        return render(request, 'AccountApp/forgot-reset.html', {'form': form})


class EnterOTP(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'AccountApp/forgot.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if User.objects.filter(username=cd['username']).exists():
                request.session['username_info'] = {'username': cd['username']}
                code = randint(10000, 99999)
                print(code)
                OTP.objects.filter(username=cd['username']).delete()
                OTP.objects.create(username=cd['username'], code=code)
                if '@' in cd['username']:
                    send_mail(
                        'Welcome Back to Rotikala Shop',
                        f'Your OTP code is {code}',
                        'AshkanGhodrati01@gmail.com',
                        [cd['username']]
                    )
                else:
                    pass  # سامانه sms
                return redirect('AccountApp:enter_otp_verify')
            else:
                form.add_error('username', 'شماره موبایل یا ایمیل وارد شده وجود ندارد.')
        return render(request, 'AccountApp/forgot.html', {'form': form})


class EnterOTPVerify(View):
    def get(self, request):
        form = OTPVerifyForm()
        return render(request, 'AccountApp/verify-otp.html', {'form': form})

    def post(self, request):
        form = OTPVerifyForm(request.POST)
        username_forget = request.session.get('username_info', {})
        username = username_forget.get('username')
        if not username:
            messages.error(request, "مشکلی در دریافت اطلاعات به وجود آمده. لطفا مجدد تلاش کنید.")
            return redirect('AccountApp:register')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "مشکلی در دریافت اطلاعات به وجود آمده. لطفا مجدد تلاش کنید.")
            return redirect('AccountApp:register')
        if form.is_valid():
            cd = form.cleaned_data
            try:
                otp_instance = OTP.objects.get(username=user)
            except OTP.DoesNotExist:
                return redirect('AccountApp:enter_otp')
            if cd['code'] == otp_instance.code:
                login(request, user)
                otp_instance.delete()
                del request.session['username_info']
                return redirect('HomeApp:Home')
            else:
                form.add_error('code', 'کد معتبر نمیباشد')
                form.data = form.data.copy()
                form.data['code'] = ''
        return render(request, 'AccountApp/verify-otp.html', {'form': form})


class ResendOTP(View):
    def post(self, request):
        username_forget = request.session.get('username_info', {})
        username = username_forget.get('username')
        if not username:
            messages.error(request, "مشکلی در دریافت اطلاعات به وجود آمده. لطفا مجدد تلاش کنید.")
            return redirect('AccountApp:forget')
        code = randint(10000, 99999)
        print(f'New Code {code}')
        OTP.objects.filter(username=username).delete()
        OTP.objects.create(username=username, code=code)
        if '@' in username:
            send_mail(
                'Welcome Back to Rotikala Shop',
                f'Your OTP New Code is {code}',
                'AshkanGhodrati01@gmail.com',
                [username]
            )
        else:
            pass  # سامانه sms
        return JsonResponse({"success": True, "message": "کد جدید ارسال شد."})

