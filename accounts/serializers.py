from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class CustomUserSerializer(ModelSerializer):
    class Meta:
        fields = [
                'first_name',
                'last_name',
                'username', 
                'email', 
                'password', 
                'birth_date', 
                'scientific_degree', 
                'organization', 
                'extra_info'
                ]
        model = CustomUser
        extra_kwargs = {
                'first_name':{'required':True},
                'last_name':{'required':True},
                }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
                username = validated_data.get('username'),
                first_name = validated_data.get('first_name'),
                last_name = validated_data.get('last_name'),
                email = validated_data.get('email'),
                password = validated_data.get('password'),
                birth_date = validated_data.get('birth_date'),
                scientific_degree = validated_data.get('scientific_degree'),
                organization = validated_data.get('organization'),
                extra_info = validated_data.get('extra_info'))
        return user

    #experimental! don't touch it
    def get_fields(self):
        fields = super().get_fields()
        fields.pop('password')
        return fields
