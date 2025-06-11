from django.contrib import admin

# my imports
from .models import PapersModel_UZ, PapersModel_RU, PapersModel_EN

admin.site.register(PapersModel_UZ)
admin.site.register(PapersModel_EN)
admin.site.register(PapersModel_RU)
