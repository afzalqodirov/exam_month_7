from django.urls import path

# my import
from .views import accounts_register, accounts_show_profile, accounts_password_change

urlpatterns =[path('register/', accounts_register), path('profile/', accounts_show_profile), path('password/change/', accounts_password_change)]
