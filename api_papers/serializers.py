from rest_framework.serializers import ModelSerializer, CharField

# my imports 
from .models import PapersModel_UZ, PapersModel_RU, PapersModel_EN

class PapersSerializer(ModelSerializer):
    username = CharField(max_length=150, source='author.username', read_only=True)
    first_name = CharField(max_length=150, source='author.first_name', read_only=True)
    last_name = CharField(max_length=150, source='author.last_name', read_only=True)
    class Meta:
        fields = ['id', 'username', 'first_name', 'last_name', 'image', 'title', 'article', 'reference', 'views_count', 'download_link']
        read_only_fields = ['username', 'views_count']

    def create(self, validated_data):
        validated_data['author'] = self.context['user']
        return super().create(validated_data)

class PapersSerializer_UZ(PapersSerializer):
    class Meta(PapersSerializer.Meta):
        model = PapersModel_UZ

class PapersSerializer_RU(PapersSerializer):
    class Meta(PapersSerializer.Meta):
        model = PapersModel_RU

class PapersSerializer_EN(PapersSerializer):
    class Meta(PapersSerializer.Meta):
        model = PapersModel_EN
