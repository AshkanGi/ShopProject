from . import views
from django.urls import path

app_name = 'ProfileApp'

url_patterns_data = [
    ('', views.ProfileDashboard),  # Dashboard
    ('profile_orders', views.ProfileOrders),
    ('profile_favorite', views.ProfileFavorites),
    ('profile_recent', views.ProfileRecent),
    ('profile_notification', views.ProfileNotification),
    ('profile_address', views.ProfileAddress),
    ('profile_edit', views.ProfileEdit),
    ('update_email', views.UpdateEmail),
    ('update_phone', views.UpdatePhone),
]

urlpatterns = [path(f'{pattern}/', view.as_view(), name=pattern or 'profile_dashboard') for pattern, view in url_patterns_data]
