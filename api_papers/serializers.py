from rest_framework.serializers import ModelSerializer, CharField

# my imports 
from .models import PapersModel

class PapersSerializer(ModelSerializer):
    username = CharField(max_length=150, source='author.username', read_only=True)
    class Meta:
        fields = ['username', 'image', 'title', 'article', 'reference', 'download_link']
        model = PapersModel
        read_only_fields = ['username']

    def create(self, validated_data):
        validated_data['author'] = self.context['user']
        return super().create(validated_data)
