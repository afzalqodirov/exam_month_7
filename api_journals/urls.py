from django.urls import path
from .views import get_journals, retrieve_journal

urlpatterns = [
    path('uz/list/', get_journals),
    path('ru/list/', get_journals),
    path('en/list/', get_journals),
    path('uz/retrieve/', retrieve_journal),
    path('ru/retrieve/', retrieve_journal),
    path('en/retrieve/', retrieve_journal),
    ]
