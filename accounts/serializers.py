from rest_framework.serializers import ModelSerializer, CharField, Serializer

# my imports
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
                'extra_info',
                'photo',
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
                extra_info = validated_data.get('extra_info'),
                photo = validated_data.get('photo'))
        return user

#experimental! don't touch it
class ShowProfile(CustomUserSerializer):
    def get_fields(self):
        fields = super().get_fields()
        fields.pop('password')
        return fields

class PasswordChangeSerializer(Serializer):
    old_password = CharField(max_length=128)
    new_password = CharField(max_length=128)
    confirm_password = CharField(max_length=128)
    class Meta:
        fields = '__all__'
 
