from rest_framework.serializers import ModelSerializer
from .models import FAQModel

class FAQSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FAQModel
