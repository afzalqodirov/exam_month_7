from django.contrib import admin
from .models import FAQModel

class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')
admin.site.register(FAQModel, FAQAdmin)
# Register your models here.
