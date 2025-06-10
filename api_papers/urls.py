from django.urls import path

# my imports
from .views import post_paper, get_papers

urlpatterns = [
    path('create/', post_paper),
    path('list/', get_papers),
    ]
