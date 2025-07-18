from django.contrib import admin
from django.urls import path, include

# swagger imports and settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
schema = get_schema_view(openapi.Info('Bulletin of TUIT api', 'v01', 'The api for figma of <a target="_blank" href="https://www.figma.com/proto/QuEsUOqjoXJCJ8d4NBPlPs/TUIT-Bullet?node-id=1-2&scaling=scale-down-width&content-scaling=fixed">Bulletin of TUIT</a> and also,</p><p><a target="_blank" href="https://pub-7be1d45c4a744f86846c80e90df909eb.r2.dev/files/bbf32b34-00a0-4131-afd2-d40385c54f53.pdf">the documentation</a> (in Uzbek language)', contact=openapi.Contact('Afzal', 'https://t.me/Afzal006', 'htpafzal@gmail.com')))


# jwt authentication
# access and refresh token views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# my imports
from faq.views import show_faq
from accounts.views import accounts_register
from api_messages.views import send_message
from .views import get_main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('accounts/', include('accounts.urls')),
    path('requirements/', include('api_requirements.urls')),
    path('papers/', include('api_papers.urls')),
    path('faq/', show_faq),
    path('messages/', send_message),
    path('journals/', include('api_journals.urls')),
    path('api/uz/main/', get_main),
    path('api/ru/main/', get_main),
    path('api/en/main/', get_main),
    path('', schema.with_ui('swagger')),
    ]


# temporary! to add some requirements and faq
#from api_requirements.views import temp
#from faq.views import show_faq, tempp
# urlpatterns += [
#   path('temp/faq/create/', tempp),
#    path('temp/requirements/create/', temp),
#]
#from django.conf import settings
#from django.conf.urls.static import static
