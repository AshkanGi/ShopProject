from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from ProfileApp.forms import UpdateEmailForm, UpdatePhoneForm


class ProfileDashboard(View):
    def get(self, request):
        return render(request, 'ProfileApp/profile-dashboard.html')


class ProfileOrders(View):
    def get(self, request):
        return render(request, 'ProfileApp/profile-orders.html')


class ProfileFavorites(View):
    def get(self, request):
        return render(request, 'ProfileApp/profile-favorite.html')


class ProfileRecent(View):
    def get(self, request):
        return render(request, 'ProfileApp/profile-recent.html')


class ProfileNotification(View):
    def get(self, request):
        return render(request, 'ProfileApp/profile-notification.html')


class ProfileAddress(View):
    def get(self, request):
        return render(request, 'ProfileApp/profile-address.html')


class ProfileEdit(View):
    def get(self, request):
        return render(request, 'ProfileApp/profile-edit.html')


class UpdateFullName(View):
    def post(self, request):
        full_name = request.POST.get('full_name')
        if full_name:
            user = request.user
            user.full_name = full_name
            user.save()
        return redirect('ProfileApp:profile_edit')


class UpdateEmail(View):
    def post(self, request):
        form = UpdateEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = request.user
            user.email = email
            user.save()
            messages.success(request, "ایمیل شما با موفقیت تغییر یافت.")
        else:
            messages.error(request, "ایمیل وارد شده معتبر نیست.")
        return redirect('ProfileApp:profile_edit')


class UpdatePhone(View):
    def post(self, request):
        form = UpdatePhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            user = request.user
            user.phone = phone
            user.save()
            messages.success(request, "شماره موبایل شما با موفقیت تغییر یافت.")
        else:
            messages.error(request, "شماره موبایل وارد شده معتبر نیست.")
        return redirect('ProfileApp:profile_edit')