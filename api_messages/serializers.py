from rest_framework.serializers import ModelSerializer

# my import
from .models import MessagesModel

class MessagesSerializer(ModelSerializer):
    class Meta:
        # no first name added because the user is being added
        # the user have the first_name, last_name, email (required fields)
        fields = ['email', 'message']
        model = MessagesModel

    # the user will be added automatically
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
