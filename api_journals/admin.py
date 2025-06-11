from django.contrib import admin

#my imports
from .models import JournalsModel_UZ, JournalsModel_RU, JournalsModel_EN
admin.site.register(JournalsModel_UZ)
admin.site.register(JournalsModel_RU)
admin.site.register(JournalsModel_EN)
