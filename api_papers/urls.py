from django.urls import path
from drf_yasg.utils import swagger_auto_schema

# my imports
from .views import post_paper, get_papers, retrieve_paper

urlpatterns = [
    path('uz/create/', post_paper),
    path('ru/create/', post_paper),
    path('en/create/', post_paper),
    path('uz/list/', get_papers),
    path('ru/list/', get_papers),
    path('en/list/', get_papers),
    path('uz/retrieve/', retrieve_paper),
    path('ru/retrieve/', retrieve_paper),
    path('en/retrieve/', retrieve_paper),
    ]
