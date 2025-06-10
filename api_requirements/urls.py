from django.urls import path

#my imports
from api_requirements.views import retrieve_requirements, list_requirements

urlpatterns = [
    path('retrieve/', retrieve_requirements),
    path('list/', list_requirements),
        ]
