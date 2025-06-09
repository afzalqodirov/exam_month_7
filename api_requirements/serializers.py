from rest_framework.serializers import ModelSerializer
from .models import RequirementsModel

class RequirementsSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RequirementsModel
