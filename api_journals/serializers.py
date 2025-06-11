from rest_framework.serializers import ModelSerializer

# my imports 
from .models import JournalsModel_UZ, JournalsModel_RU, JournalsModel_EN

class JournalsSerializerList_UZ(ModelSerializer):
    class Meta:
        fields = ['id', 'image', 'title', 'article', 'reference']
        model = JournalsModel_UZ

class JournalsSerializerList_RU(ModelSerializer):
    class Meta:
        fields = ['id', 'image', 'title', 'article', 'reference']
        model = JournalsModel_RU

class JournalsSerializerList_EN(ModelSerializer):
    class Meta:
        fields = ['id', 'image', 'title', 'article', 'reference']
        model = JournalsModel_EN

class JournalsSerializer_UZ(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = JournalsModel_UZ

class JournalsSerializer_RU(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = JournalsModel_RU

class JournalsSerializer_EN(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = JournalsModel_EN


