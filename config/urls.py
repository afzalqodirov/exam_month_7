from django.contrib import admin
from django.urls import path

# swagger imports and settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
schema = get_schema_view(openapi.Info('Bulletin of TUIT api', 'v01', 'The api for figma of Bulletin of TUIT', contact=openapi.Contact('Afzal', 'https://t.me/Afzal006', 'htpafzal@gmail.com')))

# jwt authentication
# access and refresh token views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# my single imports
from api_requirements.views import get_requirements

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('api/requirements/', get_requirements),
    path('', schema.with_ui('swagger')),
]
