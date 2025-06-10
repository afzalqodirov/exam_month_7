from django.urls import path

# my import
from .views import accounts_register, accounts_show_profile

urlpatterns =[path('register/', accounts_register), path('profile/', accounts_show_profile)]
